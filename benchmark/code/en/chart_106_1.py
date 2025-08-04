import matplotlib.pyplot as plt
import numpy as np

# Beverage categories
categories = ["Vinegar drinks (e.g., Tiandi Yihao)", "Powdered drinks (e.g., Xiangpiaopiao)", "Milk - based drinks (e.g., yogurt, sour milk)", "Coffee drinks (e.g., Nescafé)", 
              "Plant - based protein drinks (e.g., soy milk)", "Tea drinks (e.g., Master Kong Jasmine Green Tea)", "Energy drinks (e.g., Dongpeng Special Drink)", "Carbonated drinks (e.g., cola)", 
              "Sparkling water (e.g., Yuanqi Forest)", "Juice or vegetable juice drinks (e.g., Minute Maid Pulpy Orange)", "Packaged drinking water (e.g., C'estbon mineral water)", "Dairy products (e.g., yogurt, milk)"]
# Corresponding proportions (%)
proportions = [16.10, 16.90, 29.30, 29.40, 31.00, 31.60, 32.80, 49.50, 50.90, 51.00, 51.00, 51.70]

y = np.arange(len(categories))  # y-axis coordinates

fig, ax = plt.subplots(figsize=(10, 7))
# Draw a horizontal bar chart
bars = ax.barh(y, proportions, color='orange')

# Add numerical annotations
for i, proportion in enumerate(proportions):
    ax.text(proportion, i, f'{proportion}', va='center', ha='left', fontsize=9)

# Set y-axis ticks and labels
ax.set_yticks(y)
ax.set_yticklabels(categories)
ax.set_xlabel('Proportion (%)')
ax.set_title('Chinese consumers\' awareness of beverage categories in 2025')

plt.tight_layout()
plt.show()