import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2016", "2017", "2018", "2019", "2020", "2021e", "2022e", "2023e", "2024e", "2025e", "2026e"]
# Global vocational education market size (in billions of US dollars), the data can be approximately the same
market_size = [491, 520, 558, 585, 604, 647, 684, 720, 751, 779, 803]
# Year-on-year growth rate of the vocational education market (%), the data can be approximately the same
yoy = [5.8, 7.4, 4.7, 3.4, 7.0, 5.8, 5.2, 4.4, 3.7, 3.1]

# Create a canvas and subplots with a dual y-axis
fig, ax1 = plt.subplots(figsize=(10, 6))
ax2 = ax1.twinx()

ax1.set_ylim(0, 1600)
ax2.set_ylim(-5, 10)

# Draw a bar chart of the global vocational education market size
x = np.arange(len(years))
bar_width = 0.6
bars = ax1.bar(x, market_size, width=bar_width, color="#A4C639", label="Global Vocational Education Market Size (Billions of USD)")

# Draw a line chart of the year-on-year growth rate of the vocational education market (Note: The yoy data has one less value than the years because there is no growth rate comparison data for 2016, and here it corresponds to the years from 2017 onwards)
line_x = x[1:]  # The x-axis of the line chart corresponds to the years from 2017 to 2026e
line, = ax2.plot(line_x, yoy, marker='o', color="#64B5F6", label="Year-on-Year Growth Rate of Vocational Education Market (%)", linewidth=2)

# Add data labels to the global vocational education market size bar chart
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Adjust the label position
                textcoords="offset points",
                ha='center', va='bottom')

# Add data labels to the year-on-year growth rate line chart of the vocational education market
for x_val, y_val in zip(line_x, yoy):
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
ax1.set_ylabel("Global Vocational Education Market Size (Billions of USD)", color="#A4C639")
ax2.set_ylabel("Year-on-Year Growth Rate of Vocational Education Market (%)", color="#64B5F6")
# Set the title
ax1.set_title("Global Vocational Education Market Size and Growth Rate from 2016 to 2026", fontsize=14, fontweight="bold")

# Combine the legends
handles, labels = ax1.get_legend_handles_labels()
handles.append(line)
labels.append(line.get_label())
ax1.legend(handles, labels, loc='upper left')

# Beautify the chart by hiding the top and right borders (for both ax1 and ax2)
for spine in ["top", "right"]:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()