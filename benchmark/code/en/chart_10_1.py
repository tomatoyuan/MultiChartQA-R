import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np

# Data is directly placed in the list (date format: 'YYYY-MM-DD', values are full values)
dates = ['2025-05-01', '2025-05-02', '2025-05-03', '2025-05-04', '2025-05-05', '2025-05-06', '2025-05-07', '2025-05-08', '2025-05-09', '2025-05-10', '2025-05-11', '2025-05-12', '2025-05-13', '2025-05-14', '2025-05-15', '2025-05-16', '2025-05-17', '2025-05-18', '2025-05-19', '2025-05-20', '2025-05-21', '2025-05-22', '2025-05-23', '2025-05-24', '2025-05-25', '2025-05-26', '2025-05-27', '2025-05-28', '2025-05-29', '2025-05-30', '2025-05-31']
search_attention = [6200000, 6500000, 7000000, 9700000, 9500000, 8500000, 7200000, 9500000, 9500000, 9500000, 9500000, 9300000, 8800000, 7800000, 9000000, 10200000, 9800000, 9500000, 9200000, 8500000, 7800000, 7800000, 9000000, 9500000, 9500000, 9300000, 8800000, 7800000, 8500000, 9000000, 9500000]

# Convert date strings to datetime objects
dates = [datetime.strptime(date, '%Y-%m-%d') for date in dates]

# Create a canvas and a sub - plot, increase the chart size
fig, ax = plt.subplots(figsize=(15, 7))

# Set the background style
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#ffffff')

# Draw a line chart, add transparency and marker points
line, = ax.plot(dates, search_attention, color='#1f77b4', linewidth=2.5, alpha=0.8, marker='o', markersize=5, markevery=3)

# Add a filled area
ax.fill_between(dates, search_attention, 0, color='#1f77b4', alpha=0.1)

# Set the x - axis to date format, display a tick every 3 days
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=3))

# Set the chart title and axis labels, increase the font size and style
ax.set_title('May Search Attention Trend in Vocational Training Industry', fontsize=20, pad=20, fontweight='bold')
ax.set_ylabel('Search Attention', fontsize=16, labelpad=15)
ax.set_xlabel('Date', fontsize=16, labelpad=15)

# Set the y - axis tick range and format, add thousands separators
ax.set_ylim(0, 12000000)
ax.yaxis.set_major_formatter(lambda x, pos: f'{int(x):,}')

# Add grid lines and set the style
ax.grid(True, linestyle='--', alpha=0.5, color='#cccccc')

# Customize the tick label font size
ax.tick_params(axis='both', which='major', labelsize=12)

# Let the x - axis dates automatically adjust the spacing to avoid overlap
fig.autofmt_xdate(rotation=45, ha='right')

# Add annotations for the maximum and minimum values
max_val = max(search_attention)
min_val = min(search_attention)
max_idx = search_attention.index(max_val)
min_idx = search_attention.index(min_val)

ax.annotate(f'Peak: {max_val:,}',
            xy=(dates[max_idx], max_val),
            xytext=(dates[max_idx], max_val + 500000),
            arrowprops=dict(facecolor='red', shrink=0.05, width=1.5, headwidth=8),
            fontsize=12,
            ha='center')

ax.annotate(f'Trough: {min_val:,}',
            xy=(dates[min_idx], min_val),
            xytext=(dates[min_idx], min_val - 1000000),
            arrowprops=dict(facecolor='green', shrink=0.05, width=1.5, headwidth=8),
            fontsize=12,
            ha='center')

# Add a legend
ax.legend([line], ['Search Attention'], loc='upper left', fontsize=12)

# Add a watermark
fig.text(0.85, 0.15, 'Data Source: Industry Report', fontsize=10, color='gray', alpha=0.7, ha='right')

# Optimize the layout
plt.tight_layout()

# Display the chart
plt.show()