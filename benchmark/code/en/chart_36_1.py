import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Date data, using serial numbers to represent dates (May 7th is day 0, and so on)
x = np.arange(0, 20, 1)
# Simulated transaction index data, roughly simulating the trend of the original curve
y = [10, 120, 140, 160, 170, 180, 190, 200, 210, 220, 250, 280, 310, 320, 330, 340, 350, 360, 370, 380]

# Create more dense x-axis data points for a smooth curve
x_smooth = np.linspace(x.min(), x.max(), 300)

# Use cubic spline interpolation to create a smooth curve
spl = make_interp_spline(x, y, k=3)  # k = 3 means cubic spline
y_smooth = spl(x_smooth)

# Create a canvas
fig, ax = plt.subplots(figsize=(8, 6))

# Add the main title
plt.title('618 Promotion Transaction Index Trend Chart', fontsize=16, pad=20)

# Plot the smooth curve, set the color close to the gradient of the original chart
line, = ax.plot(x_smooth, y_smooth, color='pink', linewidth=3)
# Fill the area below the curve with a gradient color
ax.fill_between(x_smooth, y_smooth, color='pink', alpha=0.3)

# Set x-axis ticks and labels, corresponding to actual dates
x_labels = ['May 7th', '', '', '', '', 'May 13th', '', '', '', '', '', 'May 16th', '', '', '', '', '', '', '', 'May 26th']
ax.set_xticks(np.arange(0, 20, 1))
ax.set_xticklabels(x_labels, rotation=0, ha='center')

# Add annotation text
ax.text(5, 50, 'First-wave budget proportion: 60%\nWin the first-wave traffic advantage', fontsize=12, ha='center')
ax.text(5, 30, 'Pre-sale start date', fontsize=10, ha='center', color='red')
ax.text(15, 120, '618 Pre-purchase sales', fontsize=12, ha='center', color='red')

# Annotate key data points
highlight_indices = [0, 5, 10, 15, 19]  # Select the indices of the data points to be annotated
for i in highlight_indices:
    # Annotate at the position of the original data point, not the smoothed position
    ax.annotate(f'{y[i]}',  # The text content of the annotation
                xy=(x[i], y[i]),  # The data point to be annotated
                xytext=(x[i], y[i]+15),  # The text position (above the data point)
                arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),  # Arrow style
                ha='center',  # Horizontal alignment
                fontsize=10)  # Font size

# Set the y-axis label
ax.set_ylabel('Transaction Index')

# Hide the top and right borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Display the chart
plt.tight_layout()
plt.show()