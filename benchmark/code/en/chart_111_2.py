import matplotlib.pyplot as plt
import numpy as np

# Reasons for choosing double - speed playback
reasons = ["Poor video quality", "Used to double - speed playback and feel more comfortable", "The actor's speaking speed is too slow, affecting the viewing rhythm", 
           "Some content is uninteresting or拖沓 (Here we can change '拖沓' to 'long - winded' in English) Some content is uninteresting or long - winded, don't want to watch closely", "Save time and quickly understand the plot"]
# Corresponding proportions (%)
proportions = [29.33, 41.71, 45.71, 46.29, 50.10]

y = np.arange(len(reasons))  # y-axis coordinates

fig, ax = plt.subplots(figsize=(10, 6))
# Draw a horizontal bar chart
bars = ax.barh(y, proportions, color='orange')

# Add numerical annotations
for i, proportion in enumerate(proportions):
    ax.text(proportion, i, f'{proportion}', va='center', ha='left', fontsize=9)

# Set y-axis ticks and labels
ax.set_yticks(y)
ax.set_yticklabels(reasons)
ax.set_xlabel('Proportion (%)')
ax.set_title('Reasons for Chinese TV drama viewers to choose double - speed playback in 2025')

plt.tight_layout()
plt.show()