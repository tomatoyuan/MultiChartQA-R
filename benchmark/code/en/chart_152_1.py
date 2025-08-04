import matplotlib.pyplot as plt
import numpy as np

# 构造时间序列
dates = np.arange('2023-09-01', '2023-12-28', dtype='datetime64[D]')
np.random.seed(0)
base = np.linspace(10, 80, len(dates)) + np.random.normal(0, 5, len(dates))

# 人工制造峰值
spikes = {
    '2023-09-25': 100,
    '2023-10-16': 85,
    '2023-11-07': 90,
    '2023-12-13': 105
}
for date, value in spikes.items():
    idx = np.where(dates == np.datetime64(date))[0][0]
    base[idx] = value

# 创建图表
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(dates, base, label='Average Value', color='dodgerblue')

# 高亮点
highlight_dates = list(spikes.keys())
highlight_vals = [spikes[d] for d in highlight_dates]
ax.scatter(highlight_dates, highlight_vals, color='orange', zorder=5, label='High Points')

# 添加注释（避免遮挡标题）
for i, (date, value) in enumerate(zip(highlight_dates, highlight_vals)):
    ax.annotate("Intensive Market Action Period\nIndex: " + str(value),
                xy=(np.datetime64(date), value),
                xytext=(0, 50 + i * 10),  # 增加偏移，避免标题遮挡
                textcoords='offset points',
                arrowprops=dict(arrowstyle="->", color='deeppink'),
                fontsize=9, color='deeppink')

# 样式优化
ax.set_title("SIINSIIN Brand Empowers the Shark Pants Market", fontsize=14, pad=50)
ax.set_ylabel("Search Index")
ax.legend(loc='upper left')  # 移动图例位置，避免遮挡右侧注释
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.subplots_adjust(top=1.0)  # 给标题腾出空间
plt.show()