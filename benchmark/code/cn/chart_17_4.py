import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import matplotlib.colors as mcolors
import numpy as np

# 提取图表内容
cases = [
    {
        "date": datetime(2024, 8, 21),
        "desc": "18岁大学新生徐玉玉\n被骗9900元致心脏骤停离世",
        "severity": "极高",  # 新增严重程度字段
        "color": "#e41a1c"  # 新增颜色映射
    },
    {
        "date": datetime(2024, 8, 23),
        "desc": "山东理工大二学生宋某\n因电信诈骗损失1996元导致猝死",
        "severity": "高",
        "color": "#ff7f00"
    },
    {
        "date": datetime(2024, 8, 29),
        "desc": "清华大学一教师遭电信诈骗\n涉案金额高达1760万元",
        "severity": "中",
        "color": "#4daf4a"
    },
    {
        "date": datetime(2024, 8, 31),
        "desc": "广东揭阳19岁女生蔡某妍\n被短信诈骗10000多元学费和生活费后跳海轻生",
        "severity": "高",
        "color": "#ff7f00"
    },
    {
        "date": datetime(2024, 9, 6),
        "desc": "吉林工商学院大二学生段某\n被骗5000元学费后轻生",
        "severity": "高",
        "color": "#ff7f00"
    }
]

# 拆分数据，方便绘图
dates = [case["date"] for case in cases]
descriptions = [case["desc"] for case in cases]
colors = [case["color"] for case in cases]
severities = [case["severity"] for case in cases]

# 创建画布
fig, ax = plt.subplots(figsize=(14, 8))
fig.patch.set_facecolor('#f8f9fa')  # 设置画布背景色
ax.set_facecolor('#ffffff')  # 设置绘图区背景色

# 绘制水平条形图，根据严重程度设置颜色
y_ticks = range(len(descriptions))
bars = ax.barh(y_ticks, [1]*len(descriptions), 
               left=mdates.date2num(dates), 
               height=0.6, 
               color=colors,
               alpha=0.8,
               edgecolor='black',
               linewidth=0.5)

# 添加数据标签
for i, (date, bar) in enumerate(zip(dates, bars)):
    ax.text(mdates.date2num(date) + 0.1, i, 
            date.strftime('%m-%d'), 
            va='center', 
            fontsize=10,
            fontweight='bold')

# 设置x轴为日期格式
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))  # 间隔2天显示一个刻度
ax.set_xlabel("日期", fontsize=12, fontweight='bold')
ax.set_xlim(mdates.date2num(min(dates)) - 1, mdates.date2num(max(dates)) + 2)  # 调整x轴范围

# 设置y轴为案例描述
ax.set_yticks(y_ticks)
ax.set_yticklabels(descriptions, fontsize=10)

# 添加标题
ax.set_title("电信诈骗典型案例时间线", fontsize=18, fontweight="bold", pad=20)
ax.title.set_color('#333333')

# 添加网格
ax.grid(axis="x", linestyle="--", alpha=0.6, color='#cccccc')

# 添加严重程度图例
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label='极高',
                          markerfacecolor='#e41a1c', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='高',
                          markerfacecolor='#ff7f00', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='中',
                          markerfacecolor='#4daf4a', markersize=10)]

ax.legend(handles=legend_elements, title='案件严重程度', loc='lower right')

# 添加底部注释
plt.figtext(0.5, 0.01, '数据来源：公开报道整理', ha='center', fontsize=9, color='#666666')

# 优化布局
plt.tight_layout()
plt.subplots_adjust(bottom=0.08)  # 调整底部边距
plt.show()