import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2020", "2021", "2022e", "2023e", "2024e", "2025e"]
# Overall cloud service market size (in billions of yuan)
market_size = [2256, 3280, 4769, 6812, 9550, 12683]
# Overall cloud service market growth rate (%)
growth_rate = [39.9, 45.4, 42.8, 40.2, 32.8, 30.6]

# Create a canvas and sub - plots with a dual y - axis
fig, ax1 = plt.subplots(figsize=(8, 6))
ax2 = ax1.twinx()

ax1.set_ylim(0, 26000)
ax2.set_ylim(0, 55)

# Draw a bar chart of the overall cloud service market size
x = np.arange(len(years))
bar_width = 0.6
bars = ax1.bar(x, market_size, width=bar_width, color="#A4C639", label="Overall cloud service market size (in billions of yuan)")

# Draw a line chart of the overall cloud service market growth rate
line, = ax2.plot(x, growth_rate, marker='o', color="#64B5F6", label="Overall cloud service market growth rate (%)", linewidth=2)

# Add data labels for the market size
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),  # Adjust the label position
                 textcoords="offset points",
                 ha='center', va='bottom')

# Add data labels for the growth rate
for x_val, y_val in zip(x, growth_rate):
    ax2.annotate(f'{y_val}%',
                 xy=(x_val, y_val),
                 xytext=(0, 5),  # Adjust the label position
                 textcoords='offset points',
                 ha='center', va='bottom',
                 color="#64B5F6")

# Set the x - axis ticks and labels
ax1.set_xticks(x)
ax1.set_xticklabels(years)
# Set the y - axis labels
ax1.set_ylabel("Overall cloud service market size (in billions of yuan)", color="#A4C639")
ax2.set_ylabel("Overall cloud service market growth rate (%)", color="#64B5F6")
# Set the title
ax1.set_title("Cloud Consensus: China's Overall Cloud Service Market Size and Growth Rate from 2020 to 2025", fontsize=14, fontweight="bold")

# Combine the legends
handles, labels = ax1.get_legend_handles_labels()
handles.append(line)
labels.append(line.get_label())
ax1.legend(handles, labels, loc='upper left')

# Beautify the chart by hiding the top and right borders (for ax1 and ax2)
for spine in ["top", "right"]:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()