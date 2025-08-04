import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]
# China's financing scale (in billions of yuan), the data can be approximately the same
china = [0, 0, 0, 0, 0, 0, 0, 10, 30, 0]  # Sample data, can be adjusted according to actual situation
# Overseas financing scale (in billions of yuan), the data can be approximately the same
overseas = [1, 10, 7, 21, 11, 31, 55, 71, 277, 75]  # Sample data, can be adjusted according to actual situation

# Create a figure and a sub - plot
fig, ax = plt.subplots(figsize=(10, 6))

# Draw a grouped bar chart (China and overseas stacked)
x = np.arange(len(years))
bar_width = 0.6
# First draw overseas (blue)
overseas_bars = ax.bar(x, overseas, width=bar_width, color="#64B5F6", label="Overseas financing scale (in billions of yuan)")
# Then draw China (green, stacked on top of overseas)
china_bars = ax.bar(x, china, width=bar_width, color="#C68439", label="China's financing scale (in billions of yuan)")

# Add data labels (overseas)
for bar in overseas_bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Adjust the label position
                textcoords="offset points",
                ha='center', va='bottom')

# Add data labels (China)
for bar in china_bars:
    height = bar.get_height()
    if height > 0:
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # Adjust the label position
                    textcoords="offset points",
                    ha='center', va='bottom',
                    color='white')

# Set x - axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(years)
# Set y - axis label
ax.set_ylabel("Financing scale (in billions of yuan)")
# Set the title
ax.set_title("Global enterprise digital learning industry financing scale from 2013 to H1 2022", fontsize=14, fontweight="bold")

# Add a legend
ax.legend()

# Beautify the chart, hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()