import matplotlib.pyplot as plt

# Extract chart data
age_groups = ["Under 19", "20 - 29", "30 - 39", "40 - 49", "Over 50"]
percentages = [22, 36, 28, 9, 5]

# Custom color scheme (using soft blue - green tones)
colors = ['#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Highlight the largest sector (20 - 29 age group)
explode = (0, 0.1, 0, 0, 0)

# Create a plotting object
fig, ax = plt.subplots(figsize=(10, 7))

# Draw a beautified pie chart
wedges, texts, autotexts = ax.pie(
    percentages,
    explode=explode,
    labels=age_groups,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    shadow=True,
    wedgeprops={'edgecolor': 'w', 'linewidth': 1},
    textprops={'fontsize': 12}
)

# Set the color of the percentage labels to match the pie chart colors
for text, autotext, color in zip(texts, autotexts, colors):
    text.set_color('gray')
    autotext.set_color('black')
    autotext.set_fontweight('bold')

# Set the pie chart to be a perfect circle
ax.axis('equal')

# Add a title
ax.set_title('Age Distribution of Consumers Who "Regret the Most"', fontsize=16, fontweight='bold', pad=20)

# Add a legend and adjust its position
ax.legend(wedges, age_groups, title="Age Groups", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Set the chart background color
fig.set_facecolor('#f8f9fa')

# Adjust the layout
plt.tight_layout()

# Display the chart
plt.show()