import matplotlib.pyplot as plt

# Data
labels = ['Raw Material Related', 'Brand Related', 'Medical Aesthetics Related', 'Others']
sizes = [46.6, 24.7, 16.4, 12.3]

# Softer pastel pink colors
colors = ['#FADADD', '#F9C6D0', '#F7B0C4', '#F59EB7']

# Draw a pie chart
fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    textprops={'fontsize': 12, 'color': 'black'}
)

# Add a title and data source
plt.title('Proportion of Investment Events in Different Fields in 2023', fontsize=14, pad=20)
plt.figtext(0.1, 0.01, '*Data range: Investment and financing events related to the Chinese domestic beauty industry', ha='left', fontsize=10)

# Ensure the pie chart is circular
ax.axis('equal')

plt.tight_layout()
plt.show()