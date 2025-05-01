import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/airbnb_nyc.csv")

# 1. Basic Overview
print("✅ Dataset Loaded Successfully!\n")
print("🔸 Shape of dataset:", df.shape)
print("🔸 Column names:\n", df.columns.tolist(), "\n")

# 2. Column data types
print("🔸 Column Data Types:\n", df.dtypes, "\n")

# 3. Show first 5 rows
print("🔸 First 5 Rows:\n", df.head(), "\n")

# 4. Count missing values
missing = df.isnull().sum()
print("🔸 Missing Values per Column:\n", missing[missing > 0], "\n")

# 5. Basic statistics (numerical)
print("🔸 Descriptive Statistics (Numerical):\n", df.describe(), "\n")

# 6. Save a sample preview to CSV (optional for Power BI)
df.head(100).to_csv("data/sample_airbnb_preview.csv", index=False)
print("✅ Sample preview saved to data/sample_airbnb_preview.csv")
