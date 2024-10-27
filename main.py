import pandas as pd
from sklearn.model_selection import train_test_split
from model_inference import classify_threat
from feature_engineering import preprocess_data
from model_training import train_model
from evaluate_model import evaluate_model

# Load your dataset
data = pd.read_csv('data.csv')  # Replace 'data.csv' with your actual data file

# Preprocess the data
processed_data = preprocess_data(data)

# Split the dataset
X = processed_data.drop(columns=['target'])
y = processed_data['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model with optimized hyperparameters
model = train_model(X_train, y_train)

# Evaluate model to check false positives
evaluate_model(model, X_test, y_test)

# Example inference
example_probability = model.predict_proba(X_test)[:, 1]
predictions = [classify_threat(prob) for prob in example_probability]

print("Predictions for the test set:", predictions)
