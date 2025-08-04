import matplotlib.pyplot as plt

# Date data
dates = ["Mar 28th", "Mar 30th", "Apr 1st", "Apr 3rd", "Apr 5th", "Apr 7th", "Apr 9th"]
# Corresponding numerical data
values = [290000, 290000, 580000, 870000, 1160000, 1450000, 1740000]

# Create a canvas and a sub - plot
fig, ax = plt.subplots(figsize=(10, 6))

# Draw a line chart, marker='o' shows dots, linewidth = 2.5 thickens the line
ax.plot(dates, values, color='red', marker='o', linewidth=2.5)

# Set y - axis ticks and labels
ax.set_yticks([290000, 580000, 870000, 1160000, 1450000, 1740000, 2030000])
ax.set_yticklabels(["290K", "580K", "870K", "1.16M", "1.45M", "1.74M", "2.03M"])

# Set x - axis labels, rotate 30 degrees for better appearance
ax.set_xticklabels(dates, rotation=30, ha='right', fontsize=10)

# Add grid lines to enhance readability
ax.grid(True, linestyle='--', alpha=0.7)

# Add title and axis labels
plt.title("Search Index Trend of 'In the Name of People' on the Internet", fontsize=15, pad=20)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Search Index", fontsize=12)

# Beautify the chart border
for spine in ax.spines.values():
    spine.set_color('gray')

# Add data labels
for x, y in zip(dates, values):
    ax.annotate(f'{y:,}', (x, y), textcoords='offset points',
                xytext=(0, 10), ha='center', fontsize=9)

# Display the graph
plt.tight_layout()
plt.show()