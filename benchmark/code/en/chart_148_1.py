import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

# --------------------- Data Preparation ---------------------
# Gender distribution
gender_labels = ["Female", "Male"]
gender_sizes = [60, 40]
gender_colors = ["pink", "lightblue"]

# Age distribution
age_labels = ["21 and under", "22 - 30", "31 - 40", "41 - 50", "51 - 59", "60 and above"]
age_sizes = [4.0, 35.5, 46.6, 10.9, 2.4, 0.6]
age_colors = ["coral", "gold", "green", "brown", "gray", "olive"]

# Monthly income distribution
income_labels = ["5000 and below", "5001 - 10000", "10001 - 15000", "15001 - 20000", 
                 "20001 - 25000", "25001 - 30000", "Above 30000"]
income_sizes = [20.0, 37.2, 26.5, 10.2, 2.9, 1.3, 1.9]
income_colors = ["sienna", "orange", "darkorange", "coral", "lightcoral", "pink", "palevioletred"]

# --------------------- Create the canvas ---------------------
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 6))

# --------------------- Draw the gender distribution (in block form) ---------------------
ax1.set_xlim(0, 100)
ax1.set_ylim(0, 20)
ax1.axis('off')  # Hide the axes

# Draw female blocks
female_blocks = int(gender_sizes[0] / 2)  # Each block represents 2%
for i in range(female_blocks):
    ax1.add_patch(Rectangle((i * 2, 5), 2, 10, color=gender_colors[0]))

# Draw male blocks
male_blocks = int(gender_sizes[1] / 2)
for i in range(male_blocks):
    ax1.add_patch(Rectangle((i * 2, 5), 2, 10, color=gender_colors[1], alpha=0.8))

# Add gender labels and percentages
ax1.text(10, 2, f"{gender_labels[0]}: {gender_sizes[0]}%", fontsize=12, ha='center')
ax1.text(10 + gender_sizes[0], 2, f"{gender_labels[1]}: {gender_sizes[1]}%", fontsize=12, ha='center')

ax1.set_title('Gender Distribution', fontsize=14)

# --------------------- Draw the age distribution pie chart ---------------------
wedges, texts, autotexts = ax2.pie(age_sizes, colors=age_colors, autopct='%1.1f%%', startangle=90)
ax2.set_title('Age Distribution', fontsize=14)
ax2.legend(wedges, age_labels, title="Age Range", loc="center left", bbox_to_anchor=(1, 0.5))

# Adjust the color of annotation text
for autotext in autotexts:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

# --------------------- Draw the monthly income distribution pie chart ---------------------
wedges, texts, autotexts = ax3.pie(income_sizes, colors=income_colors, autopct='%1.1f%%', startangle=90)
ax3.set_title('Monthly Income Distribution', fontsize=14)
ax3.legend(wedges, income_labels, title="Income Range", loc="center left", bbox_to_anchor=(1, 0.5))

# Adjust the color of annotation text
for autotext in autotexts:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

plt.suptitle('Portrait of Chinese Sugar - free Beverage Consumers: Gender/Age/Income', fontsize=16, y=1.03)
plt.tight_layout()
plt.show()