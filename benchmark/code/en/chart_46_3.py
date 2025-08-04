import matplotlib.pyplot as plt
import numpy as np

# Data
years = ['2022', '2030E']
values = [8.2, 17.4]

# Used to display the compound annual growth rate at a suitable position above the bar chart. Here, it is simply set above the middle of the two bars.
x_pos = 0.5
y_pos = max(values) + 1

# Create a figure and axes
fig, ax = plt.subplots()

# Draw a bar chart
ax.bar(years, values, color='skyblue')

# Add data labels
for x, y in zip(years, values):
    ax.text(x, y + 0.2, f'{y}', ha='center', va='bottom')

# Set the title
ax.set_title('China Ergonomic Chair Market Size and Outlook from 2022 to 2030 (in billions of US dollars)')

# Display the figure
plt.show()