import matplotlib.pyplot as plt

# Data definition
labels = ['Blood Sugar Control', 'Blood Pressure Regulation', 'Cholesterol Reduction', 'Heart Health', 'Others']
sizes = [25, 25, 25, 17, 8]
colors = ['#00d2c8', '#66cdaa', '#00a2e8', '#3399ff', '#ccecf9']  # According to the illustration color scheme

# Construct label content (with percentages)
labels_with_pct = [f'{label},\n {size}%' for label, size in zip(labels, sizes)]

# Plotting
fig, ax = plt.subplots(figsize=(6, 6))
wedges, texts = ax.pie(sizes, labels=labels_with_pct, colors=colors,
                       startangle=90, labeldistance=0.4,
                       textprops={'fontsize': 11, 'color': 'white'})

# Title
plt.title('Innovative Directions of Raw Materials for Chronic Diseases in 2024', fontsize=14, fontweight='bold', pad=20)

# Keep the graph circular
ax.axis('equal')

plt.tight_layout()
plt.show()