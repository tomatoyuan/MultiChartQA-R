import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime

# Original key data points
dates = [
    datetime.datetime(2024, 8, 16),
    datetime.datetime(2024, 8, 30),
    datetime.datetime(2024, 9, 15),
    datetime.datetime(2024, 9, 25),  # Surge point
    datetime.datetime(2024, 10, 15),
    datetime.datetime(2024, 11, 4),
    datetime.datetime(2024, 11, 24),
    datetime.datetime(2024, 12, 11)
]

ai_index = [0, -5, -3, 23, 20, 36, 35, 42.3]
sh_index = [0, 1, -2, 17, 18, 12, 16, 19.3]

# Convert dates to numerical values
x = mdates.date2num(dates)

# Generate more dense date points (daily data)
start_date = dates[0]
end_date = dates[-1]
delta = end_date - start_date
all_dates = [start_date + datetime.timedelta(days=i) for i in range(delta.days + 1)]
all_x = mdates.date2num(all_dates)

# Market volatility generation function (uniform volatility across the entire curve)
def generate_market_volatility(x, y, all_x, volatility=0.03, persistence=0.7):
    """
    Generate market data with uniform volatility across the entire curve
    
    Parameters:
    x: x-coordinates of the original data points
    y: y-coordinates of the original data points
    all_x: all x-coordinates where data needs to be generated
    volatility: Volatility intensity coefficient
    persistence: Persistence of the volatility direction (between 0 and 1)
    """
    # Perform cubic spline interpolation on the original data to get the base curve
    from scipy.interpolate import make_interp_spline
    spl = make_interp_spline(x, y, k=3)
    base_curve = spl(all_x)
    
    # Calculate the daily volatility amplitude (as a percentage of the base curve)
    daily_volatility = np.abs(base_curve) * volatility
    
    # Generate random walk volatility with directional persistence
    n_points = len(all_x)
    noise = np.zeros(n_points)
    direction = 1  # Initial direction
    
    for i in range(1, n_points):
        # Change the direction with a probability of (1 - persistence)
        if np.random.random() > persistence:
            direction = -direction
        
        # Generate the volatility value at this point (using Laplace distribution to increase extreme values)
        noise[i] = np.random.laplace(0, daily_volatility[i]) * direction
    
    # Cumulate the volatility to form a random walk
    cumulative_noise = np.cumsum(noise)
    
    # Ensure that the endpoints match the original data
    # Calculate the offset needed to adjust so that the final point returns to the original value
    offset = y[-1] - (base_curve[-1] + cumulative_noise[-1])
    adjusted_noise = cumulative_noise + offset * np.linspace(0, 1, n_points)
    
    # Final volatility curve = base curve + adjusted volatility
    final_curve = base_curve + adjusted_noise
    
    return final_curve

# Generate data with uniform volatility across the entire curve
ai_volatile = generate_market_volatility(x, ai_index, all_x, volatility=0.04, persistence=0.6)
sh_volatile = generate_market_volatility(x, sh_index, all_x, volatility=0.025, persistence=0.7)

# Create the chart
fig, ax = plt.subplots(figsize=(16, 9))

# Plot the volatility curves
line_ai, = ax.plot(all_x, ai_volatile, label='AI Glass Index (886085)', 
                   color='#32CD32', linewidth=1.6, alpha=0.9)
line_sh, = ax.plot(all_x, sh_volatile, label='Shanghai Composite Index (000001)', 
                   color='#1E90FF', linewidth=1.6, alpha=0.9, linestyle='--')

# Label the final price changes
ax.text(all_x[-1], ai_volatile[-1], f'{ai_volatile[-1]:.1f}%', ha='left', va='bottom', 
        color='#32CD32', fontweight='bold', fontsize=12, bbox=dict(facecolor='white', alpha=0.7))
ax.text(all_x[-1], sh_volatile[-1], f'{sh_volatile[-1]:.1f}%', ha='left', va='bottom', 
        color='#1E90FF', fontweight='bold', fontsize=12, bbox=dict(facecolor='white', alpha=0.7))

# Set the x-axis to date format and control the display density
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))  # Display one date per week
plt.xticks(rotation=45, fontsize=10)

# Set the title and legend
ax.set_title('Comparison of Cumulative Price Changes between AI Glass Index and Shanghai Composite Index\n(2024/8/16 - 2024/12/11)', 
             fontsize=17, pad=15, fontweight='bold')
ax.legend(loc='upper left', frameon=True, framealpha=0.9, fontsize=12)

# Set the y-axis to percentage format
ax.set_ylabel('Cumulative Price Change (%)', fontsize=13)
ax.set_ylim(-30, 70)  # Further expand the y-axis range to accommodate larger volatility

# Show the grid
ax.grid(True, linestyle='--', alpha=0.6, which='both')

# Highlight the vertical line for the key date
ax.axvline(x[3], color='gray', linestyle='-.', alpha=0.5)  # 2024/9/25

# Add background colors to distinguish different time periods
for i in range(len(x)-1):
    if i == 3:  # The area after the surge point
        ax.axvspan(x[i], x[i+1], color='lightgreen', alpha=0.1)
    else:
        ax.axvspan(x[i], x[i+1], color='white' if i%2==0 else 'lightgray', alpha=0.1)

# Beautify the chart border
for spine in ax.spines.values():
    spine.set_color('gray')
    spine.set_linewidth(1)

# Add a note about volatility
ax.text(0.02, 0.02, 'Note: Volatility is uniformly applied across the entire curve, consistent with the continuous volatility characteristics of the market', 
        transform=ax.transAxes, fontsize=10, color='gray')

# Adjust the layout
plt.tight_layout()
plt.show()