import matplotlib.pyplot as plt
import numpy as np

# 城市名称
cities = ["广州", "北京", "上海", "深圳", "杭州", "福州", "宁波", "温州", "厦门", "武汉"]
# 模拟的柱状图数据，大体体现高度差异，可根据实际微调
data = [30, 25, 22, 20, 18, 16, 19, 17, 15, 14]

x = np.arange(len(cities))  # x轴坐标
width = 0.5  # 柱子宽度

fig, ax = plt.subplots(figsize=(8, 5))  # 创建画布和轴对象，设置图尺寸
# 绘制柱状图，颜色设置为接近原图的两种色调，可微调rgb值更贴近
bars1 = ax.bar(x[::2], data[::2], width, color=(209/255, 78/255, 68/255))  # 红色系柱子
bars2 = ax.bar(x[1::2], data[1::2], width, color=(255/255, 235/255, 201/255))  # 浅米色柱子

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(cities)
# 设置图表标题
ax.set_title("春运回家十大热门出发城市", fontsize=14, fontweight='bold')

# 添加x轴标签
ax.set_xlabel("城市", fontsize=12)
# 添加y轴标签和单位
ax.set_ylabel("出行热度指数", fontsize=12)

# 隐藏上、右坐标轴
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 在每个柱子上方添加数值标签
for i, v in enumerate(data):
    ax.text(i, v + 0.5, str(v), ha='center', fontsize=10)

# 使用纯绘图方式创建装饰元素，替代图片
from matplotlib.patches import Polygon, Circle

# 创建热气球形状
def create_balloon(ax, x, y, scale=1.0):
    # 气球主体
    balloon = Polygon([
        (x, y+15*scale), (x-5*scale, y+5*scale), (x-3*scale, y), 
        (x+3*scale, y), (x+5*scale, y+5*scale), (x, y+15*scale)
    ], fill=True, color=(209/255, 78/255, 68/255))
    ax.add_patch(balloon)
    
    # 吊篮
    basket = Polygon([
        (x-2*scale, y), (x-3*scale, y-3*scale), 
        (x+3*scale, y-3*scale), (x+2*scale, y)
    ], fill=True, color=(139/255, 69/255, 19/255))
    ax.add_patch(basket)
    
    # 绳子
    ax.plot([x-2*scale, x-2.5*scale], [y, y-1.5*scale], 'k-', linewidth=0.5)
    ax.plot([x+2*scale, x+2.5*scale], [y, y-1.5*scale], 'k-', linewidth=0.5)

# 在右上角添加热气球装饰
create_balloon(ax, 8.5, 32, scale=0.3)

plt.tight_layout()  # 调整布局，确保标签不被遮挡
plt.show()