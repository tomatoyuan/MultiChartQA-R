import matplotlib.pyplot as plt
import numpy as np

# 年龄段
ages = ["00后", "95后", "90后", "85后", "80后", "75后", "70后", "70前"]
# 总体送礼人群比例（柱状图）
total_gift_pct = [11, 17, 25, 18, 15, 8, 7, 4]
# 送健康礼TGI（折线图）
health_gift_tgi = [105, 90, 101, 106, 103, 99, 97, 93]

x = np.arange(len(ages))
width = 0.6

fig, ax1 = plt.subplots(figsize=(10, 6))

# 柱状图（左轴）
bars = ax1.bar(x, total_gift_pct, width=width, color='lightcoral', label='总体送礼人群')
ax1.set_ylabel('总体送礼人群占比', fontsize=12)
ax1.set_ylim(0, 30)
ax1.set_xticks(x)
ax1.set_xticklabels(ages, fontsize=10)
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}%', xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3), textcoords="offset points", ha='center', fontsize=10)

# 折线图（右轴）
ax2 = ax1.twinx()
line, = ax2.plot(x, health_gift_tgi, color='firebrick', marker='o', label='送健康礼TGI')
ax2.set_ylabel('送健康礼TGI', fontsize=12)
ax2.set_ylim(80, 110)
for i, v in enumerate(health_gift_tgi):
    ax2.text(x[i], v + 1, str(v), color='firebrick', ha='center', fontsize=10)

# 合并图例（修复方式）
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
fig.legend(handles1 + handles2, labels1 + labels2, loc='upper right', fontsize=10)

# 标题与布局
fig.suptitle('新年送礼人群年龄代际分布', fontsize=14, fontweight='bold')
fig.tight_layout()
plt.show()