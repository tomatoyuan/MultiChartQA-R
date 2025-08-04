import matplotlib.pyplot as plt
import numpy as np

# 数据
factors = ["最大续航里程", "充电所需时间", "汽车安全性", "新能源汽车价格", "节能减排性能", 
           "国家补贴", "新能源汽车外观", "车企促销力度", "跟随潮流"]
percentages = [51.3, 46.2, 46.0, 45.1, 38.2, 35.7, 34.8, 22.9, 17.4]

x = np.arange(len(factors))

fig, ax = plt.subplots(figsize=(12, 7))

# 绘制柱状图
bars = ax.bar(x, percentages, color='orange')

# 添加数值标注
for i, percentage in enumerate(percentages):
    ax.text(i, percentage + 1, f'{percentage}%', ha='center', va='bottom')

# 设置坐标轴
ax.set_ylabel('百分比（%）')
ax.set_xlabel('选购因素')
ax.set_xticks(x)
ax.set_xticklabels(factors, rotation=45, ha='right')
ax.set_title('2023年中国新能源汽车用户选购因素分析')

plt.tight_layout()
plt.show()