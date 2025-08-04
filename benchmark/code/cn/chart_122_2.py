import matplotlib.pyplot as plt
import numpy as np

# 婚礼预算区间
categories = ["5万元以下", "5-10万元", "10-20万元", "20-30万元", "30-40万元", "40-50万元", "50万元以上"]
# 对应占比（%）
proportions = [8.8, 30.4, 34.2, 18.2, 6.5, 1.2, 0.7]
# 模拟钱袋数量（根据占比大致对应，可微调让视觉更接近原图）
bag_counts = [1, 6, 7, 4, 2, 1, 1]

x = np.arange(len(categories))

fig, ax = plt.subplots(figsize=(10, 6))

# 绘制“钱袋”柱状图（用多个小矩形模拟堆叠效果）
for i in range(len(categories)):
    for j in range(bag_counts[i]):
        rect = plt.Rectangle((x[i] - 0.2, j * 1), 0.4, 1, color='orange')
        ax.add_patch(rect)
        # 在最上方钱袋附近添加占比标注（只添加一次）
        if j == bag_counts[i] - 1:
            ax.text(x[i], (j + 1) * 1 + 0.2, f'{proportions[i]}%', ha='center', va='bottom')

# 设置坐标轴
ax.set_ylabel('钱袋堆叠示意')
ax.set_xlabel('预算区间')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.set_ylim(0, max(bag_counts) + 1)  # 预留空间显示标注
ax.axis('off')  # 隐藏默认坐标轴，突出钱袋样式

ax.set_title('中国婚礼筹办花费/预算情况调查')

plt.tight_layout()
plt.show()