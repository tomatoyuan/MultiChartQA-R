import matplotlib.pyplot as plt
import numpy as np

# Data preparation
# Proportion of each city type in the in - store service (assuming from left to right corresponding to first - tier cities, new first - tier cities, second - tier cities, and third - tier and below cities, judged visually from the bar chart)
store_service = [28.1, 32.4, 31.4, 8.1]
# Proportion of each city type in the home - delivery service (similarly corresponding)
home_service = [23.0, 32.9, 35.9, 8.2]

# City type labels (inferred from the number of bars in the bar chart)
city_types = ["First - tier cities", "New first - tier cities", "Second - tier cities", "Third - tier and below cities"]
x = np.arange(len(city_types))  # x - axis coordinates

fig, ax = plt.subplots(figsize=(12, 7))

# Draw the bar chart for the in - store service (yellow series)
bar_width = 0.35
ax.bar(x - bar_width/2, store_service, width=bar_width, color=['gold', 'peru', 'coral', 'lightpink'], label='In - store service')
# Draw the bar chart for the home - delivery service (orange series)
ax.bar(x + bar_width/2, home_service, width=bar_width, color=['orange', 'darkorange', 'tomato', 'lightcoral'], label='Home - delivery service')

ax.set_title('Survey on the consumption willingness of Internet users in Chinese cities of different tiers for local life service products in 2023', fontsize=14)
ax.set_ylabel('Consumption willingness proportion (%)')
ax.set_xticks(x)
ax.set_xticklabels(city_types)
ax.legend()

# Add value labels for the in - store service
for i, val in enumerate(store_service):
    ax.text(x[i] - bar_width/2, val + 1, f'{val}%', ha='center', va='bottom', color='black')

# Add value labels for the home - delivery service
for i, val in enumerate(home_service):
    ax.text(x[i] + bar_width/2, val + 1, f'{val}%', ha='center', va='bottom', color='black')

plt.tight_layout()
plt.show()