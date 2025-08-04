import matplotlib.pyplot as plt

# Data
labels = ['Hotels without promotion', 'Hotels with signboards', 'Hotels with posters']
sizes = [88, 7, 5]
colors = ['#058b83', '#dbe5c4', '#abd7a6']  # Custom color scheme, consistent with the style in the figure

# Generate a pie chart
plt.figure(figsize=(8, 6))
wedges, texts, autotexts = plt.pie(
    sizes,
    labels=labels,
    autopct='%1.0f%%',
    startangle=90,
    colors=colors,
    textprops={'fontsize': 14}
)

# Set the title
plt.title('Proportion of various promotions for \nthe new plastic restriction order in hotels', fontsize=16)

# Display the chart
plt.tight_layout()
plt.show()