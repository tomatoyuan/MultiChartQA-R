import matplotlib.pyplot as plt

# Data
years = [2023, 2024, 2029]
market_size = [3500, 3700, 3850]  # Approximate data for 2023 and 2024. 2029E is an example value and can be replaced with actual accurate data.

# Create a chart
fig, ax = plt.subplots()

# Use indices as x - positions to evenly distribute the bars
x_pos = range(len(years))
bars = ax.bar(x_pos, market_size, color='pink')

# Add a title and labels
ax.set_title('Global Functional Apparel Market Size')
ax.set_ylabel('(Billion US Dollars)')
ax.text(0.5, 1.05, 'CAGR = 6.1%\n*From 2024 to 2029', ha='center', va='bottom', transform=ax.transAxes)

# Set x - axis labels (keep the "E" in the x-axis label to indicate forecast)
ax.set_xticks(x_pos)
ax.set_xticklabels(['2023', '2024', '... 2029E'])

# Add data labels above each bar (without "E")
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 10,
            f'{height}',  # Removed "E" from the label
            ha='center', va='bottom',
            fontweight='bold')  # Make labels bold for better visibility

# Set y - axis ticks
ax.set_ylim([3300, 3900])
ax.set_yticks(range(3300, 3901, 100))

# Display the chart
plt.show()