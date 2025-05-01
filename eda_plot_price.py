import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/airbnb_nyc.csv")

# Filter to remove extreme prices (outliers)
df_filtered = df[df['price'] <= 500]

# Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(df_filtered['price'], bins=50, color='skyblue', edgecolor='black')

# Add labels and title
plt.title("Distribution of Airbnb Listing Prices (Filtered, <= $500)", fontsize=14)
plt.xlabel("Price (USD)", fontsize=12)
plt.ylabel("Number of Listings", fontsize=12)
plt.grid(True)

# Save the plot to file
plt.savefig("data/price_distribution.png")
plt.show()
