import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np

# 数据直接放在列表中（日期格式：'YYYY-MM-DD'，数值为完整数值）
dates = ['2025-05-01', '2025-05-02', '2025-05-03', '2025-05-04', '2025-05-05', '2025-05-06', '2025-05-07', '2025-05-08', '2025-05-09', '2025-05-10', '2025-05-11', '2025-05-12', '2025-05-13', '2025-05-14', '2025-05-15', '2025-05-16', '2025-05-17', '2025-05-18', '2025-05-19', '2025-05-20', '2025-05-21', '2025-05-22', '2025-05-23', '2025-05-24', '2025-05-25', '2025-05-26', '2025-05-27', '2025-05-28', '2025-05-29', '2025-05-30', '2025-05-31']
search_attention = [6200000, 6500000, 7000000, 9700000, 9500000, 8500000, 7200000, 9500000, 9500000, 9500000, 9500000, 9300000, 8800000, 7800000, 9000000, 10200000, 9800000, 9500000, 9200000, 8500000, 7800000, 7800000, 9000000, 9500000, 9500000, 9300000, 8800000, 7800000, 8500000, 9000000, 9500000]

# 将日期字符串转换为datetime对象
dates = [datetime.strptime(date, '%Y-%m-%d') for date in dates]

# 创建画布和子图，增加图表大小
fig, ax = plt.subplots(figsize=(15, 7))

# 设置背景样式
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#ffffff')

# 绘制折线图，添加透明度和标记点
line, = ax.plot(dates, search_attention, color='#1f77b4', linewidth=2.5, alpha=0.8, marker='o', markersize=5, markevery=3)

# 添加填充区域
ax.fill_between(dates, search_attention, 0, color='#1f77b4', alpha=0.1)

# 设置 x 轴为日期格式，每3天显示一个刻度
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=3))

# 设置图表标题和坐标轴标签，增加字体大小和样式
ax.set_title('5月职业培训行业搜索关注度趋势', fontsize=20, pad=20, fontweight='bold')
ax.set_ylabel('搜索关注度', fontsize=16, labelpad=15)
ax.set_xlabel('日期', fontsize=16, labelpad=15)

# 设置 y 轴刻度范围和格式，添加千位分隔符
ax.set_ylim(0, 12000000)
ax.yaxis.set_major_formatter(lambda x, pos: f'{int(x):,}')

# 添加网格线，设置样式
ax.grid(True, linestyle='--', alpha=0.5, color='#cccccc')

# 自定义刻度标签字体大小
ax.tick_params(axis='both', which='major', labelsize=12)

# 让 x 轴日期自动调整间距，避免重叠
fig.autofmt_xdate(rotation=45, ha='right')

# 添加最大值和最小值标注
max_val = max(search_attention)
min_val = min(search_attention)
max_idx = search_attention.index(max_val)
min_idx = search_attention.index(min_val)

ax.annotate(f'峰值: {max_val:,}',
            xy=(dates[max_idx], max_val),
            xytext=(dates[max_idx], max_val + 500000),
            arrowprops=dict(facecolor='red', shrink=0.05, width=1.5, headwidth=8),
            fontsize=12,
            ha='center')

ax.annotate(f'低谷: {min_val:,}',
            xy=(dates[min_idx], min_val),
            xytext=(dates[min_idx], min_val - 1000000),
            arrowprops=dict(facecolor='green', shrink=0.05, width=1.5, headwidth=8),
            fontsize=12,
            ha='center')

# 添加图例
ax.legend([line], ['搜索关注度'], loc='upper left', fontsize=12)

# 添加水印
fig.text(0.85, 0.15, '数据来源: 行业报告', fontsize=10, color='gray', alpha=0.7, ha='right')

# 优化布局
plt.tight_layout()

# 显示图表
plt.show()