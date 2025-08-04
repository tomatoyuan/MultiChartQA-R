import matplotlib.pyplot as plt

# Data
labels = ['Accept policy \nmandatory requirements', 'Accept publicity reasons of\n environmental protection values', 'Other']
sizes = [56.3, 37.4, 7.3]
colors = ['#058b83', '#abd7a6', '#efe9d2']  # Match the chart colors

# Generate a pie chart
plt.figure(figsize=(10, 6))
wedges, texts, autotexts = plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    textprops={'fontsize': 14}
)

# Set the title
plt.title('Consumers\' recognized publicity methods', fontsize=16)

# Display the chart
plt.tight_layout()
plt.show()