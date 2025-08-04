import matplotlib.pyplot as plt
import numpy as np

# 数据整理
# 日均睡眠时长数据（非工作日、工作日）
sleep_duration_labels = ["6小时以内", "6-7小时", "7-8小时", "8-9小时", "9-10小时", "10小时以上"]
sleep_weekend = [2.2, 12.2, 29.0, 35.3, 17.6, 3.7]
sleep_weekday = [6.7, 20.4, 40.0, 16.6, 10.5, 5.8]

# 入睡时间数据（非工作日、工作日）
sleep_time_labels = ["22点以前", "22-23点", "23-0点", "0-1点", "1-2点", "2点之后"]
sleep_time_weekend = [5.2, 23.0, 33.1, 22.1, 12.5, 4.1]
sleep_time_weekday = [7.9, 31.2, 34.4, 13.5, 7.8, 5.2]

x = np.arange(len(sleep_duration_labels))  # 用于睡眠时长的 x 轴
x2 = np.arange(len(sleep_time_labels))     # 用于入睡时间的 x 轴

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# 绘制【非工作日-日均睡眠时长】
axes[0, 0].bar(x, sleep_weekend, color='orange', label='非工作日')
axes[0, 0].set_xticks(x)
axes[0, 0].set_xticklabels(sleep_duration_labels)
axes[0, 0].set_ylabel('占比（%）')
axes[0, 0].set_title('中国居民的日均睡眠时长（非工作日）')
for i, val in enumerate(sleep_weekend):
    axes[0, 0].text(i, val + 1, f'{val}%', ha='center')

# 绘制【工作日-日均睡眠时长】
axes[1, 0].bar(x, sleep_weekday, color='gold', label='工作日')
axes[1, 0].set_xticks(x)
axes[1, 0].set_xticklabels(sleep_duration_labels)
axes[1, 0].set_ylabel('占比（%）')
axes[1, 0].set_title('中国居民的日均睡眠时长（工作日）')
for i, val in enumerate(sleep_weekday):
    axes[1, 0].text(i, val + 1, f'{val}%', ha='center')

# 绘制【非工作日-入睡时间】
axes[0, 1].bar(x2, sleep_time_weekend, color='orange', label='非工作日')
axes[0, 1].set_xticks(x2)
axes[0, 1].set_xticklabels(sleep_time_labels)
axes[0, 1].set_ylabel('占比（%）')
axes[0, 1].set_title('中国居民的入睡时间（非工作日）')
for i, val in enumerate(sleep_time_weekend):
    axes[0, 1].text(i, val + 1, f'{val}%', ha='center')

# 绘制【工作日-入睡时间】
axes[1, 1].bar(x2, sleep_time_weekday, color='gold', label='工作日')
axes[1, 1].set_xticks(x2)
axes[1, 1].set_xticklabels(sleep_time_labels)
axes[1, 1].set_ylabel('占比（%）')
axes[1, 1].set_title('中国居民的入睡时间（工作日）')
for i, val in enumerate(sleep_time_weekday):
    axes[1, 1].text(i, val + 1, f'{val}%', ha='center')

plt.tight_layout()
plt.show()