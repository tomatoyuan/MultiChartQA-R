import matplotlib.pyplot as plt
import numpy as np

# Years
years = np.arange(2011, 2022)
# Total logistics cost (trillion)
logistics_cost = [8.4, 9.4, 10.2, 10.6, 10.8, 11.1, 12.1, 13.3, 14.6, 14.9, 16.7]
# Proportion of GDP (%)
gdp_ratio = [17.2, 17.4, 17.1, 16.5, 15.7, 14.9, 14.7, 14.8, 14.7, 14.7, 14.6]

# Create a canvas with a secondary y - axis
fig, ax1 = plt.subplots(figsize=(10, 6))
ax2 = ax1.twinx()

ax1.set_ylim(0, 32)
ax2.set_ylim(5, 20)

# Draw a bar chart for total logistics cost
ax1.bar(years, logistics_cost, width=0.6, color="#C63982", label="Total logistics cost (trillion)")
# Draw a line chart for the proportion of GDP
ax2.plot(years, gdp_ratio, marker='o', color="#64B5F6", label="Proportion of GDP (%)", linewidth=2)

# Add data labels to the bar chart
for x, y in zip(years, logistics_cost):
    ax1.annotate(f'{y}',
                 xy=(x, y),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom')

# Add data labels to the line chart
for x, y in zip(years, gdp_ratio):
    ax2.annotate(f'{y}%',
                 xy=(x, y),
                 xytext=(0, 5),
                 textcoords="offset points",
                 ha='center', va='bottom',
                 color="#64B5F6")

# Set axis labels and title
ax1.set_xlabel("Year")
ax1.set_ylabel("Total logistics cost (trillion)", color="#C63982")
ax2.set_ylabel("Proportion of GDP (%)", color="#64B5F6")
ax1.set_title("Total logistics cost and its proportion of GDP in China from 2011 to 2021", fontsize=14, fontweight="bold")

# Set x - axis ticks
ax1.set_xticks(years)
ax1.set_xticklabels(years)

# Combine legends
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(handles1 + handles2, labels1 + labels2, loc='upper left')

# Beautify the chart by hiding the top and right borders
for spine in ["top", "right"]:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()