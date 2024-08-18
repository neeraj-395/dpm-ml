"""
Executable code to generate a barplot, counts the number of occurance of each prognosis
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data from the correct file
data = pd.read_csv("dataset/traninig.csv")

# Count the occurrences of each unique 'prognosis'
prognosis_counts = data['prognosis'].value_counts().reset_index()
prognosis_counts.columns = ['Prognosis', 'Count']

# Create the bar plot with clean and neat aesthetics
plt.figure(figsize=(12, 6))  # Adjusting figure size for better spacing
sns.barplot(
    data=prognosis_counts,
    x='Prognosis',
    y='Count',
    palette='viridis',  
    linewidth=0,      
    edgecolor=None    
)

plt.title('Count of Each Prognosis', fontsize=16)
plt.xlabel('Prognosis', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.xticks(rotation=90, fontsize=8)  # Rotate x-axis labels for better readability

# Remove the top and right spines for a cleaner look
sns.despine()

plt.tight_layout()  # Adjust layout to make sure everything fits well
plt.show()