import matplotlib.pyplot as plt
import numpy as np

# 构造时间序列
dates = np.arange('2023-09-01', '2023-12-28', dtype='datetime64[D]')
np.random.seed(0)
base = np.linspace(10, 80, len(dates)) + np.random.normal(0, 5, len(dates))

# 人工制造几个高峰模拟“密集市场动作”
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
ax.plot(dates, base, label='平均值', color='dodgerblue')

# 添加高点标注点
highlight_dates = list(spikes.keys())
highlight_vals = [spikes[d] for d in highlight_dates]
ax.scatter(highlight_dates, highlight_vals, color='orange', zorder=5, label='高点')

# 添加注释（箭头 + 描述 + 数值）
for i, (date, value) in enumerate(zip(highlight_dates, highlight_vals)):
    ax.annotate("SIINSIIN密集市场动作时期\n指数：" + str(value),
                xy=(np.datetime64(date), value),
                xytext=(0, 40 + i * 10),
                textcoords='offset points',
                arrowprops=dict(arrowstyle="->", color='deeppink'),
                fontsize=9, color='deeppink')

# 样式设置
ax.set_title("SIINSIIN品牌赋能鲨鱼裤市场", fontsize=14)
ax.set_ylabel("搜索指数")
ax.legend()
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()