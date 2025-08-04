import matplotlib.pyplot as plt
import numpy as np

# 左侧饼图数据
pie_labels = ["重点关注过", "看到过但没深入了解", "没关注过"]
pie_sizes = [53.4, 42.2, 4.4]
pie_colors = ["#FF9933", "#B34D4D", "#4D88B3"]

# 右侧柱状图数据
bar_channels = ["电商平台", "社交平台", "短视频平台", "内容分享平台", "线下专卖店", "智能产品展览会", 
                "朋友/亲人/同学告知", "其他"]
bar_proportions = [60.2, 53.4, 41.4, 41.2, 32.5, 17.1, 9.6, 0.4]

fig = plt.figure(figsize=(16, 6))
# 左侧子图
ax1 = fig.add_subplot(121)
wedges, texts, autotexts = ax1.pie(pie_sizes, labels=pie_labels, colors=pie_colors, autopct="%1.1f%%", 
                                   startangle=90, hatch="////")
for autotext in autotexts:
    autotext.set_color("black")
ax1.set_title("中国消费者对小屏手机的了解情况")

# 右侧子图
ax2 = fig.add_subplot(122)
x = np.arange(len(bar_channels))
bars = ax2.bar(x, bar_proportions, color="#FF9933", hatch="////")
for i, proportion in enumerate(bar_proportions):
    ax2.text(i, proportion + 1, f"{proportion}%", ha="center", va="bottom")
ax2.set_ylabel("占比（%）")
ax2.set_xlabel("了解渠道")
ax2.set_xticks(x)
ax2.set_xticklabels(bar_channels, rotation=45)
ax2.set_title("中国消费者了解小屏手机的渠道")

plt.tight_layout()
plt.show()