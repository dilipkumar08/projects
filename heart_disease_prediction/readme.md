
# Heart Disease Prediction

This project aims to predict the presence of heart disease in patients using various machine learning techniques. The dataset used comes from the Cleveland database available at the UCI Machine Learning Repository and Kaggle.

## Table of Contents
- [Problem Definition](#problem-definition)
- [Data](#data)
- [Evaluation](#evaluation)
- [Features](#features)
- [Machine Learning Techniques](#machine-learning-techniques)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)

## Problem Definition
With the given patients' data, the objective is to predict whether a patient has heart disease.

## Data
The original data is from the Cleveland database available at:
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/45/heart+disease)
- [Kaggle](https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data)

## Evaluation
The project aims to achieve an accuracy of 95% in predicting whether or not a patient has heart disease during the proof of concept.

## Features
The dataset includes the following features:
- `id`: Unique id for each patient
- `age`: Age of the patient in years
- `origin`: Place of study
- `sex`: Male/Female
- `cp`: Chest pain type (typical angina, atypical angina, non-anginal, asymptomatic)
- `trestbps`: Resting blood pressure (in mm Hg on admission to the hospital)
- `chol`: Serum cholesterol in mg/dl
- `fbs`: Fasting blood sugar > 120 mg/dl (True/False)
- `restecg`: Resting electrocardiographic results
- `thalach`: Maximum heart rate achieved
- `exang`: Exercise-induced angina (True/False)
- `oldpeak`: ST depression induced by exercise relative to rest
- `slope`: The slope of the peak exercise ST segment
- `ca`: Number of major vessels (0-3) colored by fluoroscopy
- `thal`: Thalassemia (normal; fixed defect; reversible defect)
- `target`: Presence of heart disease (1 = yes, 0 = no)

## Machine Learning Techniques
The following machine learning techniques are used in this project:
- **Logistic Regression**
- **K-Nearest Neighbors (KNN)**
- **Random Forest Classifier**

## Requirements
To install the necessary libraries, the following packages are required:

```
pandas
numpy
matplotlib
seaborn
sklearn
```

## Installation
To install the necessary libraries, run:
```bash
pip install -r requirements.txt
```

## Usage
1. Clone the repository:
```bash
git clone https://github.com/yourusername/heart-disease-prediction.git
```
2. Navigate to the project directory:
```bash
cd heart-disease-prediction
```
3. Open the Jupyter Notebook:
```bash
jupyter notebook heartdiseaseprediction.ipynb
```

## Results
The results of the model, including accuracy and other performance metrics, will be displayed in the notebook.

## Contributing
Contributions are welcome! Please create a pull request or open an issue to discuss any changes.

---
