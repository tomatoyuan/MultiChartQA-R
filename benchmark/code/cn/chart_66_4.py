import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# 渠道名称
channels = ["天猫", "京东", "宠物店", "淘宝", "宠物医院"]
# 对应数据（占比）
data = [27, 27, 19, 17, 10]
# 图标路径，这里假设你有对应的本地图标文件，需替换为实际路径
icon_paths = ["tmall_icon.png", "jd_icon.png", "pet_shop_icon.png", "taobao_icon.png", "pet_hospital_icon.png"]
# 颜色设置，贴近原图绿色和灰色
bar_colors = ["#A4C639", "#A4C639", "#A4C639", "#A4C639", "#A4C639"]
bg_colors = ["#D3D3D3"] * len(channels)

# 创建画布
fig, ax = plt.subplots(figsize=(8, 5))

# 绘制条形图，设置整体宽度等
x = np.arange(len(channels))
bar_width = 0.6
for i in range(len(channels)):
    # 绘制灰色背景条
    bg_rect = ax.bar(x[i], 100, bar_width, color=bg_colors[i], edgecolor="white")
    # 绘制彩色前景条
    bar = ax.bar(x[i], data[i], bar_width, color=bar_colors[i], edgecolor="white")
    # 添加数据标注
    ax.annotate(f'{data[i]}%',
                xy=(x[i], data[i]),
                xytext=(5, -15),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom',
                color="black")

    # 处理图标，这里简单演示，若要精准还原，需更细致调整
    try:
        icon = Image.open(icon_paths[i])
        icon = icon.resize((20, 20))  # 调整图标大小
        fig.canvas.draw()
        ax_image = fig.add_axes([ax.get_xlim()[0] + i * (ax.get_xlim()[1] - ax.get_xlim()[0])/len(channels) - 0.03, 
                                 ax.get_ylim()[0] + 0.01, 0.05, 0.05])  # 图标位置
        ax_image.imshow(icon)
        ax_image.axis("off")
    except:
        pass

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(channels)
# 隐藏y轴
ax.set_yticks([])
ax.set_ylabel("")
# 设置标题
ax.set_title("膏剂购买渠道（TOP5）", fontsize=14, fontweight="bold")

# 美化图表，隐藏顶部、右侧和底部边框
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)
    
plt.show()