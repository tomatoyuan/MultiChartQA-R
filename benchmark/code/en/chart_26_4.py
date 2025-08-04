import matplotlib.pyplot as plt
import numpy as np

# Data
age_groups = ["<19 years old", "19 - 24 years old", "25 - 34 years old", "35 - 49 years old", ">=50 years old"]
male_percents = [13, 37, 41, 8, 1]
female_percents = [20, 47, 27, 5, 1]

x = np.arange(len(age_groups))  # x-axis positions
width = 0.35  # Bar width

# Create a figure and a subplot
fig, ax = plt.subplots(figsize=(8, 6))

# Draw grouped bars for males and females
rects_male = ax.bar(x - width/2, male_percents, width, label="Male group", color="#4CAF50")
rects_female = ax.bar(x + width/2, female_percents, width, label="Female group", color="#F44336")

# Set x-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(age_groups)
# Set y-axis label
ax.set_ylabel("Attention percentage (%)")
# Set the title
ax.set_title('Gender - Age distribution of attention to "Valentine\'s Day gifts"')
# Add a legend
ax.legend()

# Annotate values on the bars
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}%'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # Vertical distance of the value label from the bar
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects_male)
autolabel(rects_female)

# Adjust the layout and display the chart
plt.tight_layout()
plt.show()