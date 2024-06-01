
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor

# Load the dataset
carsales = pd.read_csv('car-sales-extended-missing-data.csv')

# Drop rows with missing target values
carsales.dropna(subset=['Price'], inplace=True)

# Define features
categorical_feature = ['Make', 'Colour']
door_feature = ['Doors']
numeric_feature = ['Odometer (KM)']

# Preprocessing pipelines for each feature type
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

door_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value=4))
])

numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean'))
])

# Combine preprocessing steps
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', categorical_transformer, categorical_feature),
        ('door', door_transformer, door_feature),
        ('num', numeric_transformer, numeric_feature)
    ])

# Define the model pipeline
model = Pipeline(steps=[
    ('preprocess', preprocessor),
    ('model', RandomForestRegressor(n_estimators=250))
])

# Split the data into training and testing sets
X = carsales.drop('Price', axis=1)
y = carsales['Price']
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit the model
model.fit(x_train, y_train)

# Evaluate the model
print("Initial Model Score:", model.score(x_test, y_test))

# Define parameter grid for GridSearchCV
pipe_grid = {
    'preprocess__num__imputer__strategy': ['mean', 'median'],
    'model__n_estimators': [100, 200, 1000],
    'model__max_depth': [None, 5],
    'model__max_features': ['sqrt', None],
    'model__min_samples_split': [2, 4]
}

# Set up GridSearchCV
gs_model = GridSearchCV(model, param_grid=pipe_grid, cv=5, verbose=2, n_jobs=-1)

# Fit the GridSearchCV model
gs_model.fit(x_train, y_train)

# Print the best parameters and best score
print(f"Best parameters found: {gs_model.best_params_}")
print(f"Best cross-validation score: {gs_model.best_score_}")

# Evaluate the best model on the test set
print("Test set score of the best model:", gs_model.score(x_test, y_test))
