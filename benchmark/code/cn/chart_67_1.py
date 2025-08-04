import matplotlib.pyplot as plt
import numpy as np

# 模拟数据（与原图趋势一致，数值近似）
cities = [
    "北京", "上海", "广州", "深圳", "天津", 
    "沈阳", "大连", "南京", "杭州", "青岛", 
    "武汉", "重庆", "成都", "西安"
]
stock = np.array([849, 833.3, 561.7, 637.8, 238.5, 121.2, 98.1, 237.8, 230.7, 160.1, 257.2, 182.9, 270.4, 280.8])  # 存量
net_absorption = np.array([34.1, 53.1, 42.6, 64.1, 12.9, 3.5, 2.4, 22.2, 6.4, 9.7, 17.1, 11.3, 19.7, 12.6])  # 净吸纳量
vacancy_rate = np.array([10, 10, 8, 19, 29, 33, 32, 22, 16, 24, 35, 28, 13, 22])  # 空置率

# 初始化画布（宽高与原图适配）
fig, ax1 = plt.subplots(figsize=(12, 6))
ax2 = ax1.twinx()  # 双坐标轴

# 绘制柱状图（存量 + 净吸纳量）
x = np.arange(len(cities))
width = 0.6
# 存量柱状图
rects_stock = ax1.bar(x, stock, width, label="2021年核心商圈存量（万平方米）", color="#8BC34A")
# 净吸纳量柱状图（叠加在存量底部，用较小尺寸模拟“蓝色小条”）
rects_absorption = ax1.bar(x, net_absorption, width, bottom=0, label="2021年核心商圈净吸纳量（万平方米）", color="#42A5F5")

# 绘制折线图（空置率）
line_vacancy, = ax2.plot(x, vacancy_rate, marker="o", color="#7CB342", label="2021年核心商圈空置率（%）", linewidth=2)

# 添加数据标注（存量、净吸纳量、空置率）
for rect in rects_stock:
    height = rect.get_height()
    ax1.annotate(f'{height}', 
                 xy=(rect.get_x() + rect.get_width()/2, height),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom', fontsize=9)
for rect in rects_absorption:
    height = rect.get_height()
    ax1.annotate(f'{height}', 
                 xy=(rect.get_x() + rect.get_width()/2, height/2 + 5),  # 标注在蓝色条中间
                 xytext=(0, 0),
                 textcoords="offset points",
                 ha='center', va='center', fontsize=9, color='white')
for i, rate in enumerate(vacancy_rate):
    ax2.annotate(f'{rate}%', 
                 xy=(x[i], rate),
                 xytext=(0, 5),
                 textcoords="offset points",
                 ha='center', va='bottom', fontsize=9, color="black")

# 坐标轴与图例配置
ax1.set_xticks(x)
ax1.set_xticklabels(cities, fontsize=10, rotation=45)
ax1.set_ylabel("存量/净吸纳量（万平方米）", fontsize=11, color="#8BC34A")
ax2.set_ylabel("空置率（%）", fontsize=11, color="#7CB342")

# 合并图例（解决双轴图例重叠问题）
handles, labels = ax1.get_legend_handles_labels()
handles.append(line_vacancy)
labels.append(line_vacancy.get_label())
ax1.legend(handles, labels, loc="upper left", bbox_to_anchor=(0, 1.05), ncol=3, fontsize=9)

# 标题与美化
plt.title("2021年中国主要一二线城市核心商圈甲级写字楼市场规模及空置率", fontsize=14, pad=20)
ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)
plt.tight_layout()

# 显示图表
plt.show()