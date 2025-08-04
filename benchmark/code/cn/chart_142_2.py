import matplotlib.pyplot as plt
import numpy as np

# 数据
years = ["2019", "2020", "2021", "2022"]
export_growth = [30.5, 39.2, 28.3, 10.1]  # 出口规模同比增长率（%）
import_growth = [10.8, 9.1, -0.9, 0.8]    # 进口规模同比增长率（%）
total_growth = [22.2, 25.7, 18.6, 7.1]    # 进出口规模同比增长率（%）

x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(10, 6))

# 绘制折线图
ax.plot(x, total_growth, marker='o', color='blue', label='进出口规模同比（%）', linewidth=2)
ax.plot(x, import_growth, marker='o', color='orange', label='进口规模同比（%）', linewidth=2)
ax.plot(x, export_growth, marker='o', color='green', label='出口规模同比（%）', linewidth=2)

ax.set_ylabel('同比增长率（%）')
ax.set_xlabel('年份')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()
ax.set_title('2019-2022年中国跨境电商进出口规模同比增长率')

# 添加数值标注
for i in range(len(years)):
    # 标注进出口规模同比数值
    ax.text(i, total_growth[i] + 1, f'{total_growth[i]}', ha='center', va='bottom', color='blue')
    # 标注进口规模同比数值
    ax.text(i, import_growth[i] + 1, f'{import_growth[i]}', ha='center', va='bottom', color='orange')
    # 标注出口规模同比数值
    ax.text(i, export_growth[i] + 1, f'{export_growth[i]}', ha='center', va='bottom', color='green')

plt.tight_layout()
plt.show()