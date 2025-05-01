import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/airbnb_nyc.csv")

# Group and count by room_type
room_counts = df['room_type'].value_counts()

# Plot bar chart
plt.figure(figsize=(8, 6))
room_counts.plot(kind='bar', color='mediumseagreen', edgecolor='black')

# Customize plot
plt.title("Number of Listings by Room Type", fontsize=14)
plt.xlabel("Room Type", fontsize=12)
plt.ylabel("Number of Listings", fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y')

# Save to file
plt.tight_layout()
plt.savefig("data/room_type_distribution.png")
plt.show()
