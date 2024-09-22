"""
Random Forest Model Training Script

This script trains a Random Forest Classifier on a dataset of symptoms and prognosis,
evaluates its performance, and saves the trained model to a specified file path.
"""
    
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from src.utils.preprocess import data_preprocessor

def train_random_forest_model(file_path : str, dump_model : bool = True) -> bool:
    try:
        x_train, y_train = data_preprocessor(file_path)

        (x_train, x_val,y_train, y_val) = train_test_split(
            x_train, y_train,random_state=42,test_size=0.2
        )

        clf2 = RandomForestClassifier(random_state=42)

        clf2 = clf2.fit(x_train, y_train)

        y_pred = clf2.predict(x_val)
        norml_accuracy = accuracy_score(y_val, y_pred)
        count_accuracy = accuracy_score(y_val, y_pred, normalize=False)
        print(f"Validated Score (normalized): {norml_accuracy}")
        print(f"Validated Score (count): {count_accuracy}")

        if dump_model is True:
           joblib.dump(clf2,'models/random_forest_model.pkl')
           print("Random forest model is saved to /models directory.")
    
        return True

    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        return False 

if __name__ == "__main__":
    train_random_forest_model('data/training.csv', dump_model=False)