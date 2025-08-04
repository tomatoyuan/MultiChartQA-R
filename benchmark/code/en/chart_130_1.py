import matplotlib.pyplot as plt
import numpy as np

# Data organization
# Average daily sleep duration data (weekends, weekdays)
sleep_duration_labels = ["Less than 6 hours", "6 - 7 hours", "7 - 8 hours", "8 - 9 hours", "9 - 10 hours", "More than 10 hours"]
sleep_weekend = [2.2, 12.2, 29.0, 35.3, 17.6, 3.7]
sleep_weekday = [6.7, 20.4, 40.0, 16.6, 10.5, 5.8]

# Bedtime data (weekends, weekdays)
sleep_time_labels = ["Before 22:00", "22:00 - 23:00", "23:00 - 0:00", "0:00 - 1:00", "1:00 - 2:00", "After 2:00"]
sleep_time_weekend = [5.2, 23.0, 33.1, 22.1, 12.5, 4.1]
sleep_time_weekday = [7.9, 31.2, 34.4, 13.5, 7.8, 5.2]

x = np.arange(len(sleep_duration_labels))  # x - axis for sleep duration
x2 = np.arange(len(sleep_time_labels))     # x - axis for bedtime

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Plot [Weekends - Average daily sleep duration]
axes[0, 0].bar(x, sleep_weekend, color='orange', label='Weekends')
axes[0, 0].set_xticks(x)
axes[0, 0].set_xticklabels(sleep_duration_labels)
axes[0, 0].set_ylabel('Percentage (%)')
axes[0, 0].set_title('Average daily sleep duration of Chinese residents (Weekends)')
for i, val in enumerate(sleep_weekend):
    axes[0, 0].text(i, val + 1, f'{val}%', ha='center')

# Plot [Weekdays - Average daily sleep duration]
axes[1, 0].bar(x, sleep_weekday, color='gold', label='Weekdays')
axes[1, 0].set_xticks(x)
axes[1, 0].set_xticklabels(sleep_duration_labels)
axes[1, 0].set_ylabel('Percentage (%)')
axes[1, 0].set_title('Average daily sleep duration of Chinese residents (Weekdays)')
for i, val in enumerate(sleep_weekday):
    axes[1, 0].text(i, val + 1, f'{val}%', ha='center')

# Plot [Weekends - Bedtime]
axes[0, 1].bar(x2, sleep_time_weekend, color='orange', label='Weekends')
axes[0, 1].set_xticks(x2)
axes[0, 1].set_xticklabels(sleep_time_labels)
axes[0, 1].set_ylabel('Percentage (%)')
axes[0, 1].set_title('Bedtime of Chinese residents (Weekends)')
for i, val in enumerate(sleep_time_weekend):
    axes[0, 1].text(i, val + 1, f'{val}%', ha='center')

# Plot [Weekdays - Bedtime]
axes[1, 1].bar(x2, sleep_time_weekday, color='gold', label='Weekdays')
axes[1, 1].set_xticks(x2)
axes[1, 1].set_xticklabels(sleep_time_labels)
axes[1, 1].set_ylabel('Percentage (%)')
axes[1, 1].set_title('Bedtime of Chinese residents (Weekdays)')
for i, val in enumerate(sleep_time_weekday):
    axes[1, 1].text(i, val + 1, f'{val}%', ha='center')

plt.tight_layout()
plt.show()