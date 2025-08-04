import matplotlib.pyplot as plt
import numpy as np

# Data
years = [2015, 2016, 2017, 2018]
# Attention in each quarter (Quarter 1 - 4)
q1 = [1000, 1200, 5000, 4000]
q2 = [800, 1300, 4800, 5000]
q3 = [600, 1100, 4600, 4500]
q4 = [1200, 1500, 8000, 1500]
# Newly reported HIV infections
new_infections = [115465, 124555, 134512, 160000]

# Offset for plotting multiple bar charts on the same X - axis
x = np.arange(len(years))
width = 0.2

# Create a canvas and subplots
fig, ax1 = plt.subplots(figsize=(8, 5))

# Plot bar charts for attention in each quarter
ax1.bar(x - 1.5*width, q1, width, label='Quarter 1', color='#f78b9b')
ax1.bar(x - 0.5*width, q2, width, label='Quarter 2', color='#ff5e2d')
ax1.bar(x + 0.5*width, q3, width, label='Quarter 3', color='#d4b17c')
ax1.bar(x + 1.5*width, q4, width, label='Quarter 4', color='#3b3b3b')

# Set the title of the left Y - axis (Attention)
ax1.set_ylabel('Attention', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# Create the right Y - axis for plotting the line chart of newly reported HIV infections
ax2 = ax1.twinx()
line, = ax2.plot(x, new_infections, marker='o', color='#8bc34a', label='Newly reported HIV infections')

# Add data labels to the line chart
for i, (x_val, y_val) in enumerate(zip(x, new_infections)):
    # Convert the number of infections to a string with thousands separators
    y_text = f"{y_val:,}"
    ax2.annotate(y_text,  # Annotation text
                 (x_val, y_val),  # Data point position
                 textcoords="offset points",  # Text coordinates relative to the data point
                 xytext=(0, 10),  # Offset in the X and Y directions
                 ha='center',  # Horizontal alignment
                 fontsize=9)  # Font size

ax2.set_ylabel('Newly reported HIV infections', fontsize=12)
ax2.legend(loc='upper right')

# Chart title
plt.title('Attention to "AIDS" - related information and newly reported HIV infections (2015 - 2018)', fontsize=14, pad=20)

# Adjust the layout
plt.tight_layout()
# Display the chart
plt.show()