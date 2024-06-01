# Car Sales Price Prediction

This project aims to predict the price of cars using a dataset with various features such as make, color, number of doors, and odometer reading. The project uses a machine learning pipeline with a `RandomForestRegressor` model and employs `GridSearchCV` for hyperparameter tuning.

## Dataset

The dataset `car-sales-extended-missing-data.csv` contains the following features:
- `Make`: The make of the car (e.g., Toyota, Ford)
- `Colour`: The color of the car
- `Doors`: The number of doors on the car
- `Odometer (KM)`: The odometer reading in kilometers
- `Price`: The price of the car (target variable)

## Project Steps

1. **Data Loading**: Load the dataset using `pandas`.
2. **Data Cleaning**: Drop rows with missing target values (`Price`).
3. **Feature Engineering**:
    - Handle missing values for categorical features (`Make`, `Colour`) by filling them with the constant value 'missing' and applying one-hot encoding.
    - Handle missing values for the `Doors` feature by filling them with the constant value 4.
    - Handle missing values for the `Odometer (KM)` feature by imputing with the mean value.
4. **Pipeline Creation**:
    - Create a preprocessing pipeline for the categorical, door, and numerical features.
    - Combine the preprocessing steps with a `RandomForestRegressor` model in a single pipeline.
5. **Model Training**: Split the data into training and testing sets, then fit the model on the training data.
6. **Hyperparameter Tuning**: Use `GridSearchCV` to find the best hyperparameters for the model.
7. **Evaluation**: Evaluate the model on the test set.

## Usage

### Requirements

Install the required packages using `pip`:

```bash
pip install -r requirements.txt
