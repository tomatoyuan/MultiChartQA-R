import matplotlib.pyplot as plt
import numpy as np

# 收益来源
labels = ["流量分成(如平台广告共享计划分成)", "私人接单(如提供个性化定制等服务)", "内容营销(如品牌合作种草推广)", 
          "电商带货(图文/视频/直播带货等)", "知识付费(如教授付费课程，提供付费内容等)", "其他来源"]
# 对应数据
sizes = [46.2, 44.5, 18.9, 16.5, 13.9, 12.0]
# 颜色设置，尽量贴近原图绿色系
colors = ["#A4C639"] * len(labels)

x = np.arange(len(labels))  # 用于设置x轴位置
bar_width = 0.5  # 柱状图宽度

fig, ax = plt.subplots()
# 绘制柱状图
bars = ax.bar(x, sizes, width=bar_width, color=colors, edgecolor="white")  

# 添加数据标签
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 标签距离柱状图的垂直距离
                textcoords="offset points",
                ha='center', va='bottom')

# 设置x轴刻度和标签，旋转标签让其显示更美观
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha="right")
# 设置y轴标签（原图表未显示y轴标签，可根据需求决定是否添加）
# ax.set_ylabel("占比（%）")
# 设置图表标题
ax.set_title("中国及海外实现内容变现的创作者的主要收益来源")

# 美化图表，隐藏顶部和右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局，避免标签显示不全
plt.show()