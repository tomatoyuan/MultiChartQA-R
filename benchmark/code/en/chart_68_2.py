import matplotlib.pyplot as plt
import numpy as np

# Simulated data (consistent with the trend of the original graph)
years = ["2017", "2018", "2019", "2020", "2021", "2022e", "2023e", "2024e"]
market_size = np.array([2, 4, 8, 15, 16, 18, 22, 30])  # Market size (in billions of yuan)
growth_rate = np.array([136.6, 101.1, 89.4, 10.3, 12.0, 23.7, 33.4])  # Growth rate (%), note that the length is 1 less than years (no growth rate for 2017)

# Initialize a dual-axis canvas
fig, ax1 = plt.subplots(figsize=(12, 6))
ax2 = ax1.twinx()

# Draw a bar chart (market size)
x = np.arange(len(years))
bar_width = 0.6
rects = ax1.bar(x, market_size, width=bar_width, label="China's Real - Time Audio and Video (RTC) PaaS Market Size (in billions of yuan)", color="#A4C639")

# Draw a line chart (growth rate)
line, = ax2.plot(x[1:], growth_rate, marker="o", color="#42A5F5", label="China's Real - Time Audio and Video (RTC) PaaS Market Size Growth Rate", linewidth=2)

# Add market size annotations (on top of the bar chart)
for rect in rects:
    height = rect.get_height()
    ax1.annotate(f'{height}', 
                 xy=(rect.get_x() + rect.get_width()/2, height),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom', fontsize=9)

# Add growth rate annotations (above the points of the line chart)
for i, rate in enumerate(growth_rate):
    ax2.annotate(f'{rate}%', 
                 xy=(x[i+1], rate),  # x starts from 2018 (index 1)
                 xytext=(0, 5),
                 textcoords="offset points",
                 ha='center', va='bottom', fontsize=9, color="#42A5F5")

# Add CAGR annotations (manually simulate arrows and text)
ax1.annotate(
    "CAGR=77.6%", 
    xy=(0.2, 0.8), xycoords="axes fraction",
    xytext=(0.2, 0.9), textcoords="axes fraction",
    arrowprops=dict(facecolor='gray', width=1, headwidth=6),
    fontsize=10, ha='center'
)
ax1.annotate(
    "CAGR=28.4%", 
    xy=(0.7, 0.8), xycoords="axes fraction",
    xytext=(0.7, 0.9), textcoords="axes fraction",
    arrowprops=dict(facecolor='gray', width=1, headwidth=6),
    fontsize=10, ha='center'
)

# Axes and legend configuration
ax1.set_xticks(x)
ax1.set_xticklabels(years, fontsize=10)
ax1.set_ylabel("Market Size (in billions of yuan)", fontsize=11, color="#A4C639")
ax2.set_ylabel("Growth Rate (%)", fontsize=11, color="#42A5F5")

# Combine legends (solve the problem of overlapping legends on dual - axes)
handles, labels = ax1.get_legend_handles_labels()
handles.append(line)
labels.append(line.get_label())
ax1.legend(handles, labels, loc="upper left", bbox_to_anchor=(0, 1.09), ncol=2, fontsize=9)

# Title and beautification
plt.title("China's Real - Time Audio and Video (RTC) PaaS Market Size and Forecast from 2017 to 2024", fontsize=14, pad=30)
ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)
plt.tight_layout()

# Display the chart
plt.show()