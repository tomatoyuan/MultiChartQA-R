import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2016", "2017", "2018", "2019", "2020", "2021", "2022"]
# Various types of production data (Unit: 10,000 tons), order: Vegetables, Meat, Aquatic products
vegetable = [67434.2, 69192.7, 70346.7, 72102.6, 74912.9, 77549.0, 80000.0]
meat = [8628.3, 8654.4, 8624.6, 7758.8, 7748.4, 8990.0, 9328.4]
aquatic = [6379.5, 6445.3, 6457.7, 6480.4, 6549.0, 6690.0, 6549.0]

x = np.arange(len(years))  # x-axis coordinates
bar_width = 0.3  # Width of each category's bar chart

fig, ax = plt.subplots(figsize=(12, 8))

# Draw the bar chart for vegetable production (at the bottom)
ax.bar(x, vegetable, width=bar_width, label='Vegetable Production (10,000 tons)', color='#CD5C5C')
# Draw the bar chart for meat production (above the vegetable production)
ax.bar(x, meat, width=bar_width, bottom=vegetable, label='Meat Production (10,000 tons)', color='#FFA07A')
# Draw the bar chart for aquatic product production (above the meat production)
ax.bar(x, aquatic, width=bar_width, bottom=np.array(vegetable) + np.array(meat), 
       label='Total Aquatic Product Production (10,000 tons)', color='#FFDAB9')

# Add numerical labels for various types of production
# Label the vegetable production
for i, v in enumerate(vegetable):
    ax.text(i, v / 2, f'{v}', ha='center', va='center', color='white', fontweight='bold')
# Label the meat production
for i, (v, m) in enumerate(zip(vegetable, meat)):
    ax.text(i, v + m / 2, f'{m}', ha='center', va='center', color='white', fontweight='bold')
# Label the aquatic product production
for i, (v, m, a) in enumerate(zip(vegetable, meat, aquatic)):
    bottom_sum = v + m
    ax.text(i, bottom_sum + a / 2, f'{a}', ha='center', va='center', color='white', fontweight='bold')

ax.set_ylabel('Production (10,000 tons)')
ax.set_xlabel('Year')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()
ax.set_title('Production of Hot Pot Ingredient Raw Materials in China from 2016 - 2022')

plt.tight_layout()
plt.show()