import matplotlib.pyplot as plt
import numpy as np

# Data organization
companies = ["Yili Group", "Bright Dairy", "New Hope Dairy"]
# Operating revenue in 2022 (billion yuan)
revenue_2022 = [1227.0, 282.15, 100.06]
# Operating revenue in the first half of 2023 (billion yuan)
revenue_2023h = [659.82, 141.39, 52.98]
# Proportion of liquid milk in 2022 (%)
ratio_2022 = [69.22, 57.03, 87.76]
# Proportion of liquid milk in 2023 (%)
ratio_2023 = [64.29, 58.40, 90.94]

x = np.arange(len(companies))  # Dairy company names as X-axis coordinates
width = 0.35  # Bar width

# Create a canvas
fig, ax1 = plt.subplots(figsize=(10, 6))

# Draw the bar chart of operating revenue in 2022 and the first half of 2023
bar_2022 = ax1.bar(x - width/2, revenue_2022, width, label='Operating revenue in 2022', color='#FF7F50')
bar_2023h = ax1.bar(x + width/2, revenue_2023h, width, label='Operating revenue in H1 2023', color='#40E0D0')

# Label the operating revenue values
for bar in bar_2022 + bar_2023h:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, height + 5, f'{height:.1f} billion yuan', ha='center', va='bottom')

# Configure the left Y-axis (operating revenue)
ax1.set_ylabel('Operating revenue (billion yuan)', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(companies, fontsize=12)
ax1.legend(loc='lower left')

# Create the right Y-axis (proportion of liquid milk)
ax2 = ax1.twinx()
ax2.plot(x, ratio_2022, marker='o', color='#FFD700', label='Proportion of liquid milk in 2022', linewidth=2)
ax2.plot(x, ratio_2023, marker='s', color='#DA70D6', label='Proportion of liquid milk in 2023', linewidth=2)

# Label the proportion of liquid milk values
for i, (r22, r23) in enumerate(zip(ratio_2022, ratio_2023)):
    ax2.text(i, r22 + 1, f'{r22:.2f}%', ha='center', va='bottom', color='#FFD700')
    ax2.text(i, r23 + 1, f'{r23:.2f}%', ha='center', va='bottom', color='#DA70D6')

# Configure the right Y-axis (proportion of liquid milk)
ax2.set_ylabel('Proportion of liquid milk revenue (%)', fontsize=12)
ax2.legend(loc='center right')

# Chart title
plt.title('Operating revenue and proportion of liquid milk revenue of some Chinese dairy companies', fontsize=14, pad=20)
plt.tight_layout()
plt.show()