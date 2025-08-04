import matplotlib.pyplot as plt
import numpy as np

# Years
years = np.arange(2019, 2029)
# Online market share (sample data, following the original trend)
online_share = [16, 20, 31, 33, 35, 36, 37, 47, 55, 60]
# Offline market share = 100 - online (simplified simulation to ensure the total logic)
offline_share = [100 - x for x in online_share]

# Bar width
bar_width = 0.6

# Create a canvas
fig, ax = plt.subplots()

# Plot the offline share (gray, corresponding to the bottom layer of the original chart)
offline_bars = ax.bar(years, offline_share, width=bar_width, color='#D3D3D3', label='Offline')
# Plot the online share (blue, corresponding to the upper layer of the original chart)
online_bars = ax.bar(years, online_share, width=bar_width, bottom=offline_share, color='#4682B4', label='Online')

# Set the x-axis ticks
ax.set_xticks(years)
# Set the y-axis label
ax.set_ylabel('Market Share (%)')
# Set the title
ax.set_title('Market Share Distribution of Online and Offline Channels for Household Cleaning and Care Products from 2019 to 2028')
# Add a legend
ax.legend()

# Add data labels for offline bars
for bar, share in zip(offline_bars, offline_share):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height/2,
            f'{share}%', ha='center', va='center', color='black')

# Add data labels for online bars
for bar, share, base in zip(online_bars, online_share, offline_share):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., base + height/2,
            f'{share}%', ha='center', va='center', color='white')

# Display the chart
plt.show()