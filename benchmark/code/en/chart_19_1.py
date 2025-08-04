import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ["Found unnecessary after purchase", "Product does not match description", "Size or model does not match", "Counterfeit or shoddy goods", "Poor customer service attitude", "Poor quality of free gifts", "Difficult after - sales service", "Express delivery delay"]
values = [10, 3, 2, 1, 1, 1, 0.5, 0.3]  # The values are simulated and can be adjusted according to the actual situation

x = np.arange(len(labels))  # x - axis tick positions

# Create a chart
fig, ax = plt.subplots()
rects = ax.bar(x, values, color=['pink', 'pink', 'pink', 'orange', 'orange', 'orange', 'lightblue', 'lightblue'])

# Set x - axis tick labels
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha='right')

# Add a title
ax.set_title('Reasons for regret on Double Eleven', fontsize=14, fontweight='bold')

# Add numerical labels to each bar
for rect in rects:
    height = rect.get_height()
    ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 - pixel offset
                textcoords="offset points",
                ha='center', va='bottom')

# Display the chart
plt.tight_layout()
plt.show()