import matplotlib.pyplot as plt
import numpy as np

# 数据
functions = ["购物方便性", "个性化服务", "互动与社交", "服务与售后", 
             "数据安全和隐私保护", "图像识别", "其他"]
percentages = [67.2, 63.5, 48.8, 40.0, 31.6, 24.4, 0.0]

x = np.arange(len(functions))

fig, ax = plt.subplots(figsize=(10, 6))

# 绘制柱状图
bars = ax.bar(x, percentages, color='orange')

# 添加数值标注
for i, percentage in enumerate(percentages):
    ax.text(i, percentage + 1, f'{percentage}%', ha='center', va='bottom')

# 设置坐标轴
ax.set_ylabel('百分比（%）')
ax.set_xlabel('优势功能类型')
ax.set_xticks(x)
ax.set_xticklabels(functions, rotation=15, ha='right')
ax.set_title('2024年中国AI电商吸引消费者的主要优势功能')

plt.tight_layout()
plt.show()