import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2016-12", "2017-12", "2018-12", "2019-12", "2020-12", "2021-12", "2022-12", "2023-12"]
# Online food delivery user scale (in ten thousand people)
user_scale = [20856, 34338, 40601, 39780, 41883, 54416, 52118, 54454]
# Penetration rate (percentage of the total Internet users)
penetration_rate = [28.5, 44.5, 49.0, 44.0, 42.3, 52.7, 48.8, 49.9]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot the bar chart of online food delivery user scale
ax1.bar(x, user_scale, color='orange', label='Online food delivery user scale (in ten thousand people)')
ax1.set_ylabel('Online food delivery user scale (in ten thousand people)')
ax1.set_xlabel('Year')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# Create a secondary y - axis and plot the line chart of penetration rate
ax2 = ax1.twinx()
ax2.plot(x, penetration_rate, marker='o', color='brown', label='Penetration rate (% of total Internet users)')
ax2.set_ylabel('Penetration rate (%)')
ax2.legend(loc='center right')

# Add labels for online food delivery user scale
for i, scale in enumerate(user_scale):
    ax1.text(i, scale + 500, f'{scale}', ha='center', va='bottom')

# Add labels for penetration rate
for i, rate in enumerate(penetration_rate):
    ax2.text(i, rate + 1, f'{rate}%', ha='center', va='bottom')

ax1.set_title('Online food delivery user scale and penetration rate in China from 2016 to 2023')

plt.tight_layout()
plt.show()