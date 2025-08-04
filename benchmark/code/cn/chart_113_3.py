import matplotlib.pyplot as plt
import numpy as np

# 孕期主要焦虑类型
anxieties = ["经济压力焦虑", "孕育知识焦虑", "未来规划焦虑", "信息不对称焦虑", 
             "家庭关系焦虑", "个人成长/工作焦虑", "身材焦虑", "健康焦虑", "选品购物焦虑"]
# 对应占比（%）
proportions = [31.57, 28.51, 27.90, 27.70, 26.68, 26.48, 25.87, 25.46, 23.42]

x = np.arange(len(anxieties))  # x轴坐标

fig, ax = plt.subplots(figsize=(12, 7))
# 绘制柱状图
bars = ax.bar(x, proportions, color='orange')

# 添加数值标注
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# 设置x轴刻度和标签，旋转标签
ax.set_xticks(x)
ax.set_xticklabels(anxieties, rotation=45, ha='right')
ax.set_ylabel('占比（%）')
ax.set_title('2025年中国母婴消费者认为女性孕期的主要焦虑')

plt.tight_layout()
plt.show()