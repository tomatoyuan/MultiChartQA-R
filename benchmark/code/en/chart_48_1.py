import matplotlib.pyplot as plt
import numpy as np

# Years
years = np.array([2019, 2020, 2021, 2022, 2023])
# Population aged 60 and above (in ten thousand people)
elderly_population = np.array([25388, 26402, 26736, 28004, 29697])
# Proportion of population aged 60 and above (%)
proportion = np.array([18.1, 18.7, 18.9, 19.8, 21.1])

# Create a figure and an axis
fig, ax1 = plt.subplots(figsize=(10, 6))

# Draw a bar chart (left - hand axis)
bars = ax1.bar(years, elderly_population, color='darkgreen', label='Population aged 60 and above (in ten thousand people)')
ax1.set_xlabel('Year')
ax1.set_ylabel('Population aged 60 and above (in ten thousand people)', color='darkgreen')
ax1.tick_params(axis='y', labelcolor='darkgreen')

# Add data labels above the bars
for bar, pop in zip(bars, elderly_population):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 200, 
             f'{pop}', ha='center', va='bottom', color='darkgreen')

# Create a right - hand axis for the line chart
ax2 = ax1.twinx()
line, = ax2.plot(years, proportion, marker='o', color='black', label='Proportion of population aged 60 and above (%)')
ax2.set_ylabel('Proportion of population aged 60 and above (%)', color='black')
ax2.tick_params(axis='y', labelcolor='black')

# Add data labels beside the data points of the line chart
for x, y in zip(years, proportion):
    ax2.annotate(f'{y}%', (x, y), textcoords='offset points',
                 xytext=(0,10), ha='center', color='black')

# Add a legend
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left')

# Set the x - axis ticks to years
ax1.set_xticks(years)

# Display the chart
plt.title('Population aged 60 and above and its proportion of the total population from 2019 to 2023')
plt.tight_layout()  # Adjust the layout to avoid content overlap
plt.show()