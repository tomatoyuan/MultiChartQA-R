import matplotlib.pyplot as plt
import numpy as np

# Data preparation
brands = [
    "元气森林", "Coca - Cola", "Nongfu Spring", "Oriental Leaves", 
    "Pepsi", "Wanglaoji", "Vitasoy", "Suntory", 
    "Schweppes", "Watsons", "Yineng", "Mingren", "Lingqi"
]
proportions = [49.54, 42.52, 42.38, 34.70, 
               34.44, 23.05, 21.19, 20.00, 
               14.83, 14.70, 9.93, 9.93, 9.27]  # Proportion (%)

x = np.arange(len(brands))

fig, ax = plt.subplots(figsize=(10, 8))

# Draw a horizontal bar chart
bars = ax.barh(x, proportions, color='coral')
ax.set_title('Popular Sugar - free Beverage Brands among Chinese Consumers in 2023', fontsize=14)
ax.set_xlabel('Proportion (%)')
ax.set_ylabel('Sugar - free Beverage Brands')
ax.set_yticks(x)
ax.set_yticklabels(brands)
ax.set_xlim(0, 55)  # Adjust the x - axis range to fit the maximum proportion (49.54%)

# Add numerical labels
for i, prop in enumerate(proportions):
    ax.text(prop + 1, i, f'{prop}%', ha='left', va='center', color='black', fontsize=11)

# Add a legend and sample source (adjust the position if you need to restore the original image)
ax.legend(bars, ['Proportion'], loc='lower right')
ax.text(0.8, -0.12, 'Sample Source: Strawberry Pie Data Survey and Calculation System', 
        fontsize=10, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.show()