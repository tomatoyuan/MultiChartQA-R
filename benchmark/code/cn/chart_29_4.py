import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# 每小时的搜索热度数据（单位：万）
hours = list(range(25))  # 0-24时
heat_data = [
    1100, 1100, 1100, 1100, 1100,  # 0-4时
    1500, 2000, 2800, 3200, 2800,  # 5-9时
    2300, 2000, 1800, 2200, 2700,  # 10-14时
    3000, 3100, 2800, 2200, 1600,  # 15-19时
    1200, 1250, 1320, 1200, 1100   # 20-24时
]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(14, 7), facecolor='#f8f9fa')
ax.set_facecolor('#f8f9fa')

# 使用三次样条插值生成平滑曲线
x_smooth = np.linspace(min(hours), max(hours), 500)
spl = make_interp_spline(hours, heat_data, k=3)
heat_smooth = spl(x_smooth)

# 绘制平滑曲线，添加渐变色填充
line, = ax.plot(x_smooth, heat_smooth, linestyle='-', color='#1a73e8', linewidth=3)
ax.fill_between(x_smooth, heat_smooth, 0, alpha=0.1, color='#1a73e8')

# 添加参考水平线，优化线条样式
ax.axhline(y=1100, color='#9aa0a6', linestyle='--', alpha=0.7, linewidth=1.5)
ax.axhline(y=3300, color='#9aa0a6', linestyle='--', alpha=0.7, linewidth=1.5)

# 添加标题和标签，优化字体和位置
ax.set_title('世界杯搜索热度24小时趋势图', fontsize=18, pad=20, fontweight='bold', color='#202124')
ax.set_xlabel('时间（小时）', fontsize=14, labelpad=10, color='#3c4043')
ax.set_ylabel('搜索热度（万）', fontsize=14, labelpad=10, color='#3c4043')

# 设置x轴刻度，优化显示格式
ax.set_xticks(hours[::4])
ax.set_xticklabels([f'{h}时' for h in hours[::4]], fontsize=12)
ax.set_xlim(0, 24)
ax.set_ylim(0, 4000)

# 设置y轴刻度，优化显示格式
ax.set_yticks(np.arange(0, 4500, 500))
ax.set_yticklabels([f'{y}' for y in np.arange(0, 4500, 500)], fontsize=12)

# 添加网格线，优化样式
ax.grid(True, linestyle='--', alpha=0.4, color='#9aa0a6')

# 添加原始数据点，优化样式
ax.scatter(hours, heat_data, color='#1a73e8', s=50, zorder=5, edgecolor='white', linewidth=1)

# 为关键时间点添加数据标签，优化样式和位置
for x, y in zip(hours[::4], heat_data[::4]):
    ax.annotate(f'{y}', (x, y), textcoords='offset points',
                xytext=(0, 12), ha='center', fontsize=11, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='#dadce0', alpha=0.8))

# 突出显示峰值和谷值，优化样式
peak_idx = np.argmax(heat_data)
valley_idx = np.argmin(heat_data)
ax.scatter([hours[peak_idx], hours[valley_idx]], 
           [heat_data[peak_idx], heat_data[valley_idx]], 
           color='#ea4335', s=100, zorder=5, edgecolor='white', linewidth=1.5)

# 添加峰值和谷值的注释，优化样式
ax.annotate(f'峰值: {heat_data[peak_idx]}万', (hours[peak_idx], heat_data[peak_idx]),
            textcoords='offset points', xytext=(30, 20), ha='left', fontsize=12,
            arrowprops=dict(arrowstyle='->', color='#ea4335', linewidth=1.5))

ax.annotate(f'谷值: {heat_data[valley_idx]}万', (hours[valley_idx], heat_data[valley_idx]),
            textcoords='offset points', xytext=(-30, -30), ha='right', fontsize=12,
            arrowprops=dict(arrowstyle='->', color='#ea4335', linewidth=1.5))

# 添加时间区域提示，优化样式
ax.axvspan(5, 9, alpha=0.05, color='#4285f4', label='早间高峰')
ax.axvspan(15, 17, alpha=0.05, color='#4285f4')
ax.text(7, 3800, '早间高峰', ha='center', fontsize=12, color='#202124', 
        bbox=dict(boxstyle='round,pad=0.2', fc='#4285f4', alpha=0.1))
ax.text(16, 3800, '晚间高峰', ha='center', fontsize=12, color='#202124', 
        bbox=dict(boxstyle='round,pad=0.2', fc='#4285f4', alpha=0.1))

# 优化坐标轴样式
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#dadce0')
ax.spines['bottom'].set_color('#dadce0')
ax.tick_params(axis='both', which='major', labelsize=12, color='#9aa0a6')

# 添加图例，优化样式
ax.legend([line], ['搜索热度趋势'], loc='upper right', frameon=True, 
          framealpha=0.9, edgecolor='#dadce0', fontsize=12)

# 添加水印，优化样式
fig.text(0.85, 0.15, '数据可视化', fontsize=30, color='#e0e0e0', 
         ha='center', va='center', rotation=30, alpha=0.3)

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()