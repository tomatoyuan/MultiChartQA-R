import matplotlib.pyplot as plt
import numpy as np

# Data organization (in order of metrics and satisfaction levels: Very Satisfied, Fairly Satisfied, Average, Fairly Dissatisfied, Very Dissatisfied)
metrics = [
    "Service Convenience", "Cleanliness", "Service Experience", 
    "Consistency with Promotional Information", "Price Reasonableness", "Safety", "Promotional Activities"
]
# Proportion (%) of each satisfaction level under each metric
data = np.array([
    [57, 34, 7, 2, 0],   # Service Convenience
    [50, 41, 7, 2, 0],   # Cleanliness
    [50, 40, 10, 0, 0],  # Service Experience
    [49, 40, 8, 3, 0],   # Consistency with Promotional Information
    [44, 44, 10, 4, 0],  # Price Reasonableness
    [51, 37, 10, 3, 0],  # Safety
    [49, 38, 11, 2, 0]   # Promotional Activities
])
# Color scheme for each satisfaction level (similar to the original figure)
colors = ["#f8cecc", "#f4a460", "#ff8c00", "#cd5c5c", "#8b0000"]
# Labels for satisfaction levels
labels = ["Very Satisfied", "Fairly Satisfied", "Average", "Fairly Dissatisfied", "Very Dissatisfied"]

x = np.arange(len(metrics))  # x-axis coordinates (one position for each metric)
bar_width = 0.8  # Width of the bars to make the segments more compact

fig, ax = plt.subplots(figsize=(12, 8))

# Draw the segmented stacked bar chart
bottom = np.zeros(len(metrics))  # Starting position for stacking
for i in range(5):
    ax.bar(
        x, 
        data[:, i], 
        width=bar_width, 
        color=colors[i], 
        bottom=bottom, 
        label=labels[i] if i == 0 else ""  # Only show the legend for the first level to avoid repetition
    )
    bottom += data[:, i]  # Update the starting position for the next segment

ax.set_title('2023 Survey on the Satisfaction of Chinese Local Service Users\' In - Store Service Experience', fontsize=14)
ax.set_ylabel('Proportion (%)')
ax.set_xticks(x)
ax.set_xticklabels(metrics, rotation=45, ha='right')
ax.legend(title='Satisfaction Level', loc='upper right')

# Add numerical annotations (only annotate "Very Satisfied" and "Fairly Satisfied" as the original figure only shows these two parts; can expand the loop if all need to be annotated)
for i in range(len(metrics)):
    # Annotate the value of "Very Satisfied"
    ax.text(x[i], data[i, 0]/2, f'{data[i, 0]}%', ha='center', va='center', color='black')
    # Annotate the value of "Fairly Satisfied"
    ax.text(x[i], data[i, 0] + data[i, 1]/2, f'{data[i, 1]}%', ha='center', va='center', color='black')
    # If you need to annotate "Average", "Fairly Dissatisfied", "Very Dissatisfied", you can continue to add:
    # ax.text(x[i], data[i, 0]+data[i, 1]+data[i, 2]/2, f'{data[i, 2]}%', ...) 

plt.tight_layout()
plt.show()