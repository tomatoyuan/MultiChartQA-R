import matplotlib.pyplot as plt

# Data
labels = ['Medical Services Market', 'Pharmaceutical Market', 'Non - Pharmaceutical Products Market', 'Consumer Medical Services Market', 'Medical Infrastructure']
sizes = [53.9, 19.6, 13.7, 9.8, 2.9]
colors = ['#a6d854', '#d9ef8b', '#ffffbf', '#fee08b', '#f46d43']

fig, ax = plt.subplots(figsize=(8, 6))

# Pie chart drawing
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct='%.2f%%',
    startangle=90,
    textprops={'fontsize': 10},
    wedgeprops={'edgecolor': 'white'}
)

# Title
ax.set_title('Market Share Distribution of China\'s Big Health Industry Segments in 2022', fontsize=14, weight='bold')

# Set equal aspect ratio to make the pie circular
ax.axis('equal')

plt.tight_layout()
plt.show()