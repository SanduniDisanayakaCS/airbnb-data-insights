import pandas as pd

# Load dataset
df = pd.read_csv("data/airbnb_nyc.csv")

# Show total missing values per column
print("🔍 Missing Values Before Cleaning:\n")
print(df.isnull().sum(), "\n")

# Fill missing reviews_per_month with 0 (reasonable default)
df['reviews_per_month'] = df['reviews_per_month'].fillna(0)

# Fill missing last_review with 'No review'
df['last_review'] = df['last_review'].fillna("No review")

# Optional: Remove rows with missing host_name (if any)
df = df.dropna(subset=['host_name'])

df['host_id'] = df['host_id'].astype(str)

# 🔄 Convert all columns to string
df = df.astype(str)

# Show updated missing value status
print("✅ Missing Values After Cleaning:\n")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("data/airbnb_cleaned.csv", index=False)
print("\n🧼 Cleaned dataset saved as 'data/airbnb_cleaned.csv'")
