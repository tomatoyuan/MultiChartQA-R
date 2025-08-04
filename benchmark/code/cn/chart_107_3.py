import matplotlib.pyplot as plt
import numpy as np

# 不足类型
shortcomings = ["套餐性价比低", "推销电话过多", "售后服务差", "网速较差，会限速", "业务程序繁琐", 
                "增值服务费用多", "通话时长少", "网络覆盖不均（在某些地区信号弱或不稳定）", "套餐变更困难"]
# 对应占比（%）
proportions = [44.75, 38.97, 34.58, 31.69, 27.30, 25.05, 20.66, 18.31, 9.31]

x = np.arange(len(shortcomings))  # x轴坐标

fig, ax = plt.subplots(figsize=(10, 6))
# 绘制柱状图
bars = ax.bar(x, proportions, color='orange')

# 添加数值标注
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# 设置x轴刻度和标签，旋转标签
ax.set_xticks(x)
ax.set_xticklabels(shortcomings, rotation=45, ha='right')
ax.set_ylabel('占比（%）')
ax.set_title('2025年中国用户认为目前所使用的通信运营商存在的不足')

plt.tight_layout()
plt.show()