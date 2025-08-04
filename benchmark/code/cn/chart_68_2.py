import matplotlib.pyplot as plt
import numpy as np

# 模拟数据（与原图趋势一致）
years = ["2017", "2018", "2019", "2020", "2021", "2022e", "2023e", "2024e"]
market_size = np.array([2, 4, 8, 15, 16, 18, 22, 30])  # 市场规模（亿元）
growth_rate = np.array([136.6, 101.1, 89.4, 10.3, 12.0, 23.7, 33.4])  # 增长率（%），注意长度比 years 少1（2017无增长率）

# 初始化双轴画布
fig, ax1 = plt.subplots(figsize=(12, 6))
ax2 = ax1.twinx()

# 绘制柱状图（市场规模）
x = np.arange(len(years))
bar_width = 0.6
rects = ax1.bar(x, market_size, width=bar_width, label="中国实时音视频（RTC）PaaS市场规模（亿元）", color="#A4C639")

# 绘制折线图（增长率）
line, = ax2.plot(x[1:], growth_rate, marker="o", color="#42A5F5", label="中国实时音视频（RTC）PaaS市场规模增长率", linewidth=2)

# 添加市场规模标注（柱状图顶部）
for rect in rects:
    height = rect.get_height()
    ax1.annotate(f'{height}', 
                 xy=(rect.get_x() + rect.get_width()/2, height),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom', fontsize=9)

# 添加增长率标注（折线图点上方）
for i, rate in enumerate(growth_rate):
    ax2.annotate(f'{rate}%', 
                 xy=(x[i+1], rate),  # x 从2018开始（索引1）
                 xytext=(0, 5),
                 textcoords="offset points",
                 ha='center', va='bottom', fontsize=9, color="#42A5F5")

# 添加 CAGR 标注（手动模拟箭头和文本）
ax1.annotate(
    "CAGR=77.6%", 
    xy=(0.2, 0.8), xycoords="axes fraction",
    xytext=(0.2, 0.9), textcoords="axes fraction",
    arrowprops=dict(facecolor='gray', width=1, headwidth=6),
    fontsize=10, ha='center'
)
ax1.annotate(
    "CAGR=28.4%", 
    xy=(0.7, 0.8), xycoords="axes fraction",
    xytext=(0.7, 0.9), textcoords="axes fraction",
    arrowprops=dict(facecolor='gray', width=1, headwidth=6),
    fontsize=10, ha='center'
)

# 坐标轴与图例配置
ax1.set_xticks(x)
ax1.set_xticklabels(years, fontsize=10)
ax1.set_ylabel("市场规模（亿元）", fontsize=11, color="#A4C639")
ax2.set_ylabel("增长率（%）", fontsize=11, color="#42A5F5")

# 合并图例（解决双轴图例重叠问题）
handles, labels = ax1.get_legend_handles_labels()
handles.append(line)
labels.append(line.get_label())
ax1.legend(handles, labels, loc="upper left", bbox_to_anchor=(0, 1.09), ncol=2, fontsize=9)

# 标题与美化
plt.title("2017-2024年中国实时音视频（RTC）PaaS市场规模及预测", fontsize=14, pad=30)
ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)
plt.tight_layout()

# 显示图表
plt.show()