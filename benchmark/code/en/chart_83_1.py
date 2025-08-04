import matplotlib.pyplot as plt
import numpy as np

# Years
years = np.arange(2010, 2021)
# Total value of equipment worth over 10,000 yuan (in ten thousand yuan), the data can be approximately the same
values = [61623, 73154, 120292, 155770, 164474, 240805, 318904, 468174, 642335, 748276, 746559]

# Create a canvas
fig, ax = plt.subplots(figsize=(10, 6))

# Draw a bar chart
bars = ax.bar(years, values, color='#A4C639', width=0.6)

# Add data labels
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 3),
                textcoords='offset points',
                ha='center',
                va='bottom',
                color='#A4C639')

# Add an explanatory text box
text_str = "The total value of equipment worth over 10,000 yuan in rehabilitation hospitals has been increasing year by year, \nindicating a positive overall development of the rehabilitation medical device urban market."
bbox_props = dict(boxstyle="round,pad=0.5", fc="white", ec="green", lw=1)
ax.text(0.09, 0.70, text_str, transform=ax.transAxes, fontsize=12,
        bbox=bbox_props, color='green')

# Set the axes and title
ax.set_xlabel('Year')
ax.set_ylabel('Total value of equipment worth over 10,000 yuan (in ten thousand yuan)')
ax.set_title('Total value of equipment worth over 10,000 yuan in Chinese rehabilitation hospitals from 2010 - 2020', fontsize=14, fontweight='bold')
ax.set_xticks(years)
ax.set_xticklabels(years)

# Beautification: Hide the top and right borders
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()