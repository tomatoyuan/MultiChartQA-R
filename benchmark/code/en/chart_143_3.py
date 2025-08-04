import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data preparation
data = {
    "Brand Type": ["Domestic Traditional Brands", "Domestic New Brands", "International Well - known Brands", "Foreign Niche Brands"],
    "Decrease": [24.0, 21.0, 30.3, 31.4],
    "No Significant Change": [49.1, 52.1, 48.6, 54.7],
    "Increase": [26.9, 26.9, 21.1, 13.9]
}
df = pd.DataFrame(data).set_index("Brand Type")

# Create a heatmap (with numerical annotations)
plt.figure(figsize=(8, 6))
sns.heatmap(df, annot=True, fmt=".1f", cmap="Oranges", 
            cbar=False, annot_kws={"size": 10, "color": "black"})

# Adjust axis labels and title
plt.yticks(rotation=0)  # Display y - axis labels horizontally
plt.xlabel("Change in Purchase Frequency")
plt.ylabel("Brand Type")
plt.title("Survey on the Changes in Purchase Frequency of Cosmetics Brands in China in 2023", y=1.03, fontsize=12, fontweight="bold")
# Add English subtitle
plt.suptitle("Survey on the Changes in Purchase Frequency of Cosmetics Brands in China in 2023", 
             y=0.93, fontsize=10, color="gray")

# Simulate the dashed boxes in the original figure (manually marked, accurate coordinates can be calculated additionally)
# Mark Domestic Traditional and Domestic New Brands in the "Increase" column
for i in [0, 1]:
    plt.plot([2.2, 2.2], [i + 0.5, i + 1.5], linestyle="--", color="orange", linewidth=2)
    plt.plot([1.8, 2.6], [i + 0.5, i + 0.5], linestyle="--", color="orange", linewidth=2)
    plt.plot([1.8, 2.6], [i + 1.5, i + 1.5], linestyle="--", color="orange", linewidth=2)
# Mark International Well - known and Foreign Niche Brands in the "Decrease" column
for i in [2, 3]:
    plt.plot([0.2, 0.2], [i + 0.5, i + 1.5], linestyle="--", color="orange", linewidth=2)
    plt.plot([-0.2, 0.8], [i + 0.5, i + 0.5], linestyle="--", color="orange", linewidth=2)
    plt.plot([-0.2, 0.8], [i + 1.5, i + 1.5], linestyle="--", color="orange", linewidth=2)

plt.tight_layout()
plt.show()