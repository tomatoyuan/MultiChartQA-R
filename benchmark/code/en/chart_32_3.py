import matplotlib.pyplot as plt
import numpy as np

# Age groups
age_groups = ['≤18 years old', '19 - 24 years old', '25 - 34 years old', '35 - 49 years old', '≥50 years old']
# Female percentage data (simulated, supplemented reasonably based on the chart trend and known data)
female_percents = [60, 71, 57, 55, 52]
# Male percentage data (simulated, supplemented reasonably based on the chart trend and known data)
male_percents = [40, 29, 43, 45, 48]

x = np.arange(len(age_groups))  # x-axis positions
width = 0.35  # Bar width

fig, ax = plt.subplots()
# Draw female bars
rects1 = ax.bar(x - width/2, female_percents, width, label='Female', color='pink')
# Draw male bars
rects2 = ax.bar(x + width/2, male_percents, width, label='Male', color='blue')

# Add title and labels
ax.set_ylabel('Percentage (%)')
ax.set_title('Male and female percentages of searching for "Teacher Qualification Certificate" in different age groups')
ax.set_xticks(x)
ax.set_xticklabels(age_groups, rotation=45, ha='right')
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

autolabel(rects1)
autolabel(rects2)

plt.show()