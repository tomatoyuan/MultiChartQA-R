import matplotlib.pyplot as plt
import numpy as np

# Age situation data
age_categories = ["Under 24", "25 - 34", "35 - 44", "45 and above"]
age_percentages = [29.3, 41.5, 21.6, 7.6]
# Marriage situation data
marriage_categories = ["Unmarried", "Married with children", "Married without children"]
marriage_percentages = [60.7, 34.1, 5.2]
# Free color scheme (adjustable)
bar_color = "#A4C639"  # Bar chart color
pie_colors = ["#A4C639", "#87CEEB", "#FFD700"]  # Pie chart colors

# Create a two - column layout canvas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Draw a horizontal bar chart for age situation
y = np.arange(len(age_categories))
ax1.barh(y, age_percentages, color=bar_color, height=0.6)
ax1.set_yticks(y)
ax1.set_yticklabels(age_categories)
ax1.set_title("Age situation of Chinese football fans in 2022", fontsize=12, fontweight="bold")
# Add age annotations
for i, val in enumerate(age_percentages):
    ax1.annotate(f'{val}%', (val + 1, i), va='center', fontsize=9)

# Draw a pie chart for marriage situation
wedges, texts, autotexts = ax2.pie(
    marriage_percentages,
    labels=marriage_categories,
    colors=pie_colors,
    autopct='%1.1f%%',
    startangle=90
)
ax2.set_title("Marriage situation of Chinese football fans in 2022", fontsize=12, fontweight="bold")
# Beautify pie chart annotations (color, size)
for text, autotext in zip(texts, autotexts):
    text.set_color('black')
    autotext.set_color('black')
    autotext.set_fontsize(9)

# Beautification: Hide borders
for ax in [ax1, ax2]:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

plt.tight_layout()
plt.show()