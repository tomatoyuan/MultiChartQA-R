import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# Data
years = ['2019', '2020', '2021', '2022', '2023']
T1 = [12, 11, 11, 10, 10]
T2 = [47, 47, 46, 45, 43]
T3 = [41, 43, 44, 45, 48]
totals = [6243, 4114, 7044, 5476, 6221]

bar_width = 0.5
fig1, ax1 = plt.subplots(figsize=(10, 6))

# Calculate the bottom positions
bottom_T1 = np.array(T3)
bottom_T2 = bottom_T1 + np.array(T2)

# Draw the bar chart
p1 = ax1.bar(years, T3, label='T3+', color='#FDB462')
p2 = ax1.bar(years, T2, bottom=bottom_T1, label='T2', color='#80B1D3')
p3 = ax1.bar(years, T1, bottom=bottom_T2, label='T1', color='#FB8072')

# Add total number annotations on top
for i, total in enumerate(totals):
    ax1.text(i, 103, str(total), ha='center', va='bottom', fontsize=10, fontweight='bold')

# Add percentage annotations for each segment
for i in range(len(years)):
    # T3+
    ax1.text(i, T3[i] / 2, f"{T3[i]}%", ha='center', va='center', fontsize=10, color='black')
    # T2
    ax1.text(i, bottom_T1[i] + T2[i] / 2, f"{T2[i]}%", ha='center', va='center', fontsize=10, color='black')
    # T1
    ax1.text(i, bottom_T2[i] + T1[i] / 2, f"{T1[i]}%", ha='center', va='center', fontsize=10, color='black')

# Set the title and axes
ax1.set_title('Distribution of Newly Opened Stores from 2019 - 2023', fontsize=14)
ax1.set_ylabel('Percentage (%)')
ax1.set_ylim(0, 115)
ax1.legend()

plt.tight_layout()
plt.show()