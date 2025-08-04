import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['Before "Double Reduction"', 'After "Double Reduction"']
tutoring = [56, 18]  # Proportion of parents sending their children to tutoring classes
home_edu = [68, 77]  # Proportion of time spent on family education

x = np.arange(len(labels))
width = 0.35

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Figure 1: Proportion of parents sending their children to tutoring classes
ax1.bar(x, tutoring, color='orange')
ax1.set_title('Proportion of parents sending their children to tutoring classes\n before and after "Double Reduction"')
ax1.set_xticks(x)
ax1.set_xticklabels(labels)
ax1.set_ylim(0, 100)
for i, v in enumerate(tutoring):
    ax1.text(i, v + 2, f'{v}%', ha='center', fontsize=10)

# Figure 2: Proportion of time spent on family education
ax2.bar(x, home_edu, color='red')
ax2.set_title('Change in the proportion of time spent on family education \n'
              'before and after "Double Reduction"')
ax2.set_xticks(x)
ax2.set_xticklabels(labels)
ax2.set_ylim(0, 100)
for i, v in enumerate(home_edu):
    ax2.text(i, v + 2, f'{v}%', ha='center', fontsize=10)

plt.suptitle('Data source: Ministry of Education of the People\'s Republic of China, "Research on the Impact of the "Double Reduction" Policy on Family Education"', fontsize=10, y=0)
plt.tight_layout()
plt.show()