import matplotlib.pyplot as plt
import numpy as np

# Simulated data (consistent with the original graph trend and approximate in values)
cities = [
    "Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Tianjin", 
    "Shenyang", "Dalian", "Nanjing", "Hangzhou", "Qingdao", 
    "Wuhan", "Chongqing", "Chengdu", "Xi'an"
]
stock = np.array([849, 833.3, 561.7, 637.8, 238.5, 121.2, 98.1, 237.8, 230.7, 160.1, 257.2, 182.9, 270.4, 280.8])  # Stock
net_absorption = np.array([34.1, 53.1, 42.6, 64.1, 12.9, 3.5, 2.4, 22.2, 6.4, 9.7, 17.1, 11.3, 19.7, 12.6])  # Net absorption
vacancy_rate = np.array([10, 10, 8, 19, 29, 33, 32, 22, 16, 24, 35, 28, 13, 22])  # Vacancy rate

# Initialize the canvas (width and height match the original graph)
fig, ax1 = plt.subplots(figsize=(12, 6))
ax2 = ax1.twinx()  # Dual axes

# Draw bar charts (stock + net absorption)
x = np.arange(len(cities))
width = 0.6
# Stock bar chart
rects_stock = ax1.bar(x, stock, width, label="2021 Core business district stock (10,000 square meters)", color="#8BC34A")
# Net absorption bar chart (stacked at the bottom of the stock, use a smaller size to simulate the "blue bar")
rects_absorption = ax1.bar(x, net_absorption, width, bottom=0, label="2021 Core business district net absorption (10,000 square meters)", color="#42A5F5")

# Draw a line chart (vacancy rate)
line_vacancy, = ax2.plot(x, vacancy_rate, marker="o", color="#7CB342", label="2021 Core business district vacancy rate (%)", linewidth=2)

# Add data labels (stock, net absorption, vacancy rate)
for rect in rects_stock:
    height = rect.get_height()
    ax1.annotate(f'{height}', 
                 xy=(rect.get_x() + rect.get_width()/2, height),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom', fontsize=9)
for rect in rects_absorption:
    height = rect.get_height()
    ax1.annotate(f'{height}', 
                 xy=(rect.get_x() + rect.get_width()/2, height/2 + 5),  # Label in the middle of the blue bar
                 xytext=(0, 0),
                 textcoords="offset points",
                 ha='center', va='center', fontsize=9, color='white')
for i, rate in enumerate(vacancy_rate):
    ax2.annotate(f'{rate}%', 
                 xy=(x[i], rate),
                 xytext=(0, 5),
                 textcoords="offset points",
                 ha='center', va='bottom', fontsize=9, color="black")

# Axis and legend configuration
ax1.set_xticks(x)
ax1.set_xticklabels(cities, fontsize=10, rotation=45)
ax1.set_ylabel("Stock/Net absorption (10,000 square meters)", fontsize=11, color="#8BC34A")
ax2.set_ylabel("Vacancy rate (%)", fontsize=11, color="#7CB342")

# Combine legends (solve the problem of overlapping legends on dual axes)
handles, labels = ax1.get_legend_handles_labels()
handles.append(line_vacancy)
labels.append(line_vacancy.get_label())
ax1.legend(handles, labels, loc="upper left", bbox_to_anchor=(0, 1.05), ncol=3, fontsize=9)

# Title and beautification
plt.title("2021 Grade A office building market scale and vacancy rate in core business districts of major first - and second - tier cities in China", fontsize=14, pad=20)
ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)
plt.tight_layout()

# Display the chart
plt.show()