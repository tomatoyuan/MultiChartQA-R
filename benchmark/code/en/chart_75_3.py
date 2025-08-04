import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2017", "2018", "2019", "2020", "2021"]
# Consumption volume of green coffee beans (10,000 tons), the data can be approximately the same
bean_consumption = [13.5, 9.9, 12.9, 14.4, 21.9]
# Import volume of coffee products (10,000 tons), the data can be approximately the same
import_volume = [3.3, 3.6, 3.8, 4.0, 3.9]

# Fix: Ensure the lengths of the two growth rate data are the same (both are 1 less than the original data)
# Growth rate of green coffee bean consumption (%), the data can be approximately the same
bean_growth_rate = [-26.7, 30.3, 11.6, 52.1]  # Remove the first incorrect data point
# Growth rate of coffee product imports (%), the data can be approximately the same
import_growth_rate = [9.1, 5.6, 5.3, -2.5]

# Create a canvas and sub - plots with a dual y - axis
fig, ax1 = plt.subplots(figsize=(8, 6))
ax2 = ax1.twinx()

ax1.set_ylim(0, 40)
ax2.set_ylim(-200, 100)

# Draw the bar chart of green coffee bean consumption
x = np.arange(len(years))
bar_width = 0.35
bean_bars = ax1.bar(x - bar_width / 2, bean_consumption, width=bar_width, color="#A4C639", label="Consumption of green coffee beans (10,000 tons)")
# Draw the bar chart of coffee product import volume
import_bars = ax1.bar(x + bar_width / 2, import_volume, width=bar_width, color="#64B5F6", label="Import volume of coffee products (10,000 tons)")

# Draw the line chart of growth rates (starting from 2018 because there is no growth rate data for 2017)
growth_x = x[1:]  # Corresponds to 2018 - 2021
bean_growth_line, = ax2.plot(growth_x, bean_growth_rate, marker='o', color="#A4C639", label="Growth rate of green coffee bean consumption (%)", linewidth=2, linestyle='--')
import_growth_line, = ax2.plot(growth_x, import_growth_rate, marker='o', color="#64B5F6", label="Growth rate of coffee product imports (%)", linewidth=2, linestyle='--')

# Add data labels (bar chart)
for bar in bean_bars:
    height = bar.get_height()
    ax1.annotate(f'{height}',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom')

for bar in import_bars:
    height = bar.get_height()
    ax1.annotate(f'{height}',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom')

# Add data labels (line chart)
for x_val, y_val in zip(growth_x, bean_growth_rate):
    ax2.annotate(f'{y_val}%',
                 xy=(x_val, y_val),
                 xytext=(0, 5),
                 textcoords='offset points',
                 ha='center', va='bottom',
                 color="#A4C639")

for x_val, y_val in zip(growth_x, import_growth_rate):
    ax2.annotate(f'{y_val}%',
                 xy=(x_val, y_val),
                 xytext=(0, 5),
                 textcoords='offset points',
                 ha='center', va='bottom',
                 color="black")

# Set the axes and title
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.set_ylabel("Quantity (10,000 tons)", color="#333333")
ax2.set_ylabel("Growth rate (%)", color="#333333")
ax1.set_title("Consumption of green coffee beans and imported coffee products in China from 2017 to 2021", fontsize=14, fontweight="bold")

# Combine the legends
handles, labels = ax1.get_legend_handles_labels()
handles.extend([bean_growth_line, import_growth_line])
labels.extend([bean_growth_line.get_label(), import_growth_line.get_label()])
ax1.legend(handles, labels, loc='upper left')

# Beautify the chart
for spine in ["top", "right"]:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()