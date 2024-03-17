# Predicting Heart Disease using Machine Learning

This project focuses on utilizing various Python-based machine learning and data science libraries to build a model capable of predicting whether or not an individual has heart disease based on their medical attributes.

## 1. Problem Definition

The primary objective is to develop a predictive model that can accurately determine the presence or absence of heart disease in patients based on their clinical parameters and medical history.

## 2. Data Sources

The original dataset used in this project is obtained from the Cleavland data from the UCI Machine Learning Repository, accessible through the following link: [UCI Machine Learning Repository - Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/heart+Disease).

Additionally, a version of the dataset is available on Kaggle, accessible here: [Kaggle Heart Disease Classification Dataset](https://www.kaggle.com/datasets/sumaiyatasmeem/heart-disease-classification-dataset).

## 3. Features

The dataset comprises several features that serve as inputs to our predictive model:

1. **age**: Age of the patient in years.
2. **sex**: Gender of the patient (1 = male; 0 = female).
3. **cp**: Chest pain type, categorized as:
    - 0: Typical angina (chest pain related to decreased blood supply to the heart).
    - 1: Atypical angina (chest pain not related to the heart).
    - 2: Non-anginal pain (typically esophageal spasms, not heart-related).
    - 3: Asymptomatic (chest pain not showing signs of disease).
4. **trestbps**: Resting blood pressure (mm Hg) on admission to the hospital, where values above 130-140 are typically concerning.
5. **chol**: Serum cholesterol level in mg/dl, with values above 200 indicating a cause for concern.
6. **fbs**: Fasting blood sugar level (> 120 mg/dl) (1 = true; 0 = false), where levels '>126' mg/dL signal diabetes.
7. **restecg**: Resting electrocardiographic results, categorized as:
    - 0: Normal.
    - 1: ST-T Wave abnormality (signals non-normal heart rhythm).
    - 2: Possible or definite left ventricular hypertrophy (enlarged heart's main pumping chamber).
8. **thalach**: Maximum heart rate achieved during exercise.
9. **exang**: Exercise-induced angina (1 = yes; 0 = no).
10. **oldpeak**: ST depression induced by exercise relative to rest, indicating the stress of the heart during exercise.
11. **slope**: The slope of the peak exercise ST segment, categorized as:
    - 0: Upsloping (better heart rate with exercise, uncommon).
    - 1: Flatsloping (typical healthy heart response).
    - 2: Downsloping (signs of an unhealthy heart).
12. **ca**: Number of major vessels (0-3) colored by fluoroscopy, indicating blood movement (more movement is better).
13. **thal**: Thallium stress test result, categorized as:
    - 1, 3: Normal.
    - 6: Fixed defect (previously a defect but currently okay).
    - 7: Reversible defect (improper blood movement during exercise).
14. **target**: Presence of heart disease (1 = yes, 0 = no) - the predicted attribute.

The model's performance will be evaluated based on its ability to accurately predict the presence or absence of heart disease using these features.