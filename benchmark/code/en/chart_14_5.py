import matplotlib.pyplot as plt
import numpy as np

# Date data
dates = ['July 1st', 'July 6th', 'July 11th', 'July 16th', 'July 21st', 'July 26th']
# Search index data
heatstroke_index = [7000, 10000, 10000, 14000, 7000, 42000]
air_condition_illness_index = [3500, 7000, 7000, 10000, 10000, 21000]

# Convert dates to indices for plotting
x = np.arange(len(dates))

# Create a plotting object
fig, ax = plt.subplots(figsize=(12, 7))

# Set a gradient background (from light blue to dark blue)
gradient = np.linspace(0.95, 0.85, 256).reshape(256, 1)
ax.imshow(gradient, aspect='auto', extent=[0, len(dates)-1, 0, max(heatstroke_index)*1.1],
          alpha=0.3, cmap=plt.cm.Blues)

# Plot the optimized line chart
ax.plot(x, heatstroke_index, color='#FF3333', marker='o', markersize=8,
        label='Heatstroke', linewidth=3, alpha=0.8)
ax.plot(x, air_condition_illness_index, color='#FF9933', marker='o', markersize=8,
        label='Air - Condition Illness', linewidth=3, alpha=0.8)

# Set the x - axis and y - axis
ax.set_xticks(x)
ax.set_xticklabels(dates, fontsize=12)
ax.set_ylabel('Search Index', fontsize=14, labelpad=10)
ax.set_ylim(0, max(heatstroke_index) * 1.1)  # Leave some space at the top

# Set the beautified title
ax.set_title('Comparison Trend of Search Index between Air - Condition Illness and Heatstroke',
             fontsize=18, fontweight='bold', pad=20, color='#333333')

# Add data labels
for i, (xi, yi) in enumerate(zip(x, heatstroke_index)):
    ax.annotate(f'{yi}', (xi, yi), textcoords='offset points',
                xytext=(0, 10), ha='center', fontsize=10, fontweight='bold')

for i, (xi, yi) in enumerate(zip(x, air_condition_illness_index)):
    ax.annotate(f'{yi}', (xi, yi), textcoords='offset points',
                xytext=(0, -15), ha='center', fontsize=10, fontweight='bold')

# Add grid lines
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Set the legend and borders
ax.legend(fontsize=12, loc='upper left')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#AAAAAA')
ax.spines['bottom'].set_color('#AAAAAA')

# Adjust the layout
plt.tight_layout()

# Display the chart
plt.show()