import matplotlib.pyplot as plt
import numpy as np

# Country names
countries = [
    "European Union", "United States", "Japan", "Russia", "Canada", "South Korea",
    "Algeria", "Australia", "Turkey", "Ukraine", "Saudi Arabia", "Switzerland",
    "Brazil", "Indonesia", "Ethiopia", "Philippines", "Vietnam", "Mexico",
    "Colombia", "India", "Thailand", "Venezuela"
]
# Coffee consumption in coffee - importing countries (thousands of bags), data can be approximately the same
import_consumption = [40251, 26982, 7386, 4681, 4011, 2513,
                      2131, 1962, 1754, 1379, 1253, 1074,
                      0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0]
# Coffee consumption in coffee - exporting countries (thousands of bags), data can be approximately the same
export_consumption = [0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0,
                      22400, 5000, 3798, 3312, 2700, 2420,
                      2045, 1485, 1415, 1100]

# Position settings for grouped bar charts
x = np.arange(len(countries))
bar_width = 0.35

# Create a canvas and sub - plots
fig, ax = plt.subplots(figsize=(10, 8))

# Draw the bar chart for coffee consumption in coffee - importing countries
import_bars = ax.barh(x - bar_width/2, import_consumption, height=bar_width, 
                      color="#C6C439", label="Coffee green bean consumption in coffee - importing countries (thousands of bags)")
# Draw the bar chart for coffee consumption in coffee - exporting countries
export_bars = ax.barh(x + bar_width/2, export_consumption, height=bar_width, 
                      color="#AD64F6", label="Coffee green bean consumption in coffee - exporting countries (thousands of bags)")

# Add data labels for consumption in importing countries
for bar in import_bars:
    width = bar.get_width()
    if width > 0:
        ax.annotate(f'{width}',
                    xy=(width, bar.get_y() + bar.get_height() / 2),
                    xytext=(5, 0),  # Adjust the label position
                    textcoords="offset points",
                    ha='left', va='center')

# Add data labels for consumption in exporting countries
for bar in export_bars:
    width = bar.get_width()
    if width > 0:
        ax.annotate(f'{width}',
                    xy=(width, bar.get_y() + bar.get_height() / 2),
                    xytext=(5, 0),  # Adjust the label position
                    textcoords="offset points",
                    ha='left', va='center')

# Set the y - axis ticks and labels
ax.set_yticks(x)
ax.set_yticklabels(countries)
# Set the x - axis label
ax.set_xlabel("Consumption (thousands of bags)")
# Set the title
ax.set_title("Global coffee green bean consumption in major countries in 2020", fontsize=14, fontweight="bold")

# Add a legend
ax.legend()

# Beautify the chart, hide the top, right, and bottom borders
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()