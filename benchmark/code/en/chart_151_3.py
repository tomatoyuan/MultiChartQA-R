# Chart 3: Response Measures for Adverse Reactions (Donut Chart with Highlighted Sector)

# Data
labels = [
    'Rest and drink plenty of water', 'Improve diet', 'Take over - the - counter medications',
    'Take probiotics for conditioning', 'Do nothing', 'Go to a regular hospital immediately', 'Seek advice from family and friends'
]
sizes = [18.5, 17.4, 20.3, 15.0, 2.9, 12.4, 13.5]
highlight_index = 3  # Highlight "Take probiotics for conditioning"

# Define colors and highlighted item
colors = ['#555', '#666', '#777', '#0056d6', '#999', '#bbb', '#99c']
explode = [0.01 if i == highlight_index else 0 for i in range(len(labels))]

# Plotting
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts, autotexts = ax.pie(
    sizes, labels=None, autopct='%1.1f%%', startangle=90,
    counterclock=False, colors=colors,
    explode=explode, wedgeprops=dict(width=0.4, edgecolor='white'),
    textprops={'fontsize': 10}
)

# Set the legend
ax.legend(wedges, labels, title="Response Methods", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=10)

# Center text
ax.text(0, 0, 'Response measures\nfor adverse reactions', ha='center', va='center', fontsize=12, fontweight='bold')

# Title
ax.set_title("Response measures for adverse reactions (User proportion)", fontsize=14)
plt.tight_layout()
plt.show()