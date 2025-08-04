import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Build data
data = {
    "category": ["Female", "Male", "Under 19", "20 - 29", "30 - 39", "40 - 49", "Over 50"],
    "percentage": [33, 67, 11, 26, 29, 23, 11]
}
df = pd.DataFrame(data)

# Classify data into gender and age groups
gender_data = df.iloc[:2]
age_data = df.iloc[2:]

# Create a canvas with two sub - plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
fig.patch.set_facecolor('#f8f9fa')  # Set the canvas background color

# Beautify the bar chart - Gender distribution
sns.barplot(x="category", y="percentage", data=gender_data, palette=["#ff6b6b", "#48dbfb"], ax=ax1)
ax1.set_title("Gender Distribution of UEFA European Championship Followers", fontsize=15, pad=12)
ax1.set_xlabel("Gender", fontsize=12)
ax1.set_ylabel("Percentage (%)", fontsize=12)
ax1.set_ylim(0, 100)  # Set the y - axis range
ax1.grid(axis='y', linestyle='--', alpha=0.7)  # Optimize the grid lines

# Add numerical labels for gender distribution
for p in ax1.patches:
    height = p.get_height()
    ax1.text(p.get_x() + p.get_width() / 2., height + 1.5,
             f'{height:.1f}%', ha="center", fontsize=11)

# Beautify the pie chart - Age distribution
wedges, texts, autotexts = ax2.pie(
    age_data["percentage"],
    labels=age_data["category"],
    autopct='%1.1f%%',
    startangle=90,
    colors=sns.color_palette("pastel"),
    wedgeprops={'edgecolor': 'w', 'linewidth': 1},
    textprops={'fontsize': 10}
)
ax2.set_title("Age Distribution of UEFA European Championship Followers", fontsize=15, pad=12)
ax2.axis('equal')  # Ensure the pie chart is a perfect circle

# Adjust the layout
plt.tight_layout(pad=3)  # Increase the spacing between sub - plots
plt.suptitle("Basic Data Statistics of UEFA European Championship Attention", fontsize=18, y=1.02, fontweight='bold')

# Display the chart
plt.show()