import matplotlib.pyplot as plt
import numpy as np

# Viewing time periods
time_periods = ["Weekends and holidays", "When idle and bored", "During usual fragmented time", "Before going to sleep", "When insomniac or under stress", "During meals"]
# Corresponding proportions (%)
proportions = [41.73, 41.36, 37.65, 31.36, 30.74, 26.67]

x = np.arange(len(time_periods))  # x-axis coordinates

fig, ax = plt.subplots(figsize=(8, 6))
# Draw a bar chart
bars = ax.bar(x, proportions, color='orange')

# Add numerical labels
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# Set x-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(time_periods, rotation=20, ha='right')
ax.set_ylabel('Proportion (%)')
ax.set_title('Viewing time periods of Chinese TV drama viewers in 2025')

plt.tight_layout()
plt.show()