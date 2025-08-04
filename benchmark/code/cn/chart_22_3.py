import matplotlib.pyplot as plt
import numpy as np

# 冠名商数据
sponsors = {
    "中国平安": 1.815,
    "耐克": 1,
    "福特": 0.4,
    "京东": 0.35,
    "嘉士伯": 0.2,
    "DHL": 0.2,
    "红牛": 0.2
}

# 创建画布
plt.figure(figsize=(12, 8))

# 冠名商赞助柱状图
sponsor_names = list(sponsors.keys())
sponsor_values = list(sponsors.values())
bars = plt.bar(sponsor_names, sponsor_values, color='#66b3ff')
plt.title('冠名商赞助金额')
plt.xlabel('冠名商')
plt.ylabel('金额（亿）')
plt.xticks(rotation=45)

# 添加数值标签
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.3f}',
             ha='center', va='bottom')

plt.tight_layout()
plt.show()