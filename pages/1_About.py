import streamlit as st

st.set_page_config(
    page_title="Zsolt Fehér",
    page_icon="📊",
)

# Sidebar configuration
st.sidebar.success("Select a tab above.")

# # Page information

st.write("# Zsolt Fehér")

st.markdown(
"""

   My project was to conclude an exploratory data analysis and machine learning classification task using a cardiovascular disease risk dataset sourced from the BRFSS survey. 
   The EDA is a detailed overview of the dataset structure, including feature types and distributions. 
   Key questions are addressed, such as age group representation, prevalence of heart disease, and relationships between health indicators. 
   Data preprocessing steps included cleaning, feature selection, and balancing the target variable. 
   For the classification task, I evaluated several models for predicting heart disease risk. 
   Performance was assessed using cross-validation and metrics such as accuracy, precision, recall, and F1-score. 
   The random forest classifier demonstrated the best overall performance, making it a strong candidate for predicting heart disease risk based on selected features. 


"""
)


