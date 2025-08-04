import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

# Player names
players = ["Messi", "Neymar", "Salah", "Ronaldo", "Ramos", "Iniesta", "Kane", "Pogba", "Griezmann", "Cheryshev"]
# Heat data
heats = [80, 33, 27, 20, 15, 12, 13.1, 13.1, 13, 6.4]
# Generate indices to map x-axis ticks to players
x = np.arange(len(players))  

# Create a figure
fig, ax = plt.subplots()
# Plot a bar chart with a gradient color from purple to pink
bars = ax.bar(x, heats, color=plt.cm.get_cmap('Purples')(np.linspace(0.2, 0.8, len(players))))

# Set x-axis tick labels to player names
ax.set_xticks(x)
ax.set_xticklabels(players, rotation=45)

# Set y-axis label
ax.set_ylabel("Popularity (ten thousand)")
# Set the title
ax.set_title("Top 10 Popularity Ranking of Football Stars")

# Annotate values on the bars
for bar, heat in zip(bars, heats):
    height = bar.get_height()
    ax.annotate(f'{heat}K',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Vertical offset of the value relative to the bar
                textcoords="offset points",
                ha='center', va='bottom')

# Adjust the layout to prevent labels from being cut off
plt.tight_layout()
# Display the chart
plt.show()