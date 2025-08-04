import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Low-saturation Lipstick', 'Fine Glitter Eyeshadow', 'Pink Eyeshadow', 'Date-scented Perfume', 'Autumn and Winter Mask', 'Home Beauty Device']
trade_growth = [39.5, 22.7, 323.2, 4.4, 382.8, 151.7]
payment_growth = [32.7, 22.2, 20.0, 168.1, 163.0, 32.1]

x = np.arange(len(categories))
width = 0.35

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - width/2, trade_growth, width, label='Transaction Index Growth Rate', color='orange')
bars2 = ax.bar(x + width/2, payment_growth, width, label='Payment Conversion Growth Rate', color='orangered')

# Text settings
ax.set_ylabel('Growth Rate (%)')
ax.set_title('Taobao Related Category Search & Transaction Data')
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=30)
ax.legend()

# Add data labels
for bar in bars1 + bars2:
    height = bar.get_height()
    ax.annotate(f'{height:.1f}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom')

plt.tight_layout()
plt.show()