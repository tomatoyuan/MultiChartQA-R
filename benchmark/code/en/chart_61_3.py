import matplotlib.pyplot as plt
import numpy as np

# Data definition
months = ["Jan", "Feb", "Mar"]
years = ["2023", "2024", "2025"]
data = [
    [67.3, 64.1, 62.9],
    [67.2, 64.9, 63.3],
    [69.7, 66.9, 63.4]
]
growth_rates = ["YoY -1.9%", "YoY -2.5%", "YoY -5.1%"]
colors = ["#a5d65d", "#81c784", "#4bb7e6"]  # Match chart colors

# Create a canvas
fig, ax = plt.subplots(figsize=(8, 6))

# Draw a grouped bar chart
x = np.arange(len(months))
bar_width = 0.25
for i in range(3):
    ax.bar(x + i * bar_width, data[i], width=bar_width, color=colors[i], label=years[i], edgecolor='white')
    # Add data labels
    for j, val in enumerate(data[i]):
        ax.text(x[j] + i * bar_width, val - 3, f'{val}', ha='center', va='bottom', fontsize=9)

# Add year-on-year annotations
for i in range(3):
    ax.text(x[i] + 1 * bar_width, max(data[i]) + 2, growth_rates[i], ha='center', va='bottom', fontsize=10, color='blue')

# Beautify the settings
ax.set_title("mUserTracker-2023-2025Q1\nSingle-device daily usage times", fontsize=12, fontweight='bold')
ax.set_xticks(x + bar_width)
ax.set_xticklabels(months)
ax.legend()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()