import matplotlib.pyplot as plt
import numpy as np

# Set quarterly data
quarters = ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023', 'Q1 2024', 'Q2 2024']
# App Store download volume data (in hundreds of millions), adjusted so that Q1 2024 + Q2 2024 ≈ 1.76
app_store = [0.77, 0.8, 0.95, 0.85, 0.95, 0.81]
# Google Play download volume data (in hundreds of millions), adjusted so that Q1 2024 + Q2 2024 ≈ 1.44
google_play = [0.8, 0.75, 0.75, 0.8, 0.8, 0.64]

x = np.arange(len(quarters))  # x-axis tick positions
width = 0.5  # Increase bar width

# Create a wider chart (width 12, height 6)
fig, ax = plt.subplots(figsize=(12, 6))

# Draw App Store bars (bottom)
rects1 = ax.bar(x, app_store, width, label='App Store', color='#9b59b6')
# Draw Google Play bars (top)
rects2 = ax.bar(x, google_play, width, bottom=app_store, label='Google Play', color='#1abc9c')

# Set x-axis tick labels and rotation angle
ax.set_xticks(x)
ax.set_xticklabels(quarters, rotation=0)  # Display quarterly labels horizontally

# Set y-axis range and ticks
ax.set_ylim(0, 2.0)
ax.set_yticks([0, 0.5, 1.0, 1.5, 2.0])
ax.set_yticklabels(['000M', '50M', '100M', '150M', '200M'])

# Add data labels (modified to keep two decimal places)
def add_labels(rects, bottom_values=None):
    for i, rect in enumerate(rects):
        height = rect.get_height()
        if bottom_values is not None:
            y_pos = bottom_values[i] + height / 2
        else:
            y_pos = height / 2
        # Format to display two decimal places
        ax.text(rect.get_x() + rect.get_width()/2., y_pos,
                f'{height:.2f}', ha='center', va='center', color='white', fontweight='bold')

add_labels(rects1)  # App Store labels
add_labels(rects2, app_store)  # Google Play labels

# Add legend and title
ax.legend(loc='upper right')
ax.set_title('Trend of Mobile Game Downloads in the Japanese Market from Q1 2023 to Q2 2024', fontsize=16, pad=20)

# Add grid lines
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Add specified text below the title (adjust y-coordinate to 0.92)
text = "In the first half of 2024, the number of mobile game downloads in the Japanese market increased by 2.5% year-on-year, reaching 320 million, of which the App Store platform accounted for 55% of the downloads."
fig.text(0.5, 0.92, text, ha='center', va='center', fontsize=12)

# Adjust layout
plt.tight_layout()

plt.show()