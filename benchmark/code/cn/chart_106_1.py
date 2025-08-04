import matplotlib.pyplot as plt
import numpy as np

# 饮料类别
categories = ["醋饮料（如天地壹号）", "固体饮料（如香飘飘）", "含乳饮料（如酸奶、酸乳等）", "咖啡饮料（如雀巢咖啡）", 
              "植物蛋白饮料（如豆奶等）", "茶饮料（如康师傅茉莉清茶）", "功能性饮料（如东鹏特饮）", "碳酸饮料（如可乐）", 
              "气泡水（如元气森林）", "果汁或蔬菜汁饮料（如美汁源果粒橙）", "包装饮用水（如怡宝矿泉水）", "奶制品（如酸奶、牛奶）"]
# 对应占比（%）
proportions = [16.10, 16.90, 29.30, 29.40, 31.00, 31.60, 32.80, 49.50, 50.90, 51.00, 51.00, 51.70]

y = np.arange(len(categories))  # y轴坐标

fig, ax = plt.subplots(figsize=(10, 7))
# 绘制水平柱状图
bars = ax.barh(y, proportions, color='orange')

# 添加数值标注
for i, proportion in enumerate(proportions):
    ax.text(proportion, i, f'{proportion}', va='center', ha='left', fontsize=9)

# 设置y轴刻度和标签
ax.set_yticks(y)
ax.set_yticklabels(categories)
ax.set_xlabel('占比（%）')
ax.set_title('2025年中国消费者饮料类别了解情况')

plt.tight_layout()
plt.show()