import matplotlib.pyplot as plt
import numpy as np

# 模拟的时间节点（简化，可根据实际细化）
dates = np.arange(2017, 2022, 0.5)  
# 模拟价格数据（大致趋势，可调整）
prices = [1.8, 1.6, 1.9, 1.8, 1.7, 1.8, 1.7, 1.8, 1.9, 1.8]  

# 创建画布和子图
fig, ax = plt.subplots(figsize=(8, 4))

ax.set_ylim(0, 8)

# 绘制折线图
ax.plot(dates, prices, color="#A4C639", label="不锈钢:304/2B卷板1*1219*C:无锡(万元/吨)", linewidth=2)

# 模拟标注关键节点（示例，可根据实际补充）
key_dates = [2017, 2021]
key_prices = [1.8, 2.2]
for x, y in zip(key_dates, key_prices):
    ax.annotate(f'{y}', xy=(x, y), xytext=(5, 5), textcoords="offset points", ha='center', va='bottom', color="#A4C639")

# 设置x轴刻度（简化为年份显示，可细化）
ax.set_xticks(np.arange(2017, 2022))
ax.set_xticklabels([f"{year}.1" for year in range(2017, 2022)])  # 模拟原图的时间格式

# 设置y轴标签
ax.set_ylabel("价格(万元/吨)")
# 设置标题
ax.set_title("2017-2021年中国不锈钢价格走势", fontsize=14, fontweight="bold")

# 添加图例
ax.legend()

# 美化图表，隐藏顶部和右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()