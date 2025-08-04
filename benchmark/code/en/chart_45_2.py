import matplotlib.pyplot as plt

# Data
years = [2023, 2024, 2029]
market_size = [9000, 9500, 15000]  # Approximate data for 2023 and 2024. The value for 2029E is an example and can be replaced with actual precise data.
# If there are precise market size data for 2023 and 2024, directly replace the corresponding values in the list.

# Create a chart
fig, ax = plt.subplots()

# Use indices as x - positions to make the bars evenly distributed
x_pos = range(len(years))
bars = ax.bar(x_pos, market_size, color='pink')

# Add a title and labels
ax.set_title('China Functional Apparel Market Size')
ax.set_ylabel('(Billion Yuan)')
ax.text(0.5, 1.05, 'CAGR = 9.8%\n*From 2024 to 2029', ha='center', va='bottom', transform=ax.transAxes)

# Set x - axis labels (use ellipsis to represent intermediate years and add the E mark for 2029)
ax.set_xticks(x_pos)
ax.set_xticklabels(['2023', '2024', '... 2029E'])

# Add data labels above each bar
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 200,  # 200 is the vertical offset
            f'{height}',
            ha='center', va='bottom',
            fontweight='bold')  # Make the labels bold for better visibility

# Set y - axis ticks
ax.set_ylim([0, 16000])  # Adjust the upper limit to ensure labels fit
ax.set_yticks(range(0, 16001, 5000))

# Display the chart
plt.show()