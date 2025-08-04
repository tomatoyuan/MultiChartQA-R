import matplotlib.pyplot as plt
import numpy as np

# Date data, represented by strings for subsequent display processing
dates = [f"May {i}" for i in range(1, 32)]
# Approximate daily search attention data (read from the graph, just an example, adjust according to actual situation)
values = [60000, 57000, 62000, 80000, 100000, 90000, 95000, 90000, 80000, 70000, 
          65000, 45000, 60000, 58000, 55000, 48000, 52000, 50000, 47000, 55000, 
          70000, 55000, 65000, 70000, 75000, 78000, 78000, 78000, 80000, 82000, 85000]

# Set the positions of the x - axis
x = np.arange(len(dates))  

fig, ax = plt.subplots(figsize=(14, 7))  # Adjust the chart size
# Draw a line chart and add marker points
line, = ax.plot(x, values, color='blue', marker='o', markersize=4)  

# Set the x - axis labels, display every three days
xtick_indices = np.arange(0, len(dates), 3)  # Take indices every 3 steps
xtick_labels = [dates[i] for i in xtick_indices]
ax.set_xticks(xtick_indices)
ax.set_xticklabels(xtick_labels)  

# Add data annotations
for i, (date, value) in enumerate(zip(dates, values)):
    # For the first 10 data points, annotate above; for the next 10, annotate below to avoid going out of the chart
    if i < 10:
        ax.annotate(f'{value:,}',
                    xy=(i, value),
                    xytext=(0, 10),  # 10 points vertical offset
                    textcoords="offset points",
                    ha='center',
                    va='bottom',
                    rotation=0,
                    fontsize=8)
    elif i < 20:
        ax.annotate(f'{value:,}',
                    xy=(i, value),
                    xytext=(0, -10),  # 10 points vertical offset
                    textcoords="offset points",
                    ha='center',
                    va='top',
                    rotation=0,
                    fontsize=8)
    else:
        ax.annotate(f'{value:,}',
                    xy=(i, value),
                    xytext=(0, 10),  # 10 points vertical offset
                    textcoords="offset points",
                    ha='center',
                    va='bottom',
                    rotation=0,
                    fontsize=8)

# Set axis titles, etc.
ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Search Attention', fontsize=12)
ax.set_title('Search Attention Trend of Divorce Litigation Industry in May', fontsize=14)

# Add grid lines
ax.grid(True, linestyle='--', alpha=0.7)

# Adjust the Y - axis range to leave space for annotations
y_min, y_max = ax.get_ylim()
ax.set_ylim(y_min - 5000, y_max + 5000)

plt.tight_layout()  # Ensure all elements fit within the chart area
plt.show()