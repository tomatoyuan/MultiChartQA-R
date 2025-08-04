import matplotlib.pyplot as plt
import numpy as np

# 1. 准备数据
# 城市名称
cities = ["北京", "厦门", "杭州", "哈尔滨"]  
# 这里模拟搜索热度数值（单位：万次）
search_heat = [8, 6, 4, 2]  

x = np.arange(len(cities))  # 用于在 X 轴定位每个城市的柱子

# 2. 创建图表
fig, ax = plt.subplots()
# 绘制柱状图，设置柱子颜色、宽度等样式
rects = ax.bar(x, search_heat, color=['#FF6347', '#FFA07A', '#FFD700', '#FFFF00'])  

# 3. 自定义图表内容
ax.set_xticks(x)  # 设置 X 轴刻度位置
ax.set_xticklabels(cities)  # 用城市名称作为 X 轴刻度标签
ax.set_ylabel("搜索热度（万次）")  # 设置 Y 轴标题，添加单位
ax.set_title("小长假出行安全搜索地域分布", fontsize=14, fontweight='bold')  # 设置图表标题

# 在柱子上标注数值，并添加单位
for rect in rects:
    height = rect.get_height()
    ax.annotate(f'{height}万',  # 添加"万"单位
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 数值标签距离柱子顶部的垂直距离
                textcoords="offset points",
                ha='center', va='bottom')

# 4. 显示图表
plt.show()