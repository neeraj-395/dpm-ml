"""
Script code to generate a barplot, counts the number of 
occurance of each prognosis.
"""

import yaml
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data from the correct file
with open('config.yaml', encoding='utf-8') as file:
    config = yaml.safe_load(file)

data = pd.read_csv(config['rawdata']['training'])

# Count the occurrences of each unique 'prognosis'
prognosis_counts = data['prognosis'].value_counts().reset_index()
prognosis_counts.columns = ['Prognosis', 'Count']

# Adjusting figure size for better spacing
plt.figure(figsize=(10, 5))

sns.barplot(data=prognosis_counts, x='Prognosis', y='Count', palette='viridis',
            linewidth=0, hue='Prognosis', legend=False, edgecolor=None)

plt.xlabel('Prognosis', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(rotation=90, fontsize=10)  # Rotate x-axis labels for better readability

# Remove the top and right spines for a cleaner look
sns.despine()

# Adjust layout to make sure everything fits well
plt.tight_layout()
plt.show()
