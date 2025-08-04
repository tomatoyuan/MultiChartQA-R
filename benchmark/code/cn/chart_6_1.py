import matplotlib.pyplot as plt
import numpy as np

# 日期列表
dates = ["5/1", "5/2", "5/3", "5/4", "5/5", "5/6", "5/7", "5/8", "5/9", "5/10", 
         "5/11", "5/12", "5/13", "5/14", "5/15", "5/16", "5/17", "5/18", "5/19", 
         "5/20", "5/21", "5/22", "5/23", "5/24", "5/25", "5/26", "5/27", "5/28", 
         "5/29", "5/30", "5/31"]
# 法律服务搜索量（柱状，左轴）
legal_service = [1200000, 1100000, 1200000, 1300000, 1400000, 1800000, 2000000, 
                 1900000, 1950000, 1900000, 1800000, 1850000, 1500000, 
                 1400000, 1300000, 1800000, 1700000, 1750000, 1400000, 
                 1350000, 1300000, 2200000, 1200000, 1350000, 1800000, 
                 1850000, 1900000, 1500000, 1400000, 1450000, 2000000]
# 房产纠纷占比（近似%）列表
property_dispute = [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 
                    0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 
                    0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.5]
# 离婚诉讼占比（近似%）列表
divorce_lawsuit = [5.2, 5.0, 4.9, 4.8, 4.7, 4.6, 5.5, 5.0, 4.6, 4.5, 
                   4.4, 4.3, 3.2, 3.3, 3.4, 3.5, 3.4, 3.3, 3.0, 3.1, 
                   3.2, 5.0, 4.5, 4.0, 3.2, 3.3, 3.4, 4.5, 4.3, 4.2, 4.0]

# 创建画布与双轴
fig, ax1 = plt.subplots(figsize=(14, 8))  # 主轴（左轴）
ax2 = ax1.twinx()  # 次轴（右轴，占比）

# 绘制法律服务（柱状图，左轴）
x = np.arange(len(dates))  # 横坐标索引
bars = ax1.bar(x, legal_service, color='blue', label='法律服务', width=0.6)
ax1.set_ylabel('搜索量', color='blue', fontsize=12)
ax1.set_ylim(0, 2500000)  # 匹配原图左轴范围
ax1.tick_params(axis='y', labelcolor='blue')

# 绘制房产纠纷、离婚诉讼（折线图，右轴）
line1, = ax2.plot(x, property_dispute, color='orange', label='房产纠纷', marker='o', linestyle='-', linewidth=2)
line2, = ax2.plot(x, divorce_lawsuit, color='green', label='离婚诉讼', marker='o', linestyle='-', linewidth=2)
ax2.set_ylabel('占比（%）', color='black', fontsize=12)
ax2.set_ylim(0, 6)  # 匹配原图右轴范围（0%-6%）
ax2.tick_params(axis='y', labelcolor='black')

# 横坐标与图例设置
ax1.set_xticks(x)
ax1.set_xticklabels(dates, rotation=45, fontsize=10)  # 倾斜日期避免重叠
ax1.set_title('5月法律服务行业搜索关注度趋势及细分行业占比', fontsize=14, pad=20)

# 为柱状图添加数据标注（搜索量）
for i, bar in enumerate(bars):
    height = bar.get_height()
    # 每隔3天显示一次标注，避免过于密集
    if i % 3 == 0:
        ax1.annotate(f'{height:,}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 5),  # 向上偏移5点
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=9,
                    color='blue',
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="blue", alpha=0.7))

# 为房产纠纷折线图添加数据标注
for i, (x_val, y_val) in enumerate(zip(x, property_dispute)):
    # 只标注有变化的点和关键节点
    if y_val != 0.3 or i % 7 == 0 or i == len(x)-1:
        ax2.annotate(f'{y_val}%',
                    xy=(x_val, y_val),
                    xytext=(0, -15),  # 向下偏移
                    textcoords="offset points",
                    ha='center', va='top',
                    fontsize=9,
                    color='orange',
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="orange", alpha=0.7))

# 为离婚诉讼折线图添加数据标注
for i, (x_val, y_val) in enumerate(zip(x, divorce_lawsuit)):
    # 只标注峰值、谷值和关键节点
    if i == 0 or i == len(x)-1 or i % 5 == 0 or \
       (i > 0 and i < len(x)-1 and 
        (y_val > divorce_lawsuit[i-1] and y_val > divorce_lawsuit[i+1]) or 
        (y_val < divorce_lawsuit[i-1] and y_val < divorce_lawsuit[i+1])):
        ax2.annotate(f'{y_val}%',
                    xy=(x_val, y_val),
                    xytext=(0, 10),  # 向上偏移
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=9,
                    color='green',
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="green", alpha=0.7))

# 合并图例（双轴图例统一展示）
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left', fontsize=10)

# 添加网格线提高可读性
ax1.grid(True, linestyle='--', alpha=0.3)

# 优化布局
plt.tight_layout()
plt.show()