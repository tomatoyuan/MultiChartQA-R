import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2017", "2018", "2019", "2020", "2021", "2022", "2023"]
# Catering revenue (trillion yuan)
catering_revenue = [3.96, 4.27, 4.67, 3.95, 4.69, 4.39, 5.29]
# Year-on-year change in catering revenue (%)
catering_yoy = [10.7, 7.8, 9.4, -15.4, 18.6, -6.3, 20.9]
# Year-on-year change in catering revenue above the quota (%)
above_limit_yoy = [7.4, 6.4, 7.1, -14.0, 23.5, -5.9, 20.4]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(10, 6))

# Draw a bar chart of catering revenue
ax1.bar(x, catering_revenue, color='orange', label='Catering revenue (trillion yuan)')
ax1.set_ylabel('Catering revenue (trillion yuan)')
ax1.set_xlabel('Year')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# Create a secondary y-axis and draw a line chart of year-on-year changes
ax2 = ax1.twinx()
ax2.plot(x, catering_yoy, marker='o', color='brown', label='Year-on-year change in catering revenue (%)')
ax2.plot(x, above_limit_yoy, marker='o', color='blue', label='Year-on-year change in catering revenue above the quota (%)')
ax2.set_ylabel('Year-on-year change (%)')
ax2.legend(loc='center right')

# Add catering revenue value labels
for i, rev in enumerate(catering_revenue):
    ax1.text(i, rev + 0.1, f'{rev}', ha='center', va='bottom')

# Add year-on-year change value labels for catering revenue
for i, yoy in enumerate(catering_yoy):
    ax2.text(i, yoy + 1, f'{yoy}%', ha='center', va='bottom')

# Add year-on-year change value labels for catering revenue above the quota
for i, above_yoy in enumerate(above_limit_yoy):
    ax2.text(i, above_yoy + 1, f'{above_yoy}%', ha='center', va='bottom')

ax1.set_title('China\'s catering revenue and year-on-year changes from 2017 to 2023')

plt.tight_layout()
plt.show()