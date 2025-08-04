import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2017", "2018", "2019", "2020", "2021"]
# Yunnan Province's green coffee bean production (in 10,000 tons), the data can be approximately the same
production = [16.5, 15.1, 14.5, 13.5, 14.0]
# Production growth rate (%), the data can be approximately the same
growth_rate = [-8.2, -4.1, -6.8, 3.8]

# Create a canvas and subplots with a dual y-axis
fig, ax1 = plt.subplots(figsize=(8, 6))
ax2 = ax1.twinx()

ax1.set_ylim(0, 32)
ax2.set_ylim(-40, 20)

# Draw a bar chart of green coffee bean production
x = np.arange(len(years))
bar_width = 0.6
bars = ax1.bar(x, production, width=bar_width, color="#A4C639", label="Yunnan Province's green coffee bean production (10,000 tons)")

# Draw a line chart of production growth rate (Note: There is one less growth rate data point than the number of years because there is no growth rate comparison data for 2017, so it starts corresponding from 2018)
line_x = x[1:]  # The x-axis of the line chart corresponds to the years from 2018 to 2021
line, = ax2.plot(line_x, growth_rate, marker='o', color="#64B5F6", label="Yunnan Province's green coffee bean production growth rate (%)", linewidth=2)

# Add production data labels
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),  # Adjust the label position
                 textcoords="offset points",
                 ha='center', va='bottom')

# Add growth rate data labels
for x_val, y_val in zip(line_x, growth_rate):
    ax2.annotate(f'{y_val}%',
                 xy=(x_val, y_val),
                 xytext=(0, 5),  # Adjust the label position
                 textcoords='offset points',
                 ha='center', va='bottom',
                 color="#64B5F6")

# Set x-axis ticks and labels
ax1.set_xticks(x)
ax1.set_xticklabels(years)
# Set y-axis labels
ax1.set_ylabel("Yunnan Province's green coffee bean production (10,000 tons)", color="#A4C639")
ax2.set_ylabel("Yunnan Province's green coffee bean production growth rate (%)", color="#64B5F6")
# Set the title
ax1.set_title("Yunnan Province's green coffee bean production in China from 2017 to 2021", fontsize=14, fontweight="bold")

# Combine legends
handles, labels = ax1.get_legend_handles_labels()
handles.append(line)
labels.append(line.get_label())
ax1.legend(handles, labels, loc='upper left')

# Beautify the chart, hide the top and right borders (for ax1 and ax2)
for spine in ["top", "right"]:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()