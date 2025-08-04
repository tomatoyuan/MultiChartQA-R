import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2017", "2018", "2019", "2020", "2021", "2022", "2023"]
# Operating costs (in billions of yuan)
operating_cost = [17343.1, 17790.9, 17198.7, 16446.5, 18463.0, 20525.4, 21906.8]
# Operating revenues (in billions of yuan)
operating_revenue = [14610.8, 15107.0, 14788.1, 14240.7, 16142.4, 17716.5, 21442.0]
# Revenue growth rate (%)
revenue_growth = [15.8, 3.4, -2.1, -3.7, 13.4, 9.8, 23.7]

x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(12, 8))

# Draw operating costs (simulated with yellow dashed boxes, first draw the background boxes for costs)
for i in range(len(years)):
    # Draw yellow dashed rectangular boxes
    rect = plt.Rectangle((x[i] - 0.2, 0), 0.4, operating_cost[i], fill=False, edgecolor='gold', linestyle='--', linewidth=2)
    ax.add_patch(rect)
    # Label the operating cost values
    ax.text(x[i], operating_cost[i] + 500, f'{operating_cost[i]}', ha='center', va='bottom')

# Draw the bar chart of operating revenues
bars = ax.bar(x, operating_revenue, color='blue', label='Operating Revenue (in billions of yuan)', width=0.4)
# Label the operating revenue values
for i, rev in enumerate(operating_revenue):
    ax.text(i, rev + 500, f'{rev}', ha='center', va='bottom')

# Draw the circular annotations for revenue growth rate (approximate simulation, displayed above with text)
for i, growth in enumerate(revenue_growth):
    # The position of the circular annotation is above the bar, highlighted with a circular background (simplified)
    circle = plt.Circle((x[i], operating_revenue[i] + 2000), 0.3, color='lightcoral', alpha=0.3)
    ax.add_artist(circle)
    ax.text(x[i], operating_revenue[i] + 1500, f'{growth}%', ha='center', va='center', fontsize=12, color='red')

ax.set_ylabel('Amount (in billions of yuan)')
ax.set_xlabel('Year')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()
ax.set_title('Operating Revenue and Cost of A-share New Energy Vehicle Manufacturers in China from 2017 to 2023')

plt.ylim(0, max(operating_cost) + 3000)  # Adjust the y-axis range to accommodate the annotations
plt.tight_layout()
plt.show()