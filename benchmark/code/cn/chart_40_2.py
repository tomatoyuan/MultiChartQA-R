import matplotlib.pyplot as plt
import numpy as np

# 年份
years = np.array([2022, 2023, 2024, 2025, 2026])
# 市场规模数据（亿元），大体模拟原数据趋势
market_size = np.array([1804, 2045, 2284, 2510, 2737])

# 创建图形，设置合理的尺寸
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制柱状图并保存返回的容器对象
bars = ax.bar(years, market_size, color='r', label='市场规模（亿元）')
ax.set_xlabel('年份')
ax.set_ylabel('市场规模（亿元）', color='r')
ax.tick_params(axis='y', labelcolor='r')

# 设置x轴刻度为年份
ax.set_xticks(years)

# 生成带E的年份标签
year_labels = []
for year in years:
    if year in [2025, 2026]:
        year_labels.append(f"{year}E")  # 预测年份添加E
    else:
        year_labels.append(str(year))   # 实际年份保持不变

# 设置带E的年份标签
ax.set_xticklabels(year_labels)

# 在每个条形上方标注数值（不包含E）
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2.,  # x坐标：条形中心
        height + 15,  # y坐标：条形顶部上方15个单位
        f'{height}',  # 显示数值
        ha='center',  # 水平居中对齐
        va='bottom',  # 垂直底部对齐
        color='r',    # 文字颜色与条形一致
        fontsize=10   # 字体大小
    )

# 添加标题
plt.title('2022 - 2026年中国辣味休闲食品市场规模（亿元）')

# 使用 fig.text() 方法添加注释
fig.text(0.5, 0.85, '辣味休闲食品约是休闲食品行业CAGR的1.6倍',
         ha='center', fontsize=10)

fig.text(0.15, 0.80, '*休闲食品行业CAGR=6.0%', fontsize=8)

# 添加图例
ax.legend(loc='upper left')

# 调整布局
plt.tight_layout()
# 显示图表
plt.show()