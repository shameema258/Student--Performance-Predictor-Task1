import pandas as pd

# Create dataset
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Score": [15, 25, 40, 50, 60, 65, 75, 82, 88, 95]
}

df = pd.DataFrame(data)

# Explore data
print("First 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nStatistics:")
print(df.describe())
