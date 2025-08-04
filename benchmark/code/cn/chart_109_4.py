import matplotlib.pyplot as plt
import numpy as np

# 看重因素
factors = ["产地", "质量", "品牌", "包装", "价格", "有机/绿色认证", 
           "新鲜度", "营养成分", "购买便利性", "供应商信誉", "售后服务", "促销活动"]
# 对应占比（%）
proportions = [42.42, 38.64, 35.00, 33.64, 29.70, 28.79, 
               21.82, 21.36, 14.09, 13.33, 12.73, 6.67]

x = np.arange(len(factors))  # x轴坐标

fig, ax = plt.subplots(figsize=(12, 7))
# 绘制柱状图
bars = ax.bar(x, proportions, color='orange')

# 添加数值标注
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# 设置x轴刻度和标签，旋转标签
ax.set_xticks(x)
ax.set_xticklabels(factors, rotation=45, ha='right')
ax.set_ylabel('占比（%）')
ax.set_title('2025年中国农村电商消费者购买农产品时所看重因素')

plt.tight_layout()
plt.show()