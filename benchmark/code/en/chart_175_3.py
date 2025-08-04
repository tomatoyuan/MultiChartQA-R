import matplotlib.pyplot as plt
import numpy as np

# Data
labels = [
    "Brand establishment \n"
    "and awareness improvement",
    "Marketing resource acquisition \n"
    "and campaign implementation",
    "Stable capital \n"
    "chain guarantee",
    "Strategy formulation",
    "Sales channel setup \n"
    "and operation",
    "User acquisition and \n"
    "sales conversion",
    "Product innovation and \n"
    "localization"
]
x = np.arange(len(labels))  # x-coordinate positions
width = 0.35  # Bar width

# Data for emerging overseas enterprises and established overseas enterprises
xinrui = [9, 19, 20, 24, 20, 22, 22]
chengshu = [12, 6, 9, 9, 16, 21, 22]

# Plotting
fig, ax = plt.subplots(figsize=(8, 6))
bars1 = ax.barh(x - width/2, xinrui, width, label='Emerging overseas enterprises', color='#0072CE')
bars2 = ax.barh(x + width/2, chengshu, width, label='Established overseas enterprises', color='#7EC0EE')

# Add numerical labels
for bar in bars1 + bars2:
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
            f'{bar.get_width()}%', va='center', fontsize=9)

# Axes and labels
ax.set_yticks(x)
ax.set_yticklabels(labels, fontsize=10)
ax.invert_yaxis()  # Invert the Y-axis
ax.set_xlabel('Percentage (%)')
ax.set_title('Different types of overseas enterprises face different overseas challenges')
ax.legend()

plt.tight_layout()
plt.show()