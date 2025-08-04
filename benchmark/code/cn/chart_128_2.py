import matplotlib.pyplot as plt
import numpy as np

# 企业名称
companies = ["三星", "腾讯", "百度", "索尼", "OPPO", "平安集团", "商汤科技", "佳能", "华为", "微软"]
# 专利数量（项）
patent_counts = [4094, 4085, 3094, 2637, 2301, 2260, 2194, 2163, 2126, 2108]

x = np.arange(len(companies))

fig, ax = plt.subplots(figsize=(12, 7))
# 绘制柱状图
bars = ax.bar(x, patent_counts, color='orange', label='专利数（项）')

# 添加数值标注，在柱子上方
for i, count in enumerate(patent_counts):
    ax.text(i, count + 50, f'{count}', ha='center', va='bottom')

ax.set_ylabel('专利数（项）')
ax.set_xlabel('企业名称')
ax.set_xticks(x)
ax.set_xticklabels(companies, rotation=45)  # 旋转 x 轴标签避免重叠
ax.legend()
ax.set_title('全球VR/AR发明专利数量（Top10企业）')

plt.tight_layout()
plt.show()