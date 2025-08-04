import matplotlib.pyplot as plt
import numpy as np


# 数据
months = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
data_2022 = [47.4, 46.6, 47.3, 46.2, 47.2, 47.5, 47.9, 47.9, 47.7, 47.8, 47.6, 47.8]
data_2023 = [47.8, 47.8, 48.6, 48.7, 48.5, 48.6, 48.6, 48.6, 48.8, 48.7, 48.9, 48.9]
data_2024 = [48.9, 48.0] + [None] * 10

x = np.arange(len(months))
width = 0.25

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(x - width, data_2022, width=width, label='2022年', color='#f1c232')
ax.bar(x, data_2023, width=width, label='2023年', color='#3c78d8')
ax.bar(x + width, [v if v is not None else 0 for v in data_2024], width=width, label='2024年', color='red')

# 添加值标签
for i, v in enumerate(data_2022):
    ax.text(x[i] - width, v + 0.1, f"{v}", ha='center', va='bottom', fontsize=9)
for i, v in enumerate(data_2023):
    ax.text(x[i], v + 0.1, f"{v}", ha='center', va='bottom', fontsize=9)
for i, v in enumerate(data_2024):
    if v is not None:
        ax.text(x[i] + width, v + 0.1, f"{v}", ha='center', va='bottom', fontsize=9)

ax.set_xticks(x)
ax.set_xticklabels(months)
ax.set_ylim(44, 51)
ax.set_ylabel('小时/周')
ax.set_title('2022—2024年我国企业就业人员周平均工作时间')

ax.legend()
plt.tight_layout()
plt.show()