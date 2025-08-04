import matplotlib.pyplot as plt
import numpy as np

# 左侧：中国投资者获取投资理财信息的途径数据
left_labels = [
    "银行/证券机构理财经理等专业投资人士", "家人、朋友等社会关系", 
    "投资类app", "自媒体、社交媒体等", 
    "官方的文件、公告、数据等", "其他（财经类网站、新闻app、数据库等）"
]
left_proportions = [56.01, 38.37, 36.24, 34.11, 33.91, 0.97]

# 右侧：中国投资者使用投资类APP的类型数据
right_labels = [
    "支付宝、微信等第三方支付平台", "证券公司自有app", 
    "同花顺等第三方互联网金融平台"
]
right_proportions = [75.94, 68.45, 51.34]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# 绘制左侧获取信息途径的水平柱状图
y1 = np.arange(len(left_labels))
ax1.barh(y1, left_proportions, color='orange')
ax1.set_yticks(y1)
ax1.set_yticklabels(left_labels)
ax1.set_xlabel('占比（%）')
ax1.set_title('中国投资者获取投资理财信息的途径')
# 添加左侧数值标注
for i, proportion in enumerate(left_proportions):
    ax1.text(proportion + 1, i, f'{proportion}%', va='center')

# 绘制右侧使用APP类型的水平柱状图
y2 = np.arange(len(right_labels))
ax2.barh(y2, right_proportions, color='orange')
ax2.set_yticks(y2)
ax2.set_yticklabels(right_labels)
ax2.set_xlabel('占比（%）')
ax2.set_title('中国投资者使用投资类APP的类型')
# 添加右侧数值标注
for i, proportion in enumerate(right_proportions):
    ax2.text(proportion + 1, i, f'{proportion}%', va='center')

plt.tight_layout()
plt.show()