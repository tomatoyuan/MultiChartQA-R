import matplotlib.pyplot as plt
import numpy as np

# Company names
companies = [
    "SAIC Motor", "BYD", "Great Wall Motor", "Changan Automobile", 
    "GAC Group", "FAW Jiefang", "Foton Motor", "Jianghuai Automobile", 
    "CNHTC", "SERES"
]
# Revenue in 2022 (in tens of billions of yuan)
revenue_2022 = [74.41, 42.41, 13.73, 12.13, 11.03, 3.83, 4.64, 3.66, 2.88, 3.41]
# Revenue in 2023 (in tens of billions of yuan)
revenue_2023 = [74.47, 60.23, 17.32, 15.13, 12.97, 6.39, 5.61, 4.50, 4.21, 3.58]
# Growth rates (%)
growth_rates = [0.09, 42.04, 26.12, 24.78, 17.62, 66.71, 20.78, 23.07, 45.96, 5.09]

x = np.arange(len(companies))

fig, ax = plt.subplots(figsize=(14, 8))

# Draw the revenue bar chart for 2022 (orange)
ax.bar(x - 0.2, revenue_2022, width=0.4, color='orange', label='Revenue in 2022 (in tens of billions of yuan)')
# Draw the revenue bar chart for 2023 (blue)
ax.bar(x + 0.2, revenue_2023, width=0.4, color='blue', label='Revenue in 2023 (in tens of billions of yuan)')

# Add revenue value labels for 2022
for i, rev in enumerate(revenue_2022):
    ax.text(x[i] - 0.2, rev + 0.5, f'{rev}', ha='center', va='bottom')

# Add revenue value labels for 2023
for i, rev in enumerate(revenue_2023):
    ax.text(x[i] + 0.2, rev + 0.5, f'{rev}', ha='center', va='bottom')

# Add growth rate value labels (on the right)
for i, rate in enumerate(growth_rates):
    ax.text(len(companies) + 0.5, x[i], f'{rate}%', ha='center', va='center', color='black')
    # Draw an upward arrow (simplified as a text arrow, or use matplotlib.patches to draw a graphic arrow)
    ax.text(len(companies) + 0.2, x[i], '↑', ha='center', va='center', color='orange', fontsize=16)

ax.set_ylabel('Revenue (in tens of billions of yuan)')
ax.set_xlabel('Company names')
ax.set_xticks(x)
ax.set_xticklabels(companies)
ax.legend()
ax.set_title('Top 10 A-share new energy vehicle manufacturing listed companies in China in terms of operating revenue in 2023')

# Adjust the x-axis range to leave space for growth rate labels
ax.set_xlim(-0.5, len(companies) + 1)

plt.tight_layout()
plt.show()