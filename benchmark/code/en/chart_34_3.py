import matplotlib.pyplot as plt
import numpy as np

# Functional enhancement items
features = ["Enhance comfort", "Improve health", "Sports professional functionality"]
# Corresponding percentage data
percentages = [71, 57, 55]
# Used to display TOP information on the chart, set according to the index here
tops = ["TOP1", "TOP2", "TOP3"]

# Set the font to ensure normal display of English (no need to adjust for English)
plt.rcParams['axes.unicode_minus'] = False  # Solve the problem of the minus sign being displayed as a square

y_pos = np.arange(len(features))  # y-axis position

# Create a horizontal bar chart
fig, ax = plt.subplots()
bars = ax.barh(y_pos, percentages, align='center', color=['#1f77b4', '#ff7f0e', '#2ca02c'])  # Set colors, try to be close to the example style

# Add percentage values to the end of each bar
for bar, percentage in zip(bars, percentages):
    length = bar.get_width()
    ax.text(length + 1,  # x-coordinate of the numerical display position, can be fine-tuned
            bar.get_y() + bar.get_height() / 2,  # y-coordinate of the numerical display position, centered
            f'{percentage}%',
            va='center')

# Add TOP information to the right of each bar
for i, (bar, top) in enumerate(zip(bars, tops)):
    length = bar.get_width()
    ax.text(length + 6,  # Can be fine-tuned according to the actual situation
            bar.get_y() + bar.get_height() / 2,
            top,
            va='center')

ax.set_yticks(y_pos)
ax.set_yticklabels(features)
ax.invert_yaxis()  # Display the first functional item at the top
ax.set_xlabel('Percentage (%)')
ax.set_title('Functional enhancements consumers hope underwear can achieve')

plt.show()