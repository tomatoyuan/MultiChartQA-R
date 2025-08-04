import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ["Engineering", "Science", "Economics", "Education", "Management", "Medicine", "Literature", 
              "History", "Law", "Art", "Agriculture", "Philosophy", "Others"]
proportions = [26.75, 25.81, 23.63, 23.48, 23.32, 19.75, 16.69, 
               15.86, 15.71, 12.59, 11.50, 11.35, 0.31]
# Proportions of liberal arts and science
liberal_arts = 43.5
science = 56.5

fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(16, 8), gridspec_kw={'width_ratios': [1, 3]})

# Left: Proportions of liberal arts and science (text + simple visualization)
ax_left.text(0.5, 0.6, f'Liberal Arts {liberal_arts}%', ha='center', va='center', fontsize=16, color='orange')
ax_left.text(0.5, 0.4, f'Science {science}%', ha='center', va='center', fontsize=16, color='blue')
ax_left.axis('off')

# Right: Horizontal bar chart of preferences for each subject/major
y = np.arange(len(categories))
ax_right.barh(y, proportions, color='orange')
ax_right.set_yticks(y)
ax_right.set_yticklabels(categories)
ax_right.set_xlabel('Proportion (%)')

# Add value labels for each subject/major proportion
for i, prop in enumerate(proportions):
    ax_right.text(prop + 0.5, i, f'{prop}%', va='center')

ax_right.set_title('Preferences of Chinese College Entrance Examination Candidates for Subjects and Majors')

plt.tight_layout()
plt.show()