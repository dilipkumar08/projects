# Laptop Price Prediction

This repository contains a simple machine learning project for predicting laptop prices based on various features. The goal of this project is to showcase progress in using machine learning techniques, rather than achieving high prediction accuracy.

## Project Description

The project involves data preprocessing, feature engineering, and model training using a RandomForestRegressor. The steps include handling missing values, encoding categorical variables, and tuning the model using GridSearchCV.

## Data

The dataset `data.csv` contains the following columns:

- `brand`: Brand of the laptop
- `spec_rating`: Specification rating of the laptop
- `Ram`: RAM size of the laptop
- `Ram_type`: Type of RAM
- `ROM`: Storage size of the laptop
- `ROM_type`: Type of storage (HDD, SSD, etc.)
- `display_size`: Size of the display
- `OS`: Operating System
- `warranty`: Warranty period
- `processor`: Processor details
- `price`: Price of the laptop (target variable)

## Steps

1. **Data Loading and Preprocessing**
   - Load the dataset.
   - Handle missing values.
   - Extract and convert units of RAM and ROM.
   - Encode categorical variables.

2. **Model Training and Evaluation**
   - Split the data into training and testing sets.
   - Train a RandomForestRegressor model.
   - Evaluate the model using Mean Absolute Error (MAE) and Mean Squared Error (MSE).

3. **Hyperparameter Tuning**
   - Use GridSearchCV for hyperparameter tuning.
   - Evaluate the tuned model.

## Requirements

To run the project, you need to install the following Python libraries:

```bash
pip install -r requirements.txt


### requirements.txt

```plaintext
pandas
numpy
scikit-learn

