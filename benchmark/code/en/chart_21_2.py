import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# 1. Simulate original data (dates, population size)
dates = np.array(['1-10', '1-13', '1-16', '1-19', '1-22', '1-25', '1-28',
                  '1-31', '2-3', '2-6', '2-9', '2-12', '2-15', '2-18', '2-21'])

# Student going home data (peaks on 1-19 and 1-25, half - peak on 1-22, 0 on 1-10 and 2-21)
student_go = np.array([0, 30, 60, 50, 30, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0])

# Migrant worker going home data (peak around 1-25)
worker_go = np.array([0, 0, 0, 30, 80, 85, 0, 0, 0, 0, 0, 0, 0, 0, 0])

# White - collar going home data (peak around 1-22)
white_collar_go = np.array([0, 0, 0, 0, 70, 75, 0, 0, 0, 0, 0, 0, 0, 0, 0])

# Return data (uniformly distributed in February)
student_back = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 60, 70, 75, 70])
worker_back = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 60, 65, 64, 45, 0, 0])
white_collar_back = np.array([0, 0, 0, 0, 0, 0, 0, 0, 75, 70, 0, 0, 0, 0, 0])

# 2. Create a uniformly distributed time axis
x_uniform = np.arange(len(dates))  # Uniformly distributed numerical axis

# 3. Interpolation and smoothing processing
def smooth_curve(y):
    x_new = np.linspace(x_uniform.min(), x_uniform.max(), 300)
    spline = make_interp_spline(x_uniform, y, k = 3)
    return x_new, spline(x_new)

# Smoothing process
x_smooth, student_go_smooth = smooth_curve(student_go)
_, worker_go_smooth = smooth_curve(worker_go)
_, white_collar_go_smooth = smooth_curve(white_collar_go)

_, student_back_smooth = smooth_curve(student_back)
_, worker_back_smooth = smooth_curve(worker_back)
_, white_collar_back_smooth = smooth_curve(white_collar_back)

# 4. Draw the curve graph
fig, ax = plt.subplots(figsize=(14, 7), facecolor='#f8f9fa')
ax.set_facecolor('#f8f9fa')

# Going home phase curve and filling
student_go_line, = ax.plot(x_smooth, student_go_smooth, color='#A8D8EA', linewidth=2.5, label='Students (Going Home)')
ax.fill_between(x_smooth, student_go_smooth, color='#A8D8EA', alpha=0.3)  # Fill the student going home curve

worker_go_line, = ax.plot(x_smooth, worker_go_smooth, color='#AA96DA', linewidth=2.5, label='Migrant Workers (Going Home)')
ax.fill_between(x_smooth, worker_go_smooth, color='#AA96DA', alpha=0.3)  # Fill the migrant worker going home curve

white_collar_go_line, = ax.plot(x_smooth, white_collar_go_smooth, color='#FCBAD3', linewidth=2.5, label='White - Collars (Going Home)')
ax.fill_between(x_smooth, white_collar_go_smooth, color='#FCBAD3', alpha=0.3)  # Fill the white - collar going home curve

# Return phase curve and filling
student_back_line, = ax.plot(x_smooth, student_back_smooth, color='#CDEAC0', linewidth=2.5, label='Students (Returning)')
ax.fill_between(x_smooth, student_back_smooth, color='#CDEAC0', alpha=0.3)  # Fill the student returning curve

worker_back_line, = ax.plot(x_smooth, worker_back_smooth, color='#FFDAC1', linewidth=2.5, label='Migrant Workers (Returning)')
ax.fill_between(x_smooth, worker_back_smooth, color='#FFDAC1', alpha=0.3)  # Fill the migrant worker returning curve

white_collar_back_line, = ax.plot(x_smooth, white_collar_back_smooth, color='#FFB7B2', linewidth=2.5, label='White - Collars (Returning)')
ax.fill_between(x_smooth, white_collar_back_smooth, color='#FFB7B2', alpha=0.3)  # Fill the white - collar returning curve

# 5. Set x - axis tick labels
plt.xticks(x_uniform, dates)
plt.xticks(rotation=30)

# 6. Add title, legend, and decoration
ax.set_title('Population Trend During the 2017 Spring Festival Travel Rush', fontsize=18, fontweight='bold', color='#333')
ax.set_xlabel('Date', fontsize=14, color='#555')
ax.set_ylabel('Population Size', fontsize=14, color='#555')
ax.legend(loc='upper right', fontsize=11)

# 7. Add a dividing line (Spring Festival position)
plt.axvline(x = 6.0, color='red', linestyle='--', alpha=0.5)
plt.text(5.6, max(student_go.max(), worker_go.max(), white_collar_go.max()) * 0.95,
         'Spring Festival', fontsize=13, color='red')

# 8. Add grid lines
plt.grid(True, linestyle='--', alpha=0.6)

# 9. Hide the top and right borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 10. Display the chart
plt.tight_layout()
plt.show()