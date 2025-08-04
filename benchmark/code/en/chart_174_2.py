import matplotlib.pyplot as plt

# Data
labels = ['No need to replace daily', 'Need to replace daily']
sizes = [62.6, 37.4]
colors = ['#058b83', '#abd7a6']  # Use the same color scheme as the chart

# Generate a pie chart
plt.figure(figsize=(8, 6))
wedges, texts, autotexts = plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    textprops={'fontsize': 14}
)

# Set the title
plt.title('Proportion of people who do not need to replace\n disposable items daily for multi - person occupancy', fontsize=16)

# Display the chart
plt.tight_layout()
plt.show()