import matplotlib.pyplot as plt
import numpy as np

# 数据
labels = [
    "品牌建立与认知度提升", "营销资源获取与营销活动开展", "稳定资金链的保障",
    "战略制定", "销售渠道搭建与运营", "用户获取与销售转化", "产品创新与本地化"
]
x = np.arange(len(labels))  # 横坐标位置
width = 0.35  # 柱宽

# 新锐出海企业数据和成熟出海企业数据
xinrui = [9, 19, 20, 24, 20, 22, 22]
chengshu = [12, 6, 9, 9, 16, 21, 22]

# 绘图
fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.barh(x - width/2, xinrui, width, label='新锐出海企业', color='#0072CE')
bars2 = ax.barh(x + width/2, chengshu, width, label='成熟出海企业', color='#7EC0EE')

# 添加数值标签
for bar in bars1 + bars2:
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
            f'{bar.get_width()}%', va='center', fontsize=9)

# 坐标轴和标签
ax.set_yticks(x)
ax.set_yticklabels(labels, fontsize=10)
ax.invert_yaxis()  # 颠倒Y轴
ax.set_xlabel('比例（%）')
ax.set_title('不同类型出海企业面临的出海挑战不同')
ax.legend()



plt.tight_layout()
plt.show()