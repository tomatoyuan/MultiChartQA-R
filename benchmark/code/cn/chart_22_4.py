import matplotlib.pyplot as plt
import numpy as np

# 官方合作伙伴数据
partners = {
    "壳牌": 0.2,
    "豪雅": 0.4
}

# 计算总金额
total = sum(partners.values())

# 创建画布
plt.figure(figsize=(10, 6))

# 官方合作伙伴水平条形图
partner_names = list(partners.keys())
partner_values = list(partners.values())

# 绘制水平条形图
y_pos = np.arange(len(partner_names))
bars = plt.barh(y_pos, partner_values, align='center', color='#4e79a7', height=0.6)
plt.yticks(y_pos, partner_names, fontsize=12)
plt.xlabel('金额 (亿元)', fontsize=12)
plt.title('官方合作伙伴及供应商分布', fontsize=14)
plt.xlim(0, max(partner_values) * 1.3)  # 调整x轴范围，为标签留出空间

# 在条形上添加数值标签
for i, v in enumerate(partner_values):
    plt.text(v + 0.01, i, f'{v:.2f} 亿元', va='center', fontsize=11)
    plt.text(v + 0.01, i - 0.3, f'({v/total*100:.1f}%)', va='center', fontsize=9, color='gray')

# 添加总计信息
plt.axvline(x=total, color='r', linestyle='--', alpha=0.5)
plt.text(total + 0.01, len(partner_names), f'总计: {total:.2f} 亿元', va='center', fontsize=11, color='red')

plt.tight_layout()
plt.show()