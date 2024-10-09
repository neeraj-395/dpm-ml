"""
Script code to generate a piechart visualizing the probabilty of 
disease using the disease prediction model.
"""

import sys
import matplotlib.pyplot as plt
from src.models.dp_model import DiseasePredictModel

# Instantiate the model
dpm = DiseasePredictModel()

# Get predicted probabilities
pred_prob = dpm.predict_proba(['itching', 'chills', 'skin_rash'])

# Exit if prediction failed
if pred_prob is None:
    sys.exit(1)

# Set a THRESHOLD for the "Other" category (e.g., 5%)
THRESHOLD = 0.05
prob = list(zip(dpm.diseases, pred_prob))

# Separate large probabilities and small ones (below the THRESHOLD)
large_probs = {disease: p for disease, p in prob if p > THRESHOLD}
small_probs = {disease: p for disease, p in prob if p <= THRESHOLD}

# Combine small probabilities into the "Other" category
if small_probs:
    other_prob = sum(small_probs.values())
    large_probs["Other"] = other_prob  # Add an "Other" category

# Check if there are any probabilities to plot
if large_probs:
    # Create pie chart
    labels = list(large_probs.keys())
    sizes = list(large_probs.values())

    plt.figure(figsize=(8, 8))  # Set figure size
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Predicted Disease Probabilities')
    plt.show()
else:
    print("No diseases with probabilities to display.")
