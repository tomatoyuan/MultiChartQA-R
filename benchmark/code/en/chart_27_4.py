import matplotlib.pyplot as plt
import numpy as np

# TV drama names
labels = ["In the Name of People", "I Rule the沉浮 (This can be translated based on its specific context, here we just keep the Chinese part for lack of better info)", "National Cadre", "National Prosecution", "Absolute Power"]
# Male percentage
male_percents = [64, 70, 70, 74, 75]
# Female percentage
female_percents = [36, 30, 30, 26, 25]

x = np.arange(len(labels))  # x-axis positions
width = 0.35  # Bar width

fig, ax = plt.subplots(figsize=(8, 5))
# Draw male percentage bars
rects_male = ax.barh(x - width/2, male_percents, width, label='Male', color='#8B4513')
# Draw female percentage bars
rects_female = ax.barh(x + width/2, female_percents, width, label='Female', color='red')

# Add labels and title
ax.set_yticks(x)
ax.set_yticklabels(labels)
ax.set_xlabel('Percentage (%)')
ax.set_title('Gender Analysis of Popular TV Drama Viewers')
ax.legend()

# Add value labels to bars
def label_bars(rects):
    for rect in rects:
        length = rect.get_width()
        ax.text(length + 1, rect.get_y() + rect.get_height()/2,
                f'{length}%', va='center')

label_bars(rects_male)
label_bars(rects_female)

plt.tight_layout()
plt.show()