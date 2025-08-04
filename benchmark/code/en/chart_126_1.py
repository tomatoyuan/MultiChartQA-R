import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Gender distribution data
gender_labels = ["Male", "Female"]
gender_sizes = [32.2, 67.8]
gender_colors = ["#6495ED", "#FFA07A"]

# Age distribution data
age_categories = ["15 - 25 years old", "26 - 29 years old", "31 - 40 years old", "41 - 50 years old", "51 - 55 years old", "56 - 60 years old", "Others"]
age_proportions = [13.8, 34.1, 31.5, 13.1, 5.4, 1.7, 0.4]
age_colors = ["#FFD700", "#FF7F50", "#FF7F50", "#FFD700", "#FFD700", "#FFD700", "#D3D3D3"]

# Marital status data
marital_labels = ["Unmarried", "Married without children", "Married with children"]
marital_sizes = [18.1, 14.4, 67.5]
marital_colors = ["#FFD700", "#32CD32", "#FF7F50"]

# Create a canvas with 3 sub-plots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

# Left: Gender distribution
male_x, male_y = 0.2, 0.5
male_width, male_height = 0.2, 0.4
ax1.add_patch(plt.Rectangle((male_x, male_y - male_height / 2), male_width, male_height, color=gender_colors[0]))
ax1.add_patch(plt.Circle((male_x + male_width / 2, male_y + 0.1), 0.05, color=gender_colors[0]))
ax1.text(male_x + male_width / 2, male_y - 0.3, f'{gender_labels[0]}, {gender_sizes[0]}%', ha='center', va='top')

female_x, female_y = 0.6, 0.5
female_width, female_height = 0.2, 0.4
ax1.add_patch(plt.Rectangle((female_x, female_y - female_height / 2), female_width, female_height, color=gender_colors[1]))
ax1.add_patch(plt.Circle((female_x + female_width / 2, female_y + 0.1), 0.05, color=gender_colors[1]))
ax1.text(female_x + female_width / 2, female_y - 0.3, f'{gender_labels[1]}, {gender_sizes[1]}%', ha='center', va='top')

ax1.axis('off')
ax1.set_title('2024 Gender Distribution of Chinese Consumers')

# Middle: Age distribution bar chart (横坐标倾斜展示)
ax2.bar(age_categories, age_proportions, color=age_colors)
ax2.set_ylabel('Proportion (%)')
ax2.set_title('2024 Age Distribution of Chinese Consumers')
# Add numerical annotations
for i, prop in enumerate(age_proportions):
    ax2.text(i, prop + 1, f'{prop}%', ha='center', va='bottom', fontsize=9)
# 关键修改：设置横坐标倾斜45度并右对齐
ax2.set_xticks(range(len(age_categories)))  # 固定刻度位置
ax2.set_xticklabels(age_categories, rotation=45, ha='right', fontsize=9)  # rotation控制倾斜角度，ha='right'右对齐

# Right: Marital status pie chart (修复解包错误)
wedges, texts, autotexts = ax3.pie(marital_sizes, colors=marital_colors, startangle=90, autopct='%1.1f%%')
ax3.legend(wedges, marital_labels, loc='lower left', fontsize=9)
for autotext in autotexts:
    autotext.set_color('white')
ax3.set_title('2024 Marital Status of Chinese Consumers')

plt.tight_layout()
plt.show()