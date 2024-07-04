# HeartGuard: Heart Disease Detection Application

Heart disease remains a significant global health challenge, contributing to a substantial portion of worldwide mortality. Early detection and accurate prediction of heart disease are crucial for timely intervention and improved patient outcomes. This report introduces a heart disease detection application developed using modern machine learning techniques and implemented with the FastAPI framework.

## Purpose and Scope

The purpose of this application is to predict the likelihood of heart disease in individuals based on various clinical and demographic factors. By leveraging machine learning models trained on historical medical data, the application aims to assist healthcare providers in:

- Identifying individuals at higher risk of heart disease.
- Guiding appropriate diagnostic and treatment decisions.
- Enhancing preventive care strategies tailored to individual patient profiles.

## Features and Functionality

**1. Input Parameters**

The application accepts inputs such as:
- **Age**: Age of the patient.
- **Sex**: Gender of the patient (encoded as 0 for female, 1 for male).
- **Chest Pain Type**: Type of chest pain experienced by the patient.
- **Blood Pressure (BP)**: Systolic blood pressure measurement.
- **Cholesterol**: Cholesterol levels in mg/dL.
- **Fasting Blood Sugar (FBS)**: Fasting blood sugar level (> 120 mg/dL represented as 1, otherwise 0).
- **Resting ECG (EKG)**: Results of the resting electrocardiogram (0 for normal, 1 for abnormal).
- **Maximum Heart Rate Achieved (Max HR)**: Maximum heart rate achieved during exercise.
- **Exercise-Induced Angina**: Presence of angina induced by exercise (1 for yes, 0 for no).
- **ST Depression**: ST depression induced by exercise relative to rest.
- **Slope of ST Segment**: Slope of the peak exercise ST segment (1 for upsloping, 2 for flat).
- **Number of Major Vessels (Fluoroscopy)**: Number of major vessels colored by fluoroscopy.
- **Thallium Test Result**: Results of thallium stress test (3 for normal, 6 for reversible defect, 7 for fixed defect).

**2. Prediction Model**

The heart disease prediction model is trained using machine learning algorithms such as logistic regression, random forests, or gradient boosting. It utilizes a dataset with labeled examples of patients' attributes and their corresponding heart disease outcomes. You can find the dataset [here](https://data.world/informatics-edu/heart-disease-prediction).

**3. Output**

Upon receiving input parameters, the application predicts the likelihood of heart disease (binary classification: 0 for no disease, 1 for presence of disease). The prediction is accompanied by a confidence score or probability estimate, providing transparency in the prediction's reliability.

## Implementation Details

The application is developed using FastAPI, a modern, fast (high-performance), web framework for building APIs with Python. FastAPI provides robust support for handling HTTP requests, form data, and integrating machine learning models seamlessly.

##  Installation
```bash
# Clone the repository
git clone https://github.com/VergilX/ibm-skillsbuild-project
cd ibm-skillsbuild-project

# Create virtual environment
python -m venv env

# Open environment (for linux)
# For windows most likely `.\env\Scripts\activate.bat` in Command Prompt
# If it's not, figure it out :p
source env/bin/activate

# Install the python packages
pip install -r requirements.txt

# Run the server backend
fastapi dev api.py
```

Open the link provided in console where you ran the last command (Most likely [`http://localhost:8000/`](http://localhost:8000/)).

## Contributors
- [Shiva Surendran](https://github.com/Shiva-Surendran)
- [Joseph T S](https://github.com/Joey-TS)
- [Abhinand D Manoj](https://github.com/VergilX)

## Conclusion

In conclusion, the heart disease detection application represents a significant advancement in leveraging machine learning and web technologies to enhance cardiovascular health assessment. By empowering healthcare providers with accurate predictive tools, the application aims to contribute to early diagnosis, personalized treatment strategies, and improved patient outcomes in the fight against heart disease.

This report outlines the rationale, functionality, and implementation approach of the heart disease detection application, underscoring its potential impact in clinical practice and public health initiatives.
