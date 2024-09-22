"""
Decision Tree Model Training Script

This script trains a Decision Tree Classifier on a dataset of symptoms and diseases,
evaluates its performance, and saves the trained model to a specified file path.
"""

import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from src.utils.preprocess import data_preprocessor

def train_decision_tree_model(data_path: str, dump_model: bool = True) -> bool:
    """
    Train a decision tree model on the given dataset, evaluate its performance, 
    and optionally save the model to a file.

    Parameters
    ----------
    data_path : str
        Path to the CSV file containing the training dataset.
    
    dump_model : bool, optional
        If True, saves the trained decision tree model to the 'models' directory 
        as a .pkl file. Default is True.
    
    Returns
    -------
    bool
        Returns True if the model is successfully trained and saved (if applicable).
        Returns False if an error occurs during the process.
    """

    try:
        # Load and prepocess the dataset
        x_train, y_train = data_preprocessor(data_path)

        # Split the dataset into training and validation sets
        (x_train, x_val,
        y_train, y_val) = train_test_split(
                                x_train, y_train,
                                random_state=42,
                                test_size=0.2
                            )

        # Initialize the model
        clf = DecisionTreeClassifier(random_state=42)

        # Fit the model
        clf = clf.fit(x_train, y_train)

        # Evaluate the model
        y_pred = clf.predict(x_val)
        norm_accuracy = accuracy_score(y_val, y_pred)
        count_accuracy = accuracy_score(y_val, y_pred, normalize=False)
        print(f"Validation Score (normalized): {norm_accuracy}")
        print(f"Validation Score (count): {count_accuracy}")

        if dump_model is True:
            joblib.dump(clf,'models/decision_tree_model.pkl')
            print("Decision tree model is saved to /models directory.")

        return True

    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    train_decision_tree_model('data/training.csv', dump_model=False)
