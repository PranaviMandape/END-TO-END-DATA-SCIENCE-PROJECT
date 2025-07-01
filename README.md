# END-TO-END-DATA-SCIENCE-PROJECT

# Task-3

Company: CODTECH IT SOLUTIONS PVT. LTD.

Name: Mandape Pranavi Vilas

Intern ID: CT04DG1467

Domain: Data Science

Duration: 4 weeks

Mentor: Neela Santhosh Kumar

# Project Description

This project involves developing a complete end-to-end data science solution, from data collection and preprocessing to model training, evaluation, and deployment. The primary objective was to build a predictive model that can determine whether a patient is diabetic based on medical diagnostic measurements. To make this solution accessible, a web application interface was built using Flask, enabling users to interact with the model in real time.

# Objective

The main goal of this project is to showcase the entire data science workflow in a single, integrated pipeline. This includes data preprocessing, model training, evaluation, saving the trained model, and finally creating a user-friendly web app to demonstrate the model’s predictive capabilities. By the end of this project, the system can reliably classify patients as diabetic or non-diabetic based on input features.

# Tools & Technologies

Jupyter Notebook

Python

Pandas & NumPy

Flask

HTML/CSS (Jinja Templates)

Joblib

# Workflow & Features

Data Collection & Preprocessing: The project uses the Pima Indians Diabetes dataset. Data preprocessing steps include handling missing values, feature scaling using standardization, and splitting the dataset into training and testing sets.

Model Building: A logistic regression model was selected due to its interpretability and efficiency for binary classification problems. The model was trained and evaluated using appropriate metrics like accuracy and confusion matrix.

Model Saving: The trained model and scaler were saved as .pkl files using joblib for easy reuse during deployment.

Flask Web App: A simple web interface was developed where users can input patient details (such as pregnancies, glucose level, BMI, etc.). On submission, the data is processed, scaled, and fed to the trained model to generate predictions, which are then displayed to the user.

Deployment: The app runs locally using Flask’s development server and can be further deployed on platforms like Heroku or AWS for wider access.

# Challenges Faced

A major challenge was integrating the preprocessing steps into the deployment pipeline to ensure that user inputs are transformed consistently before prediction. This was addressed by saving and reusing the scaler object. Additionally, designing a clean and intuitive user interface required careful mapping of input fields to model features to avoid confusion.

# Outcomes

The project successfully delivered a fully functional and deployed diabetes prediction system. Users can easily enter patient health metrics into a web form and receive instant feedback on the diabetes risk prediction. This solution demonstrates practical application of data science and machine learning concepts, showcasing the journey from raw data to a live, interactive product.







