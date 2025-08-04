import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2019", "2020", "2021", "2022", "2023", "2024Q1-Q3"]
# Total operating revenue (in hundreds of millions of yuan)
total_revenue = [86624, 98514, 119064, 121805, 129515, 99668]
# New - format operating revenue (in hundreds of millions of yuan)
new_format_revenue = [19868, 31425, 39623, 43860, 52395, 41616]
# Proportion (%)
proportion = [22.9, 31.9, 33.3, 36.0, 40.5, 41.8]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot the bar chart of total operating revenue
ax1.bar(x, total_revenue, color='lightcoral', label='Total operating revenue (in hundreds of millions of yuan)', width=0.3)
# Plot the bar chart of new - format operating revenue (shifted to the right to avoid overlap)
ax1.bar(x + 0.3, new_format_revenue, color='coral', label='New - format operating revenue (in hundreds of millions of yuan)', width=0.3)
ax1.set_ylabel('Operating revenue (in hundreds of millions of yuan)')
ax1.set_xlabel('Years')
ax1.set_xticks(x + 0.15)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# Create a secondary y - axis and plot the line chart of proportion
ax2 = ax1.twinx()
ax2.plot(x, proportion, marker='o', color='gold', label='Proportion (%)')
ax2.set_ylabel('Proportion (%)')
ax2.legend(loc='upper right')

# Add value labels for total operating revenue
for i, rev in enumerate(total_revenue):
    ax1.text(i, rev + 1000, f'{rev}', ha='center', va='bottom')

# Add value labels for new - format operating revenue
for i, new_rev in enumerate(new_format_revenue):
    ax1.text(i + 0.3, new_rev + 1000, f'{new_rev}', ha='center', va='bottom')

# Add value labels for proportion
for i, prop in enumerate(proportion):
    ax2.text(i, prop + 1, f'{prop}%', ha='center', va='bottom')

ax1.set_title('Operating revenue of new cultural formats in China from 2019 to 2024')

plt.tight_layout()
plt.show()