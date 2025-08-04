import matplotlib.pyplot as plt
import numpy as np

# 数据（示例热度值，可替换为真实数据）
categories = ["年夜饭", "拜年祝福", "看春晚/压岁钱/守岁", "压岁钱", "放鞭炮/拜神祈福"]
north = [85, 70, 65, 90, 75]  # 北方热度值（示例数据）
south = [95, 60, 70, 80, 55]  # 南方热度值（示例数据）

y = np.arange(len(categories))  # y轴坐标
max_value = max(max(north), max(south))  # 获取最大热度值用于设置x轴范围

# 创建画布
fig, ax = plt.subplots(figsize=(12, 6))

# 绘制北方条形图（左侧，向负方向延伸）
ax.barh(y, [-n for n in north], height=0.4, label="北方", color="#1E88E5")
# 绘制南方条形图（右侧，向正方向延伸）
ax.barh(y, south, height=0.4, label="南方", color="#FF5722")

# 设置y轴标签
ax.set_yticks(y)
ax.set_yticklabels(categories, fontsize=12)

# 设置x轴范围和标签
ax.set_xlim(-max_value - 10, max_value + 10)
ax.set_xticks([-100, -75, -50, -25, 0, 25, 50, 75, 100])
ax.set_xticklabels(['100', '75', '50', '25', '0', '25', '50', '75', '100'])
ax.set_xlabel('热度值', fontsize=12)

# 设置标题和图例
ax.set_title('“春节仪式感” 南北方关注热度对比', fontsize=16, pad=20)
ax.legend(loc='upper right')

# 添加数据标签
for i, v in enumerate(north):
    ax.text(-v - 5, i, str(v), va='center', ha='right', color='black')
for i, v in enumerate(south):
    ax.text(v + 5, i, str(v), va='center', ha='left', color='black')

# 隐藏顶部、右侧边框，调整底部边框位置
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_position('center')

plt.tight_layout()
plt.show()