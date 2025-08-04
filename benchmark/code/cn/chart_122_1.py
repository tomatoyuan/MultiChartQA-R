import matplotlib.pyplot as plt
import numpy as np

# 数据
sources = [
    "亲朋好友介绍", "短视频平台", "内容分享类平台", 
    "通过参加别人的婚礼认识", "婚庆类网站/APP", "网络搜索", "广告宣传"
]
proportions = [43.8, 43.5, 38.8, 37.9, 36.5, 27.1, 25.9]

y = np.arange(len(sources))

fig, ax = plt.subplots(figsize=(8, 5))
# 绘制水平柱状图
bars = ax.barh(y, proportions, color='orange')

# 添加数值标注
for i, proportion in enumerate(proportions):
    ax.text(proportion + 1, i, f'{proportion}%', va='center', ha='left', fontsize=9)

# 设置y轴刻度和标签
ax.set_yticks(y)
ax.set_yticklabels(sources)
ax.set_xlabel('占比（%）')
ax.set_title('中国婚庆公司信息来源调查')

plt.tight_layout()
plt.show()