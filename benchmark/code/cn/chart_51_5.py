import matplotlib.pyplot as plt
import numpy as np

# 数据定义，项目数量分布和项目金额分布
labels = ["银行", "保险", "证券", "其他"]
sizes数量 = [53, 12, 15, 20]  # 项目数量分布，大体模拟
sizes金额 = [56, 8, 17, 19]  # 项目金额分布，大体模拟
# 颜色设置，尽量贴近原图
colors = ["greenyellow", "green", "limegreen", "lightseagreen"]

# 创建画布和子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# 绘制项目数量分布饼图
ax1.pie(sizes数量, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
ax1.set_title('项目数量分布')

# 绘制项目金额分布饼图
ax2.pie(sizes金额, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
ax2.set_title('项目金额分布')

# 添加主标题
fig.suptitle('2024年金融行业大模型中标项目领域分布', fontsize=14)

plt.tight_layout()
plt.show()