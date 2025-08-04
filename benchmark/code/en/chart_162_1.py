import matplotlib.pyplot as plt

# Data
categories = ['Local Standards', 'Group Standards', 'Enterprise Standards']
values = [27, 289, 90]

# Plotting
fig, ax = plt.subplots(figsize=(6, 6))
bars = ax.bar(categories, values, color='red')

# Add numerical labels
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 5, f'{int(yval)}',
            ha='center', va='bottom', fontsize=12)

# Add title and labels
ax.set_title('Distribution of Current Pre - made Cuisine - related Standards in China in 2024', fontsize=14)
ax.set_ylabel('Unit: Items', fontsize=12)
ax.set_ylim(0, 320)

plt.tight_layout()
plt.show()