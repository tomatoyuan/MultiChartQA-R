import matplotlib.pyplot as plt
import numpy as np

# Date list
dates = ["5/1", "5/2", "5/3", "5/4", "5/5", "5/6", "5/7", "5/8", "5/9", "5/10", 
         "5/11", "5/12", "5/13", "5/14", "5/15", "5/16", "5/17", "5/18", "5/19", 
         "5/20", "5/21", "5/22", "5/23", "5/24", "5/25", "5/26", "5/27", "5/28", 
         "5/29", "5/30", "5/31"]
# Legal service search volume (bar chart, left - axis)
legal_service = [1200000, 1100000, 1200000, 1300000, 1400000, 1800000, 2000000, 
                 1900000, 1950000, 1900000, 1800000, 1850000, 1500000, 
                 1400000, 1300000, 1800000, 1700000, 1750000, 1400000, 
                 1350000, 1300000, 2200000, 1200000, 1350000, 1800000, 
                 1850000, 1900000, 1500000, 1400000, 1450000, 2000000]
# Property dispute proportion (approximate %) list
property_dispute = [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 
                    0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 
                    0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.5]
# Divorce lawsuit proportion (approximate %) list
divorce_lawsuit = [5.2, 5.0, 4.9, 4.8, 4.7, 4.6, 5.5, 5.0, 4.6, 4.5, 
                   4.4, 4.3, 3.2, 3.3, 3.4, 3.5, 3.4, 3.3, 3.0, 3.1, 
                   3.2, 5.0, 4.5, 4.0, 3.2, 3.3, 3.4, 4.5, 4.3, 4.2, 4.0]

# Create a canvas and dual - axes
fig, ax1 = plt.subplots(figsize=(14, 8))  # Primary axis (left - axis)
ax2 = ax1.twinx()  # Secondary axis (right - axis, proportion)

# Draw legal service (bar chart, left - axis)
x = np.arange(len(dates))  # X - coordinate index
bars = ax1.bar(x, legal_service, color='blue', label='Legal Service', width=0.6)
ax1.set_ylabel('Search Volume', color='blue', fontsize=12)
ax1.set_ylim(0, 2500000)  # Match the left - axis range of the original figure
ax1.tick_params(axis='y', labelcolor='blue')

# Draw property dispute and divorce lawsuit (line chart, right - axis)
line1, = ax2.plot(x, property_dispute, color='orange', label='Property Dispute', marker='o', linestyle='-', linewidth=2)
line2, = ax2.plot(x, divorce_lawsuit, color='green', label='Divorce Lawsuit', marker='o', linestyle='-', linewidth=2)
ax2.set_ylabel('Proportion (%)', color='black', fontsize=12)
ax2.set_ylim(0, 6)  # Match the right - axis range of the original figure (0% - 6%)
ax2.tick_params(axis='y', labelcolor='black')

# X - coordinate and legend settings
ax1.set_xticks(x)
ax1.set_xticklabels(dates, rotation=45, fontsize=10)  # Tilt the dates to avoid overlap
ax1.set_title('May Search Attention Trend of Legal Service Industry and Proportion of Sub - industries', fontsize=14, pad=20)

# Add data labels to the bar chart (search volume)
for i, bar in enumerate(bars):
    height = bar.get_height()
    # Display labels every 3 days to avoid over - crowding
    if i % 3 == 0:
        ax1.annotate(f'{height:,}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 5),  # Offset upward by 5 points
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=9,
                    color='blue',
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="blue", alpha=0.7))

# Add data labels to the property dispute line chart
for i, (x_val, y_val) in enumerate(zip(x, property_dispute)):
    # Only label points with changes and key nodes
    if y_val != 0.3 or i % 7 == 0 or i == len(x)-1:
        ax2.annotate(f'{y_val}%',
                    xy=(x_val, y_val),
                    xytext=(0, -15),  # Offset downward
                    textcoords="offset points",
                    ha='center', va='top',
                    fontsize=9,
                    color='orange',
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="orange", alpha=0.7))

# Add data labels to the divorce lawsuit line chart
for i, (x_val, y_val) in enumerate(zip(x, divorce_lawsuit)):
    # Only label peaks, valleys, and key nodes
    if i == 0 or i == len(x)-1 or i % 5 == 0 or \
       (i > 0 and i < len(x)-1 and 
        (y_val > divorce_lawsuit[i-1] and y_val > divorce_lawsuit[i+1]) or 
        (y_val < divorce_lawsuit[i-1] and y_val < divorce_lawsuit[i+1])):
        ax2.annotate(f'{y_val}%',
                    xy=(x_val, y_val),
                    xytext=(0, 10),  # Offset upward
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=9,
                    color='green',
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="green", alpha=0.7))

# Combine legends (display legends of dual - axes together)
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left', fontsize=10)

# Add grid lines to improve readability
ax1.grid(True, linestyle='--', alpha=0.3)

# Optimize the layout
plt.tight_layout()
plt.show()