import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2016", "2017", "2018", "2019", "2020", "2021e"]
# "New Three" economic scale (in billions of yuan), the data can be approximately the same
economic_scale = [113719, 129578, 145369, 161927, 169254, 197170]
# Proportion in GDP (%), the data can be approximately the same
gdp_ratio = [15.3, 15.7, 16.1, 16.3, 17.1, 17.2]

# Create a canvas and subplots with a dual y-axis
fig, ax1 = plt.subplots(figsize=(8, 6))
ax2 = ax1.twinx()

ax1.set_ylim(0, 400000)
ax2.set_ylim(10, 18)

# Draw a bar chart of the "New Three" economic scale
x = np.arange(len(years))
bar_width = 0.6
bars = ax1.bar(x, economic_scale, width=bar_width, color="#A4C639", label="\"New Three\" Economic Scale (in billions of yuan)")

# Draw a line chart of the proportion in GDP
line, = ax2.plot(x, gdp_ratio, marker='o', color="#64B5F6", label="Proportion in GDP (%)", linewidth=2)

# Add data labels for the "New Three" economic scale
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),  # Adjust the label position
                 textcoords="offset points",
                 ha='center', va='bottom')

# Add data labels for the proportion in GDP
for x_val, y_val in zip(x, gdp_ratio):
    ax2.annotate(f'{y_val}%',
                 xy=(x_val, y_val),
                 xytext=(0, 5),  # Adjust the label position
                 textcoords='offset points',
                 ha='center', va='bottom',
                 color="#64B5F6")

# Set the x-axis ticks and labels
ax1.set_xticks(x)
ax1.set_xticklabels(years)
# Set the y-axis labels
ax1.set_ylabel("\"New Three\" Economic Scale (in billions of yuan)", color="#A4C639")
ax2.set_ylabel("Proportion in GDP (%)", color="#64B5F6")
# Set the title
ax1.set_title("China's New Economy Scale and Proportion in GDP from 2016 to 2021", fontsize=14, fontweight="bold")

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