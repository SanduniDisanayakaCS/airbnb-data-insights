import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/airbnb_cleaned.csv")

# Filter for reasonable price range (optional upper cap to visualize better)
df_filtered = df[df['price'] <= 500]

# Calculate IQR for price
Q1 = df_filtered['price'].quantile(0.25)
Q3 = df_filtered['price'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Count potential outliers
outliers = df_filtered[(df_filtered['price'] < lower_bound) | (df_filtered['price'] > upper_bound)]
print(f"🔍 Potential price outliers detected: {len(outliers)}")

# Create boxplot
plt.figure(figsize=(8, 6))
plt.boxplot(df_filtered['price'], vert=False, patch_artist=True,
            boxprops=dict(facecolor='gold', color='black'),
            medianprops=dict(color='red'))

# Customize plot
plt.title("Boxplot of Airbnb Listing Prices (Filtered, <= $500)", fontsize=14)
plt.xlabel("Price (USD)", fontsize=12)
plt.grid(True)

# Save and show plot
plt.tight_layout()
plt.savefig("data/price_boxplot.png")
plt.show()
