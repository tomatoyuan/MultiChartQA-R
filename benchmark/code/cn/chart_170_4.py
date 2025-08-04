import matplotlib.pyplot as plt
import numpy as np

# 数据
age_groups = ["20岁以下", "20-29岁", "30-39岁", "40-49岁", "50-59岁", "60岁以上"]
data_2022 = np.array([6.6, 48.6, 35.8, 6.5, 2.1, 0.4])
data_2023 = np.array([6.8, 46.9, 37.1, 6.9, 1.9, 0.4])

# 设置位置
x = np.arange(len(age_groups))
width = 0.35

# 绘图
fig, ax = plt.subplots(figsize=(10, 6))
bar1 = ax.bar(x - width/2, data_2022, width, label='2022 年', color="#efbfc2")
bar2 = ax.bar(x + width/2, data_2023, width, label='2023 年', color="#5c419d")

# 添加标签
ax.set_ylabel('比例 (%)')
ax.set_title('2022-2023 年简单心理咨询来访者年龄段分布')
ax.set_xticks(x)
ax.set_xticklabels(age_groups)
ax.legend()

# 添加数据标签
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