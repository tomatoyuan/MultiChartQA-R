import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Hourly search heat data (unit: ten thousand)
hours = list(range(25))  # 0 - 24 hours
heat_data = [
    1100, 1100, 1100, 1100, 1100,  # 0 - 4 hours
    1500, 2000, 2800, 3200, 2800,  # 5 - 9 hours
    2300, 2000, 1800, 2200, 2700,  # 10 - 14 hours
    3000, 3100, 2800, 2200, 1600,  # 15 - 19 hours
    1200, 1250, 1320, 1200, 1100   # 20 - 24 hours
]

# Create a canvas and sub - plot
fig, ax = plt.subplots(figsize=(14, 7), facecolor='#f8f9fa')
ax.set_facecolor('#f8f9fa')

# Use cubic spline interpolation to generate a smooth curve
x_smooth = np.linspace(min(hours), max(hours), 500)
spl = make_interp_spline(hours, heat_data, k=3)
heat_smooth = spl(x_smooth)

# Plot the smooth curve and add gradient - colored fill
line, = ax.plot(x_smooth, heat_smooth, linestyle='-', color='#1a73e8', linewidth=3)
ax.fill_between(x_smooth, heat_smooth, 0, alpha=0.1, color='#1a73e8')

# Add reference horizontal lines and optimize the line style
ax.axhline(y=1100, color='#9aa0a6', linestyle='--', alpha=0.7, linewidth=1.5)
ax.axhline(y=3300, color='#9aa0a6', linestyle='--', alpha=0.7, linewidth=1.5)

# Add title and labels, optimize font and position
ax.set_title('24 - hour trend chart of World Cup search heat', fontsize=18, pad=20, fontweight='bold', color='#202124')
ax.set_xlabel('Time (hours)', fontsize=14, labelpad=10, color='#3c4043')
ax.set_ylabel('Search heat (ten thousand)', fontsize=14, labelpad=10, color='#3c4043')

# Set x - axis ticks and optimize the display format
ax.set_xticks(hours[::4])
ax.set_xticklabels([f'{h}h' for h in hours[::4]], fontsize=12)
ax.set_xlim(0, 24)
ax.set_ylim(0, 4000)

# Set y - axis ticks and optimize the display format
ax.set_yticks(np.arange(0, 4500, 500))
ax.set_yticklabels([f'{y}' for y in np.arange(0, 4500, 500)], fontsize=12)

# Add grid lines and optimize the style
ax.grid(True, linestyle='--', alpha=0.4, color='#9aa0a6')

# Add original data points and optimize the style
ax.scatter(hours, heat_data, color='#1a73e8', s=50, zorder=5, edgecolor='white', linewidth=1)

# Add data labels for key time points and optimize the style and position
for x, y in zip(hours[::4], heat_data[::4]):
    ax.annotate(f'{y}', (x, y), textcoords='offset points',
                xytext=(0, 12), ha='center', fontsize=11, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='#dadce0', alpha=0.8))

# Highlight peaks and valleys and optimize the style
peak_idx = np.argmax(heat_data)
valley_idx = np.argmin(heat_data)
ax.scatter([hours[peak_idx], hours[valley_idx]],
           [heat_data[peak_idx], heat_data[valley_idx]],
           color='#ea4335', s=100, zorder=5, edgecolor='white', linewidth=1.5)

# Add annotations for peaks and valleys and optimize the style
ax.annotate(f'Peak: {heat_data[peak_idx]} ten thousand', (hours[peak_idx], heat_data[peak_idx]),
            textcoords='offset points', xytext=(30, 20), ha='left', fontsize=12,
            arrowprops=dict(arrowstyle='->', color='#ea4335', linewidth=1.5))

ax.annotate(f'Valley: {heat_data[valley_idx]} ten thousand', (hours[valley_idx], heat_data[valley_idx]),
            textcoords='offset points', xytext=(-30, -30), ha='right', fontsize=12,
            arrowprops=dict(arrowstyle='->', color='#ea4335', linewidth=1.5))

# Add time zone hints and optimize the style
ax.axvspan(5, 9, alpha=0.05, color='#4285f4', label='Morning Peak')
ax.axvspan(15, 17, alpha=0.05, color='#4285f4')
ax.text(7, 3800, 'Morning Peak', ha='center', fontsize=12, color='#202124',
        bbox=dict(boxstyle='round,pad=0.2', fc='#4285f4', alpha=0.1))
ax.text(16, 3800, 'Evening Peak', ha='center', fontsize=12, color='#202124',
        bbox=dict(boxstyle='round,pad=0.2', fc='#4285f4', alpha=0.1))

# Optimize the axis style
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#dadce0')
ax.spines['bottom'].set_color('#dadce0')
ax.tick_params(axis='both', which='major', labelsize=12, color='#9aa0a6')

# Add a legend and optimize the style
ax.legend([line], ['Search heat trend'], loc='upper right', frameon=True,
          framealpha=0.9, edgecolor='#dadce0', fontsize=12)

# Add a watermark and optimize the style
fig.text(0.85, 0.15, 'Data Visualization', fontsize=30, color='#e0e0e0',
         ha='center', va='center', rotation=30, alpha=0.3)

# Adjust the layout
plt.tight_layout()

# Display the chart
plt.show()