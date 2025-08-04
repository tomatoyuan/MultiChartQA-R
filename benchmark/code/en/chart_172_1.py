import matplotlib.pyplot as plt

# Data definition
labels = ['Prefer low - sugar', 'Prefer sugar - free', 'Not concerned', 'Prefer high - sugar']
sizes = [56, 23, 12, 9]
colors = ['#00a2e8', '#b3ecf7', '#00d2c8', '#4caf50']  # Simulate the color scheme of the original image

# Concatenate labels with percentages
labels_with_pct = [f'{label}, {size}%' for label, size in zip(labels, sizes)]

# Create a pie chart
fig, ax = plt.subplots(figsize=(6, 6))
wedges, texts = ax.pie(sizes, labels=labels_with_pct, colors=colors, startangle=100,
                       labeldistance=0.3, textprops={'fontsize': 11, 'color': 'white'})

# Add a title
plt.title('Chinese consumers\' views on the sugar content of carbonated drinks in 2022', fontsize=14, fontweight='bold', pad=20)

# Force the graph to be circular
ax.axis('equal')

plt.tight_layout()
plt.show()