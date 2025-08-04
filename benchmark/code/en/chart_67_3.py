import matplotlib.pyplot as plt
import numpy as np

# City names
cities = ["Beijing", "Shanghai", "Guangzhou", "Shenzhen"]
# Vacancy rate data of core business districts
core_vacancy = [9.8, 9.9, 7.6, 18.8]
# Vacancy rate data of high - quality office buildings in the whole city
city_vacancy = [17.1, 16.6, 11.9, 16.6]

# Create a canvas and sub - plots
fig, ax = plt.subplots(figsize=(8, 5))

# Draw the line of the vacancy rate of core business districts
core_line, = ax.plot(cities, core_vacancy, marker='o', color='#A4C639', label='Vacancy rate of core business districts (%)', linewidth=2)
# Draw the line of the vacancy rate of high - quality office buildings in the whole city
city_line, = ax.plot(cities, city_vacancy, marker='o', color='#64B5F6', label='Vacancy rate of high - quality office buildings in the whole city (%)', linewidth=2)

# Add data labels (core business districts)
for x, y in zip(cities, core_vacancy):
    ax.annotate(f'{y}%',
                xy=(x, y),
                xytext=(0, 5),  # Adjust the label position
                textcoords='offset points',
                ha='center', va='bottom',
                color='#A4C639')

# Add data labels (high - quality office buildings in the whole city)
for x, y in zip(cities, city_vacancy):
    ax.annotate(f'{y}%',
                xy=(x, y),
                xytext=(0, 5),  # Adjust the label position
                textcoords='offset points',
                ha='center', va='bottom',
                color='#64B5F6')

# Set the title
ax.set_title('Vacancy rate of high - quality office buildings in first - tier cities in China in 2021', fontsize=14, fontweight='bold')
# Add a legend
ax.legend()

# Beautify the chart by hiding the top and right borders
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()