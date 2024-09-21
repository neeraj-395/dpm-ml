"""
Decision Tree Model Training Script

This script trains a Decision Tree Classifier on a dataset of symptoms and diseases,
evaluates its performance, and saves the trained model to a specified file path.
"""

import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from src.utils.preprocess import data_proprocessor

# Load and prepocess the dataset
X_train, y_train, diseases, symptoms  = data_proprocessor('data/training.csv')

# Split the dataset into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

# Initialize the model
clf = DecisionTreeClassifier(random_state=42) # Set a random state for reproduciblity

# Fit the model
clf = clf.fit(X_train, y_train)

# Evaluate the model
y_pred = clf.predict(X_val)
accuracy = accuracy_score(y_val, y_pred)
print(f"Validation Accuracy(%): {accuracy}")

joblib.dump(clf,'models/decision_tree_model.pkl')
print("Decision tree model is saved to /models directory.")
