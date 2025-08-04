import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# 构建数据
data = {
    '月份': ['202401', '202402', '202403', '202404', '202405', '202406', 
            '202407', '202408', '202409', '202410', '202411', '202412', '202501'],
    '销售额（十亿）': [8, 7, 10, 9, 11, 10, 9, 9, 10, 13, 12, 9, 10],
    '成交均价': [10, 11, 7, 8, 8, 8, 4, 6, 9, 10, 10, 8, 10]
}
df = pd.DataFrame(data)

# 将月份转换为日期格式用于更好的显示
df['日期'] = df['月份'].apply(lambda x: datetime.strptime(x, '%Y%m'))

# 创建双坐标轴
fig, ax1 = plt.subplots(figsize=(14, 7))  # 增大图表尺寸
ax2 = ax1.twinx()

# 设置图表背景和网格
fig.patch.set_facecolor('#f8f9fa')  # 浅灰色背景
ax1.set_facecolor('#ffffff')  # 白色绘图区
ax1.grid(True, linestyle='--', alpha=0.7)  # 添加网格线

# 绘制销售额柱状图 - 使用渐变色和阴影效果
bar_width = 0.6
bars = ax1.bar(df['日期'], df['销售额（十亿）'], width=bar_width, 
               color='#3274A1', edgecolor='#285F8F', alpha=0.9, 
               label='销售额（十亿）', zorder=3)  # zorder控制图层顺序

# 为柱状图添加数值标签
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 0.15,
             f'{height}', ha='center', va='bottom', fontsize=9)

# 绘制成交均价折线图 - 使用平滑曲线和标记点
line, = ax2.plot(df['日期'], df['成交均价'], color='#E1812C', 
                label='成交均价', linewidth=2.5, marker='o', markersize=7,
                markeredgecolor='white', markeredgewidth=1, zorder=4)

# 为折线图添加数值标签
for x, y in zip(df['日期'], df['成交均价']):
    ax2.annotate(f'{y}', (x, y), textcoords='offset points',
                xytext=(0, 8), ha='center', fontsize=9)

# 设置坐标轴标签和标题
ax1.set_xlabel('月份', fontsize=12)
ax1.set_ylabel('销售额（十亿）', color='#3274A1', fontsize=12)
ax2.set_ylabel('成交均价', color='#E1812C', fontsize=12)

# 设置标题和副标题
plt.suptitle('2024年保健食品相关行业逐月销售情况', fontsize=16, fontweight='bold', y=0.96)
plt.title('*部分主流货架电商与内容电商平台', fontsize=11, color='#666666', y=1.02)

# 格式化x轴日期显示
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
ax1.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
plt.xticks(rotation=45, ha='right', fontsize=10)

# 设置y轴范围
ax1.set_ylim(0, max(df['销售额（十亿）']) * 1.1)  # 留出10%的空间
ax2.set_ylim(0, max(df['成交均价']) * 1.1)

# 添加图例 - 使用更好的位置和样式
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, 
          loc='upper center', bbox_to_anchor=(0.5, -0.08),
          ncol=2, frameon=True, fancybox=True, shadow=True,
          fontsize=10)

# 添加注释 - 突出显示销售额最高的月份
max_sales_idx = df['销售额（十亿）'].idxmax()
ax1.annotate('销售额峰值', xy=(df['日期'][max_sales_idx], df['销售额（十亿）'][max_sales_idx]),
            xytext=(20, 30), textcoords='offset points',
            arrowprops=dict(arrowstyle='->', color='black'),
            fontsize=10)

# 调整布局
plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # 为底部和顶部的文本留出空间

# 显示图表
plt.show()