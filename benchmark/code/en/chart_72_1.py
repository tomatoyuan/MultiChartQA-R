import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2017", "2018", "2019", "2020", "2021", "2022e", "2023e", "2024e"]
# Maternal and infant consumption scale (in billions of yuan)
market_size = [23613, 26593, 29919, 31231, 34591, 37552, 40505, 43554]
# Growth rate (%)
growth_rate = [12.4, 12.6, 12.5, 4.4, 10.8, 8.6, 7.9, 7.5]

# Create a canvas and subplots with a dual y - axis
fig, ax1 = plt.subplots(figsize=(8, 6))
ax2 = ax1.twinx()

ax1.set_ylim(0, 100000)
ax2.set_ylim(0, 12)

# Draw a bar chart of the maternal and infant consumption scale
x = np.arange(len(years))
bar_width = 0.6
bars = ax1.bar(x, market_size, width=bar_width, color="#A4C639", label="Maternal and infant consumption scale (in billions of yuan)")

# Draw a line chart of the growth rate
line, = ax2.plot(x, growth_rate, marker='o', color="#64B5F6", label="Growth rate(%)", linewidth=2)

# Add data labels for the maternal and infant consumption scale
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
ax1.set_ylabel("Maternal and infant consumption scale (in billions of yuan)", color="#A4C639")
ax2.set_ylabel("Growth rate(%)", color="#64B5F6")
# Set the title
ax1.set_title("China's maternal and infant consumption scale and growth rate from 2017 to 2024", fontsize=14, fontweight="bold")

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