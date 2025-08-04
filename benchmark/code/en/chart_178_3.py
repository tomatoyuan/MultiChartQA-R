import matplotlib.pyplot as plt
import numpy as np

# Age groups
ages = ["Post-00s", "Post-95s", "Post-90s", "Post-85s", "Post-80s", "Post-75s", "Post-70s", "Pre-70s"]
# Proportion of the overall gift - giving population (bar chart)
total_gift_pct = [11, 17, 25, 18, 15, 8, 7, 4]
# TGI of giving health gifts (line chart)
health_gift_tgi = [105, 90, 101, 106, 103, 99, 97, 93]

x = np.arange(len(ages))
width = 0.6

fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar chart (left axis)
bars = ax1.bar(x, total_gift_pct, width=width, color='lightcoral', label='Overall gift - giving population')
ax1.set_ylabel('Proportion of overall gift - giving population', fontsize=12)
ax1.set_ylim(0, 30)
ax1.set_xticks(x)
ax1.set_xticklabels(ages, fontsize=10)
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}%', xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3), textcoords="offset points", ha='center', fontsize=10)

# Line chart (right axis)
ax2 = ax1.twinx()
line, = ax2.plot(x, health_gift_tgi, color='firebrick', marker='o', label='TGI of giving health gifts')
ax2.set_ylabel('TGI of giving health gifts', fontsize=12)
ax2.set_ylim(80, 110)
for i, v in enumerate(health_gift_tgi):
    ax2.text(x[i], v + 1, str(v), color='firebrick', ha='center', fontsize=10)

# Combine legends (fix method)
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
fig.legend(handles1 + handles2, labels1 + labels2, loc='upper right', fontsize=10)

# Title and layout
fig.suptitle('Age - cohort distribution of New Year \ngift - giving population', fontsize=16, fontweight='bold')
fig.tight_layout()
plt.show()