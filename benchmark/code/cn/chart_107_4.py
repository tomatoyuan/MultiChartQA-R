import matplotlib.pyplot as plt
import numpy as np

# 了解渠道
channels = ["报刊/书籍", "家人/朋友告知", "户外媒体（地铁，公交电视，机场广告等）", "科技展会/会议（通信展、科技论坛等）", 
            "内容分享平台（小红书、微博等）", "行业研究报告/分析（科技公司的研究报告、市场分析报告等）", "短视频平台（抖音、快手等）", 
            "电视/广播节目（新闻、科技频道等）", "手机应用推送（应用商店、新闻应用等）", "社交媒体平台（微信、QQ等）", 
            "电信运营商的推广活动（营业厅、线上线下的宣传活动等）"]
# 对应占比（%）
proportions = [12.67, 18.39, 23.13, 23.24, 23.79, 26.32, 27.64, 27.75, 28.52, 29.07, 34.69]

y = np.arange(len(channels))  # y轴坐标

fig, ax = plt.subplots(figsize=(12, 8))
# 绘制水平柱状图
bars = ax.barh(y, proportions, color='orange')

# 添加数值标注
for i, proportion in enumerate(proportions):
    ax.text(proportion, i, f'{proportion}', va='center', ha='left', fontsize=9)

# 设置y轴刻度和标签
ax.set_yticks(y)
ax.set_yticklabels(channels)
ax.set_xlabel('占比（%）')
ax.set_title('2025年中国用户对5G的了解渠道')

plt.tight_layout()
plt.show()