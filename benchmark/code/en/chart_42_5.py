import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Build data
data = {
    'Month': ['202401', '202402', '202403', '202404', '202405', '202406', 
              '202407', '202408', '202409', '202410', '202411', '202412', '202501'],
    'Sales (Billion)': [8, 7, 10, 9, 11, 10, 9, 9, 10, 13, 12, 9, 10],
    'Average Transaction Price': [10, 11, 7, 8, 8, 8, 4, 6, 9, 10, 10, 8, 10]
}
df = pd.DataFrame(data)

# Convert the month to date format for better display
df['Date'] = df['Month'].apply(lambda x: datetime.strptime(x, '%Y%m'))

# Create a dual - axis chart
fig, ax1 = plt.subplots(figsize=(14, 7))  # Increase the chart size
ax2 = ax1.twinx()

# Set the chart background and grid
fig.patch.set_facecolor('#f8f9fa')  # Light gray background
ax1.set_facecolor('#ffffff')  # White plotting area
ax1.grid(True, linestyle='--', alpha=0.7)  # Add grid lines

# Draw the sales bar chart - use gradient color and shadow effect
bar_width = 0.6
bars = ax1.bar(df['Date'], df['Sales (Billion)'], width=bar_width, 
               color='#3274A1', edgecolor='#285F8F', alpha=0.9, 
               label='Sales (Billion)', zorder=3)  # zorder controls the layer order

# Add numerical labels to the bar chart
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 0.15,
             f'{height}', ha='center', va='bottom', fontsize=9)

# Draw the average transaction price line chart - use a smooth curve and marker points
line, = ax2.plot(df['Date'], df['Average Transaction Price'], color='#E1812C', 
                label='Average Transaction Price', linewidth=2.5, marker='o', markersize=7,
                markeredgecolor='white', markeredgewidth=1, zorder=4)

# Add numerical labels to the line chart
for x, y in zip(df['Date'], df['Average Transaction Price']):
    ax2.annotate(f'{y}', (x, y), textcoords='offset points',
                xytext=(0, 8), ha='center', fontsize=9)

# Set the axis labels and title
ax1.set_xlabel('Month', fontsize=12)
ax1.set_ylabel('Sales (Billion)', color='#3274A1', fontsize=12)
ax2.set_ylabel('Average Transaction Price', color='#E1812C', fontsize=12)

# Set the title and subtitle
plt.suptitle('Monthly Sales of Health Food - Related Industries in 2024', fontsize=16, fontweight='bold', y=0.96)
plt.title('*Some mainstream shelf - e - commerce and content - e - commerce platforms', fontsize=11, color='#666666', y=1.02)

# Format the x - axis date display
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
ax1.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
plt.xticks(rotation=45, ha='right', fontsize=10)

# Set the y - axis range
ax1.set_ylim(0, max(df['Sales (Billion)']) * 1.1)  # Leave 10% space
ax2.set_ylim(0, max(df['Average Transaction Price']) * 1.1)

# Add a legend - use a better position and style
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, 
          loc='upper center', bbox_to_anchor=(0.5, -0.08),
          ncol=2, frameon=True, fancybox=True, shadow=True,
          fontsize=10)

# Add an annotation - highlight the month with the highest sales
max_sales_idx = df['Sales (Billion)'].idxmax()
ax1.annotate('Peak Sales', xy=(df['Date'][max_sales_idx], df['Sales (Billion)'][max_sales_idx]),
            xytext=(20, 30), textcoords='offset points',
            arrowprops=dict(arrowstyle='->', color='black'),
            fontsize=10)

# Adjust the layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Leave space for the bottom and top text

# Display the chart
plt.show()