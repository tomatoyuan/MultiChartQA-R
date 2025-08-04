import matplotlib.pyplot as plt
import numpy as np

# AI glasses brands
brands = ["Huawei", "Xiaomi", "Google", "Rokid", "Meta", "Xingzhe Wujiang", "LeiShen Technology", "Yiwen Technology", "Star Meizu", "Baidu"]
# Corresponding brand percentages (%), the data is roughly simulated and can be adjusted according to actual situation
percentages = [23.8, 17.3, 15.3, 7.7, 6.5, 5.8, 4.0, 3.0, 2.9, 2.2]

x = np.arange(len(brands))  # x-axis tick positions

fig, ax = plt.subplots()

# Draw a bar chart with a similar green color
bars = ax.bar(x, percentages, color='greenyellow')

# Add a title
ax.set_title('AI Glasses Brands Heard of by Overall Respondents (TOP10)')

# Set x-axis tick labels
ax.set_xticks(x)
ax.set_xticklabels(brands, rotation=45, ha='right')  # Rotate the labels to avoid overlap

# Add numerical labels to each bar
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Vertical offset of 3 points
                textcoords="offset points",
                ha='center', va='bottom')

# Set the y-axis label (can be added as needed)
ax.set_ylabel('Brand Percentage (%)')

plt.tight_layout()  # Automatically adjust the layout to avoid label overlap
plt.show()