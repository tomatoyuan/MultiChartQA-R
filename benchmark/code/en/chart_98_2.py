import matplotlib.pyplot as plt

# Year and proportion data
years = ["2020", "2021"]
percentages = [10, 13]
# Custom colors (adjustable)
colors = ["#A4C639", "#87CEEB"]

# Create a canvas (two - row layout)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 8))  # Increase the canvas size

# Set the overall title
fig.suptitle("Online Transaction Proportion of Two - wheeled Lithium Electric Vehicles", fontsize=16, fontweight="bold", y=0.95)

# Draw the pie chart for 2020
wedges, texts, autotexts = ax1.pie(
    [percentages[0], 100 - percentages[0]],  # Show the proportion part and the remaining part
    labels=[years[0], ""],  # The main label shows the year
    colors=[colors[0], 'lightgray'],  # Use the main color for the proportion part and light gray for the remaining part
    autopct=lambda p: f'≈{p:.0f}%' if p >= percentages[0] else '',  # Only show the percentage on the proportion part
    startangle=90,
    textprops={'fontsize': 12},
    wedgeprops={'edgecolor': 'white', 'linewidth': 1}  # Add a white border for separation
)
ax1.set_title(f"Market Share in {years[0]}: {percentages[0]}%", fontsize=14, pad=10)  # Clearly label the year and proportion
ax1.set_aspect('equal')  # Ensure a circular shape

# Draw the pie chart for 2021
wedges, texts, autotexts = ax2.pie(
    [percentages[1], 100 - percentages[1]],
    labels=[years[1], ""],
    colors=[colors[1], 'lightgray'],
    autopct=lambda p: f'≈{p:.0f}%' if p >= percentages[1] else '',
    startangle=90,
    textprops={'fontsize': 12},
    wedgeprops={'edgecolor': 'white', 'linewidth': 1}
)
ax2.set_title(f"Market Share in {years[1]}: {percentages[1]}%", fontsize=14, pad=10)
ax2.set_aspect('equal')

# Hide the borders
for ax in [ax1, ax2]:
    ax.axis('off')  # Completely hide the axes

# Adjust the spacing between sub - plots
plt.subplots_adjust(hspace=0.3)

plt.show()