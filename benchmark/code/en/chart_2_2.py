import matplotlib.pyplot as plt
import numpy as np

# Quarterly data
quarters = ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023', 'Q1 2024', 'Q2 2024']
# In - app purchase revenue from the App Store (in billions of US dollars, simulated data close to the chart ratio)
app_store = [20, 18, 18, 17, 16.3, 14.4]
# In - app purchase revenue from Google Play (in billions of US dollars, simulated data close to the chart ratio)
google_play = [15, 12, 12, 11, 10.6, 11.7]

x = np.arange(len(quarters))  # x - axis tick positions
width = 0.5  # Bar width to make the chart more compact and beautiful

# Create a canvas and set the size
fig, ax = plt.subplots(figsize=(12, 6))

# Draw App Store bars (bottom, purple)
rects1 = ax.bar(x, app_store, width, label='App Store', color='#9b59b6')
# Draw Google Play bars (top, cyan, stacked on top of App Store data)
rects2 = ax.bar(x, google_play, width, bottom=app_store, label='Google Play', color='#1abc9c')

# Set x - axis ticks and labels, display horizontally
ax.set_xticks(x)
ax.set_xticklabels(quarters, rotation=0)

# Set the y - axis range and ticks to match the "0, 1.8, 3.6 billion US dollars" scale of the chart
ax.set_ylim(0, 36)
ax.set_yticks([0, 18, 36])
ax.set_yticklabels(['$0B', '$18B', '$36B'])

# Function to add data labels, showing the bar height (rounded to 1 decimal place)
def add_labels(rects, bottom_values=None):
    for i, rect in enumerate(rects):
        height = rect.get_height()
        y_pos = bottom_values[i] + height / 2 if bottom_values is not None else height / 2
        ax.text(
            rect.get_x() + rect.get_width()/2.,
            y_pos,
            f'{height:.1f}',  # Key modification: Force to keep 1 decimal place
            ha='center',
            va='center',
            color='white',
            fontweight='bold'
        )

add_labels(rects1)  # App Store data labels
add_labels(rects2, app_store)  # Google Play data labels

# Legend and title settings
ax.legend(loc='upper right')
ax.set_title('Trend of In - app Purchase Revenue of Mobile Games in the Japanese Market from Q1 2023 to Q2 2024', fontsize=16, pad=40)

# Add gridlines to assist in observing data
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Explanatory text above the chart, restoring the business background
text = ("In the second quarter of 2024, the average exchange rate of the Japanese yen against the US dollar decreased by 18% compared to the first quarter of 2023. Affected by the exchange rate,\n"
        "In the first half of 2024, despite the rebound in mobile game downloads, the in - app purchase revenue decreased by 17% year - on - year to $5.3 billion.")
# Adjust the text position to avoid overlapping with the title
fig.text(0.5, 0.89, text, ha='center', va='center', fontsize=12, linespacing=1.5)

# Automatically optimize the layout to ensure that elements are not squeezed
plt.tight_layout()

plt.show()