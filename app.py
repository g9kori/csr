# Install required packages
# pip install streamlit pandas scikit-learn

import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Load sample datasets (replace with actual datasets)
# Load sample datasets (replace with actual datasets)
@st.cache_data
def load_data():
    # Simulate restaurant dataset
    restaurants = pd.DataFrame({
        'Restaurant_ID': [1, 2, 3],
        'Name': ['Spicy Hut', 'Pasta Palace', 'Sushi World'],
        'Cuisine': ['Indian', 'Italian', 'Japanese'],
        'Menu': [
            'naan, curry, rice, spices',
            'pasta, pizza, olive oil, cheese',
            'sushi, soy sauce, wasabi, rice'
        ]
    })

    # Simulate product dataset
    products = pd.DataFrame({
        'Product_ID': [101, 102, 103, 104, 105],
        'Name': ['Rice', 'Pasta', 'Spices', 'Soy Sauce', 'Cheese'],
        'Category': ['Grain', 'Grain', 'Condiment', 'Condiment', 'Dairy'],
        'Cuisine_Compatibility': ['Indian, Japanese', 'Italian', 'Indian', 'Japanese', 'Italian']
    })

    return restaurants, products


# Recommend products based on content similarity
def recommend_products(restaurant_id, restaurants, products):
    # Extract restaurant and product information
    restaurant = restaurants[restaurants['Restaurant_ID'] == restaurant_id]
    if restaurant.empty:
        return "Restaurant not found!"

    restaurant_profile = restaurant['Menu'].iloc[0]

    # Combine product metadata into a single string
    products['Profile'] = (
        products['Name'] + " " +
        products['Category'] + " " +
        products['Cuisine_Compatibility']
    )

    # Compute similarity using TF-IDF
    tfidf = TfidfVectorizer(stop_words='english')
    profiles = tfidf.fit_transform(pd.concat([products['Profile'], pd.Series([restaurant_profile])]))

    similarity_matrix = cosine_similarity(profiles)

    # Get similarity scores for the restaurant
    scores = similarity_matrix[-1][:-1]
    products['Similarity'] = scores

    # Sort products by similarity
    recommendations = products.sort_values(by='Similarity', ascending=False)
    return recommendations[['Product_ID', 'Name', 'Category', 'Similarity']]


    # Compute similarity using TF-IDF
    tfidf = TfidfVectorizer(stop_words='english')
    profiles = tfidf.fit_transform(products['Profile'].append(pd.Series(restaurant_profile)))
    similarity_matrix = cosine_similarity(profiles)

    # Get similarity scores for the restaurant
    scores = similarity_matrix[-1][:-1]
    products['Similarity'] = scores

    # Sort products by similarity
    recommendations = products.sort_values(by='Similarity', ascending=False)
    return recommendations[['Product_ID', 'Name', 'Category', 'Similarity']]


# Streamlit App
st.title("Cold-Start Recommendation Engine")
st.write("Generate product recommendations for restaurants!")

# Load data
restaurants, products = load_data()

# Sidebar: Select a restaurant
restaurant_ids = restaurants['Restaurant_ID'].tolist()
selected_restaurant_id = st.sidebar.selectbox("Select a Restaurant ID", restaurant_ids)

# Display selected restaurant details
st.subheader("Selected Restaurant Details")
selected_restaurant = restaurants[restaurants['Restaurant_ID'] == selected_restaurant_id]
st.write(selected_restaurant)

# Generate recommendations
st.subheader("Recommended Products")
recommendations = recommend_products(selected_restaurant_id, restaurants, products)
st.write(recommendations)