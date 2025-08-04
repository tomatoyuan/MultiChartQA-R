import matplotlib.pyplot as plt
import numpy as np

# Data
age_groups = ["Under 20", "20 - 29", "30 - 39", "40 - 49", "50 - 59", "Over 60"]
data_2022 = np.array([6.6, 48.6, 35.8, 6.5, 2.1, 0.4])
data_2023 = np.array([6.8, 46.9, 37.1, 6.9, 1.9, 0.4])

# Set positions
x = np.arange(len(age_groups))
width = 0.35

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
bar1 = ax.bar(x - width/2, data_2022, width, label='2022', color="#efbfc2")
bar2 = ax.bar(x + width/2, data_2023, width, label='2023', color="#5c419d")

# Add labels
ax.set_ylabel('Proportion (%)')
ax.set_title('Age Group Distribution of Simple Psychological Counseling Clients from 2022 to 2023')
ax.set_xticks(x)
ax.set_xticklabels(age_groups)
ax.legend()

# Add data labels
for bar in bar1 + bar2:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()