import matplotlib.pyplot as plt
import numpy as np

# Years
years = np.arange(2011, 2021)

# Data (example, can be adjusted according to actual situation)
# China: Logistics cost as a percentage of GDP (%)
china_logistics = [17.2, 17.4, 17.1, 16.5, 15.7, 14.9, 14.7, 14.8, 14.7, 14.7]
# China: Storage cost as a percentage of GDP (%)
china_storage = [5.1, 5.2, 5.3, 5.3, 5.1, 5.0, 4.7, 5.1, 5.0, 5.0]
# USA: Logistics cost as a percentage of GDP (%)
usa_logistics = [7.8, 7.8, 7.8, 7.8, 7.6, 7.4, 8.0, 7.8, 7.6, 7.4]
# USA: Storage cost as a percentage of GDP (%)
usa_storage = [3.6, 3.9, 3.1, 3.0, 2.5, 2.4, 2.2, 2.6, 2.5, 2.5]

# Create a canvas
fig, ax = plt.subplots(figsize=(10, 6))

ax.set_ylim(0, 20)

# Plot the line of China's logistics cost ratio
ax.plot(years, china_logistics, marker='o', color='#8BC34A', label='China: Logistics cost as a % of GDP', linewidth=2)
# Plot the line of USA's logistics cost ratio
ax.plot(years, usa_logistics, marker='o', color='#2196F3', label='USA: Logistics cost as a % of GDP', linewidth=2)
# Plot the line of China's storage cost ratio
ax.plot(years, china_storage, marker='o', color='#FFC107', label='China: Storage cost as a % of GDP', linewidth=2)
# Plot the line of USA's storage cost ratio
ax.plot(years, usa_storage, marker='o', color='#F48FB1', label='USA: Storage cost as a % of GDP', linewidth=2)

# Add data labels
for y_arr, color in zip([china_logistics, usa_logistics, china_storage, usa_storage], 
                        ['#8BC34A', '#2196F3', '#FFC107', '#F48FB1']):
    for x, y in zip(years, y_arr):
        ax.annotate(f'{y}',
                    xy=(x, y),
                    xytext=(0, 3),
                    textcoords='offset points',
                    ha='center',
                    va='bottom',
                    color=color)

# Set the axes and title
ax.set_xlabel('Year')
ax.set_ylabel('Percentage (%)')
ax.set_title('Comparison of Logistics Cost as a Percentage of GDP between China and the USA from 2011 to 2020', fontsize=14, fontweight='bold')
ax.set_xticks(years)
ax.set_xticklabels(years)

# Add a legend
ax.legend(loc='upper right')

# Beautification: Hide the top and right borders
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()