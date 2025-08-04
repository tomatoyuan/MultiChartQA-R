import matplotlib.pyplot as plt
import numpy as np

# Years
years = np.arange(2015, 2022)

# Data (example, can be adjusted according to actual situation)
# Residents' health literacy level (%)
health_literacy = [10.4, 11.6, 14.3, 17.1, 19.5, 23.2, 25.4]
# Health lifestyle and behavior literacy level (%)
lifestyle_literacy = [10.3, 9.8, 14.2, 17.0, 19.2, 26.4, 28.1]

# Create a canvas
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the line for residents' health literacy level (with upper labels)
health_line, = ax.plot(years, health_literacy, marker='o', color='#A4C639', label='Residents\' Health Literacy Level (%)', linewidth=2)
# Plot the line for health lifestyle and behavior literacy level (with lower labels)
lifestyle_line, = ax.plot(years, lifestyle_literacy, marker='o', color='#64B5F6', label='Health Lifestyle and Behavior Literacy Level (%)', linewidth=2)

# Add upper labels to the line of residents' health literacy level
for x, y in zip(years, health_literacy):
    ax.annotate(f'{y}%',
                xy=(x, y),
                xytext=(0, 5),  # Offset above
                textcoords='offset points',
                ha='center',
                va='bottom',
                color='#A4C639')

# Add lower labels to the line of health lifestyle and behavior literacy level
for x, y in zip(years, lifestyle_literacy):
    ax.annotate(f'{y}%',
                xy=(x, y),
                xytext=(0, -10),  # Offset below
                textcoords='offset points',
                ha='center',
                va='top',
                color='#64B5F6')

# Set axes and title
ax.set_xlabel('Year')
ax.set_ylabel('Literacy Level (%)')
ax.set_title('China Residents\' Health Literacy Level from 2015 to 2021', fontsize=14, fontweight='bold')
ax.set_xticks(years)
ax.set_xticklabels(years)

# Add a legend
ax.legend(loc='upper left')

# Beautification: Hide the top and right borders
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()