import matplotlib.pyplot as plt
import numpy as np

# Months
months = ["2021.4", "2021.5", "2021.6", "2021.7", "2021.8", "2021.9", "2021.10", "2021.11", "2021.12"]
# Monthly turnover index of beauty and hair care products on Tmall and Taobao (simulated data)
tmall_taobao = [1400000000, 1200000000, 2200000000, 1100000000, 1500000000, 1700000000, 1300000000, 3200000000, 1400000000]
# Monthly turnover index of beauty and hair care products on Tmall Global (simulated data)
tmall_global = [500000000, 500000000, 900000000, 400000000, 600000000, 600000000, 500000000, 1400000000, 500000000]
# Annual growth data
annual_growth = "+12.3%"
annual_growth_desc = "Annual turnover (index) growth of beauty and hair care market"

# Create a canvas
fig, ax = plt.subplots(figsize=(10, 6))

ax.set_ylim(0, 5000000000)

# Draw a line chart for Tmall and Taobao
ax.plot(months, tmall_taobao, marker='o', color="#A4C639", label="Monthly turnover index of beauty and hair care products on Tmall and Taobao", linewidth=2)
# Draw a line chart for Tmall Global
ax.plot(months, tmall_global, marker='o', color="#87CEEB", label="Monthly turnover index of beauty and hair care products on Tmall Global", linewidth=2)

# Add data labels (simplified, can be improved as needed)
for x, y in zip(months, tmall_taobao):
    ax.annotate(f'{y/1000000000:.1f} billion',
                xy=(x, y),
                xytext=(0, 5),
                textcoords="offset points",
                ha='center', va='bottom',
                color="#A4C639")
for x, y in zip(months, tmall_global):
    ax.annotate(f'{y/1000000000:.1f} billion',
                xy=(x, y),
                xytext=(0, 5),
                textcoords="offset points",
                ha='center', va='bottom',
                color="#87CEEB")

# Set the y-axis label
ax.set_ylabel("Turnover index")
# Set the title
ax.set_title("Trend of monthly turnover index of beauty and hair care products in China in 2021", fontsize=14, fontweight='bold')

# Add a legend
ax.legend(loc='upper right')

# Beautify: Hide the top and right borders
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()