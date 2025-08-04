import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# -------------------- Pie chart data for gender proportion --------------------
gender_data = {
    "Gender": ["Female", "Male"],
    "Proportion": [61, 39]
}
gender_df = pd.DataFrame(gender_data)

# -------------------- Bar chart data for age distribution --------------------
age_data = {
    "Age Group": ["16 - 23 years old", "24 - 30 years old", "31 - 35 years old", "36 - 40 years old", "41 - 45 years old", "46 - 50 years old", "Over 50 years old"],
    "Proportion": [15, 22, 21, 14, 9, 8, 9]
}
age_df = pd.DataFrame(age_data)

# Create a canvas with 2 sub - plots (1 row, 2 columns)
fig, axes = plt.subplots(1, 2, figsize=(14, 5))  # 增加画布宽度，为倾斜标签预留空间

# -------------------- Draw a pie chart for gender proportion --------------------
axes[0].pie(
    gender_df["Proportion"],
    labels=gender_df["Gender"],
    autopct="%1.1f%%",  # Display percentage, keep 1 decimal place
    colors=["#ff99cc", "#66b3ff"],  # Customize colors
    startangle=90  # Starting angle of the pie chart
)
axes[0].set_title("Gender Proportion of Douyin E - commerce Autumn and Winter Clothing Customers", fontsize=9, fontweight="bold")

# -------------------- Draw a bar chart for age distribution --------------------
bar_plot = sns.barplot(
    data=age_df,
    x="Age Group",
    y="Proportion",
    color="#c9b69f",  # Customize the color of the bar chart
    ax=axes[1]
)
axes[1].set_title("Age Distribution of Douyin E - commerce Autumn and Winter Clothing Customers", fontsize=9, fontweight="bold")
axes[1].set_xlabel("Age Group")
axes[1].set_ylabel("Proportion")

# 设置条形图横坐标标签倾斜
axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=30, ha='right', fontsize=10)

# Add numerical labels to the bar chart
for p in bar_plot.patches:
    bar_plot.annotate(
        f'{p.get_height()}%',
        (p.get_x() + p.get_width() / 2., p.get_height()),
        ha='center',
        va='center',
        fontsize=10,
        color='black',
        xytext=(0, 5),
        textcoords='offset points',
    )

# Make the layout more compact (avoid label overlap, etc.)
plt.tight_layout()
# Display the chart
plt.show()