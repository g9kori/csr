# Cold-Start Recommendation for B2B E-commerce

## Project Description
This project is a recommendation engine designed to address the **cold-start problem** for a B2B e-commerce platform that supplies raw materials to restaurants. The platform lacks historical interaction data, so the recommendation system leverages restaurant metadata (e.g., cuisine type, menu) and product features to provide personalized suggestions. The system uses **content-based filtering** and is deployed via a user-friendly **Streamlit** application.


## Requirements
To run this project, make sure you have the following dependencies installed. You can also use the provided `requirements.txt` file to install them automatically:
pandas==1.5.3 streamlit==1.25.0 scikit-learn==1.2.2 numpy==1.24.3 nltk==3.8.1 matplotlib==3.7.1 seaborn==0.12.2


## How to Run This Project
Follow these steps to set up and run the project locally:

1. **Clone or Download the Repository**:  
   Download the project files to your local machine.

2. **Set Up a Virtual Environment** (Optional but recommended):  
   In Terminal:
   python -m venv env
   source env/bin/activate       # On Mac/Linux
   env\Scripts\activate          # On Windows

3. **Install Dependencies**:
   Use the provided requirements.txt file to install the required libraries:
   pip install -r requirements.txt

4. **Run the Streamlit App**:
   Navigate to the project directory and execute the following command:
   streamlit run app.py

5. **Interact with the Application**:
   - Select a restaurant from the sidebar.
   - View personalized product recommendations based on restaurant metadata.