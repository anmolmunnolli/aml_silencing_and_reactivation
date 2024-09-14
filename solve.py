import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv', index_col=0)

# Plot the color map
plt.figure(figsize=(8, 6))
sns.heatmap(df, annot=True, fmt='.2f', linewidths=.5)

# Set labels and title
plt.title('Mean Classification Accuracy Heatmap')
plt.xlabel('Columns')
plt.ylabel('Rows')

# Show the plot
plt.show()
