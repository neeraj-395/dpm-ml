"""
Model Traning Script for Disease Prediction

This script is responsible for training two machine learning models, 
namely Decision Tree and Random Forest, on a preprocessed dataset for 
disease prediction. It evaluates both models on a validation set and 
optionally saves the trained models as `.pkl` files for later use.
"""

import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from src.models.preprocess import data_preprocessor

def __evaluate_model(y_true, y_pred):
    """
    Evaluates a model using accuracy metrics and prints the normalized and 
    count accuracy.
    """
    norm_accuracy = accuracy_score(y_true, y_pred)
    count_accuracy = accuracy_score(y_true, y_pred, normalize=False)
    print(f":: Validation Score (normalized): {norm_accuracy}")
    print(f":: Validation Score (count): {count_accuracy}")


def train_models(data_path: str, dump_model: bool = True) -> bool:
    """
    Trains Decision Tree and Random Forest models on the given dataset, 
    evaluates them on a validation set, and optionally saves the trained models.
    """
    try:
        # Load and preprocess the dataset
        x_train, y_train = data_preprocessor(data_path)

        # Split the dataset into training and validation sets
        x_train, x_val, y_train, y_val = train_test_split(
            x_train, y_train, test_size=0.2, random_state=42
        )

        # Initialize the models
        dtc = DecisionTreeClassifier(random_state=42)
        rfc = RandomForestClassifier(random_state=42)

        # Fit the models
        dtc.fit(x_train, y_train)
        rfc.fit(x_train, y_train)

        # Evaluate the models
        print("\n:: Decision Tree Model ::")
        y_pred = dtc.predict(x_val)
        __evaluate_model(y_val, y_pred)

        print("\n:: Random Forest Model ::")
        y_pred = rfc.predict(x_val)
        __evaluate_model(y_val, y_pred)

        # Save the models to disk if required
        if dump_model:
            joblib.dump(dtc, 'models/decision_tree_model.pkl')
            print('\n:: Decision tree model saved to /models directory.')
            joblib.dump(rfc, 'models/random_forest_model.pkl')
            print(':: Random forest model saved to /models directory.')

        return True

    except (FileNotFoundError, ValueError) as e:
        print("(train_models)", e)
        return False

if __name__ == "__main__":
    train_models('data/training.csv', dump_model=False)
