import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2024e", "2025e", "2026e", "2027e", "2028e", "2029e"]

# 各技术投入数据（亿元），按 RPA/IPA、其他、AI、云、大数据 顺序
# 注意：最后一个值通过总和减去前面值计算，确保每层总和正确
tech_investment = np.array([
    [12.2, 25.8, 61.1, 117.9 - (12.2 + 25.8 + 61.1)],  # 2024e 总和: 12.2+25.8+61.1+18.8=117.9
    [14.6, 32.3, 73.7, 144.9 - (14.6 + 32.3 + 73.7)],  # 2025e 总和: 14.6+32.3+73.7+24.3=144.9
    [17.5, 40.3, 88.5, 177.2 - (17.5 + 40.3 + 88.5)],  # 2026e 总和: 17.5+40.3+88.5+30.9=177.2
    [20.7, 49.9, 105.5, 215.3 - (20.7 + 49.9 + 105.5)],# 2027e 总和: 20.7+49.9+105.5+39.2=215.3
    [24.8, 62.3, 126.9, 263.8 - (24.8 + 62.3 + 126.9)],# 2028e 总和: 24.8+62.3+126.9+50.0=263.8
    [29.3, 54.0, 153.6, 325.4 - (29.3 + 54.0 + 153.6)] # 2029e 总和: 29.3+54.0+153.6+88.5=325.4
])

# 各技术对应的颜色（尽量贴近原图）
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# 技术名称（带单位）
tech_names = ["RPA/IPA", "其他", "AI", "云", "大数据"]

x = np.arange(len(years))  # x轴刻度位置
bar_width = 0.6  # 柱状图宽度

fig, ax = plt.subplots(figsize=(12, 7))

# 绘制堆积柱状图
bottom = np.zeros(len(years))
for i in range(tech_investment.shape[1]):
    bars = ax.bar(x, tech_investment[:, i], width=bar_width, bottom=bottom, 
                  color=colors[i], label=tech_names[i])
    bottom += tech_investment[:, i]
    
    # 在每个堆积层中标注数值
    for j, bar in enumerate(bars):
        height = bar.get_height()
        if height > 0:  # 只标注非零值
            ax.text(
                bar.get_x() + bar.get_width()/2, 
                bar.get_y() + height/2,
                f'{height:.1f}',
                ha='center', va='center',
                color='white', fontsize=9, fontweight='bold'
            )

# 添加标题
ax.set_title('2024-2029年中国保险业前沿技术投入情况', fontsize=14, pad=15)

# 设置x轴刻度标签
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=11)

# 添加y轴标签
ax.set_ylabel('技术投入 (亿元)', fontsize=12)

# 添加图例（放置在图表右侧）
ax.legend(loc='upper left', frameon=True, framealpha=0.9, fontsize=10)

# 计算并标注CAGR（22.5%）
cagr = 22.5
start_value = tech_investment[0].sum()
end_value = tech_investment[-1].sum()

# 绘制CAGR折线
ax.plot([x[0], x[-1]], [start_value, end_value], 'gray', linestyle='--', linewidth=1.2)

# 添加CAGR文本标注
ax.annotate(
    f'CAGR={cagr}%', 
    xy=(x[2], start_value + (end_value - start_value)*0.4), 
    xytext=(x[2]+0.5, start_value + (end_value - start_value)*0.6),
    arrowprops=dict(facecolor='gray', shrink=0.05, width=1.2, headwidth=8),
    fontsize=11,
    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8)
)

# 美化图表
plt.grid(axis='y', linestyle='--', alpha=0.7)  # 添加水平网格线
plt.tight_layout()  # 自动调整布局

plt.show()