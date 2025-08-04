import matplotlib.pyplot as plt
import numpy as np

# 资讯渠道
channels = ["微博/微信", "抖音/快手等短视频", "今日头条、百家号等资讯平台", "广播电视", 
            "财经媒体官网", "报纸/杂志", "财经媒体客户端", "财经博客/个人网站", 
            "专业财经数据提供商（Wind资讯、同花顺等）"]
# 对应占比（%）
proportions = [45.61, 44.08, 43.97, 34.32, 31.91, 24.67, 24.23, 18.64, 13.27]

x = np.arange(len(channels))  # x轴坐标

fig, ax = plt.subplots(figsize=(10, 6))
# 绘制柱状图
bars = ax.bar(x, proportions, color='orange')

# 添加数值标注
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# 设置x轴刻度和标签，旋转标签
ax.set_xticks(x)
ax.set_xticklabels(channels, rotation=45, ha='right')
ax.set_ylabel('占比（%）')
ax.set_title('2025年中国财经新闻用户获取财经媒体资讯渠道')

plt.tight_layout()
plt.show()