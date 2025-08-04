import matplotlib.pyplot as plt
import numpy as np

# Time axis data
dates = ['Jan 2015', 'Mar 2015', 'May 2015', 'Jul 2015', 'Sep 2015', 
         'Nov 2015', 'Jan 2016', 'Mar 2016', 'May 2016', 'Jul 2016', 'Sep 2016']

# Search index data with slight fluctuations (manually adjusted)
search_index = [
    2950,  # Original 3000
    2980,  # Original 3000
    3020,  # Original 3000
    6000,
    9000,
    2950,  # Original 3000
    2960,  # Original 3000
    2970,  # Original 3000
    3010,  # Original 3000
    9000,
    15000
]

# Convert the time axis to an index for plotting
x = np.arange(len(dates))  

# Create a plotting object
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the line chart, set the line width and marker style
line, = ax.plot(x, search_index, color='orange', marker='o', markersize=6, 
                linewidth=2, label='Trend of Air - conditioning sickness search index')

# Set the x - axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(dates, rotation=45, ha='right')

# Set the y - axis range and label
ax.set_ylim(0, 1.1 * max(search_index))
ax.set_ylabel('Search Index')

# Add a title and subtitle
ax.set_title('Search Index Related to "Air - conditioning sickness"', fontsize=16, pad=15)

# Annotate the values on the line chart
for i, (xi, yi) in enumerate(zip(x, search_index)):
    ax.annotate(f'{int(round(yi))}',  # Display as an integer
                (xi, yi),
                textcoords='offset points',
                xytext=(0, 10),  # Text position offset
                ha='center',
                fontsize=9)

# Add a legend and grid lines
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Hide the top and right axes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Adjust the layout
plt.tight_layout()

# Display the chart
plt.show()