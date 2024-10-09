"""
Script code to generate a heatmap visualizing the relationship 
between symptoms and prognosis from a dataset.
"""

import yaml
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Constants for the number of symptoms and prognosis to display
NUM_SYMPTOMS = 20
NUM_PROGNOSIS = 20

# Load the data from the correct file
with open('config.yaml', encoding='utf-8') as file:
    config = yaml.safe_load(file)

data = pd.read_csv(config['rawdata']['testing'])

# Extract the first 'n' prognosis labels
prognosis = data.pop('prognosis').head(NUM_PROGNOSIS)

# Define the color map for the heatmap: light green for '0' and red for '1'
cmap = sns.color_palette(['lightgreen', 'red'])

# Generate the heatmap for the selected number of symptoms and prognosis
sns.heatmap(data.iloc[:NUM_SYMPTOMS, :NUM_PROGNOSIS], cbar=False, linewidths=0.5,
            cmap=cmap, linecolor='black', yticklabels=prognosis) # type: ignore

# Set the axis labels
plt.xlabel('Symptoms')
plt.ylabel('Prognosis')
plt.yticks(fontsize=8)
plt.xticks(fontsize=8)

# Adjust the layout to ensure proper spacing and prevent overlap
plt.tight_layout()
plt.show()
