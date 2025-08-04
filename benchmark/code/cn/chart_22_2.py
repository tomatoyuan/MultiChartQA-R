import matplotlib.pyplot as plt
import numpy as np

# 数据
total_revenue = 15
media_rights = 10
sponsors = {
    "中国平安": 1.815,
    "耐克": 1,
    "福特": 0.4,
    "京东": 0.35,
    "嘉士伯": 0.2,
    "DHL": 0.2,
    "红牛": 0.2
}
partners = {
    "壳牌": 0.2,
    "豪雅": 0.4
}

# 计算其他收入
other_revenue = total_revenue - media_rights - sum(sponsors.values()) - sum(partners.values())

# 创建画布
plt.figure(figsize=(12, 10))

# 准备条形图数据
categories = ["媒体版权", "冠名商赞助", "官方合作伙伴", "其他"]
values = [media_rights, sum(sponsors.values()), sum(partners.values()), other_revenue]
colors = ['#4e79a7', '#f28e2b', '#e15759', '#76b7b2']

# 绘制主条形图 - 各类收入占比
plt.subplot(2, 1, 1)
bars = plt.bar(categories, values, color=colors)
plt.title('中超公司营收分布（按类别）')
plt.ylabel('金额 (亿元)')

# 在条形上添加数值标签
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.2f} 亿元 ({height/total_revenue*100:.1f}%)',
             ha='center', va='bottom')

# 绘制赞助商和合作伙伴详细条形图
plt.subplot(2, 1, 2)

# 合并赞助商和合作伙伴数据
sponsor_names = list(sponsors.keys())
sponsor_values = list(sponsors.values())
partner_names = list(partners.keys())
partner_values = list(partners.values())

# 设置条形位置
x_sponsor = np.arange(len(sponsor_names))
x_partner = np.arange(len(partner_names)) + len(sponsor_names) + 1

# 绘制赞助商条形
plt.bar(x_sponsor, sponsor_values, width=0.6, label='赞助商', color='#59a14f')
# 绘制合作伙伴条形
plt.bar(x_partner, partner_values, width=0.6, label='合作伙伴', color='#af7aa1')

# 设置x轴标签和刻度
plt.xticks(list(x_sponsor) + list(x_partner), sponsor_names + partner_names, rotation=45, ha='right')
plt.title('赞助商和合作伙伴详细收入')
plt.ylabel('金额 (亿元)')
plt.legend()

# 在条形上添加数值标签
for i, v in enumerate(sponsor_values):
    plt.text(x_sponsor[i], v + 0.02, f'{v:.2f}', ha='center')
for i, v in enumerate(partner_values):
    plt.text(x_partner[i], v + 0.02, f'{v:.2f}', ha='center')

plt.tight_layout()
plt.show()