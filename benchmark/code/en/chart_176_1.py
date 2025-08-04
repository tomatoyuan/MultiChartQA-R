import matplotlib.pyplot as plt

# Data
labels = ['For lovers', 'For kids', 'For friends', 'For elders', 'For oneself']
sizes = [60, 14, 10, 8, 8]

# Pie chart colors can be customized or use the default
colors = ['#FF5A7D', '#FF8DA1', '#FFA7B5', '#FFC3CB', '#FFE1E7']

# Draw a pie chart
fig, ax = plt.subplots()
ax.pie(
    sizes,
    labels=labels,
    autopct='%1.0f%%',
    startangle=90,
    colors=colors,
    textprops={'fontsize': 12}
)

# Keep it circular
ax.axis('equal')
plt.title('Distribution of Valentine\'s Day gift recipients in 2023\n(Proportion of transaction UV of gift recipients among gift - giving people)', fontsize=14, pad=20)
plt.tight_layout()
plt.show()