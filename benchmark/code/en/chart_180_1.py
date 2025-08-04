import matplotlib.pyplot as plt

# Pie chart data
labels = ['Understand the meaning of \nthe Blue Hat logo (50%)', 'Heard of it but don\'t understand\n the specific meaning (48%)', 'Completely unaware (4%)']
sizes = [50, 48, 4]
colors = ['#4A90E2', '#50E3C2', '#B8E986']  # Custom colors

# Create a pie chart
fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct='%1.0f%%',
    startangle=140,
    textprops={'fontsize': 14}
)

# Add a title
plt.title('Consumer awareness distribution of the Blue Hat logo for health foods', fontsize=14, fontweight='bold')

# Add data source
plt.figtext(0.5, 0.01, 'Data source: CBNData 2023 health food omnichannel consumer research data',
            wrap=True, horizontalalignment='center', fontsize=12)

plt.tight_layout()
plt.show()