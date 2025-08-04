import matplotlib.pyplot as plt
import numpy as np

# 时段标签
labels = ["00:00", "05:00", "10:00", "15:00", "20:00"]
# 模拟占比数据（可根据实际需求替换，这里为演示设值），数值仅作示例
sizes = [10, 10, 50, 15, 15]  
# 环形图缺口（让环形更明显），这里统一设 0.3，可调整
explode = [0.3] * len(labels)  

fig, ax = plt.subplots()

# 绘制环形图，wedgeprops 控制环形宽度等样式
ax.pie(
    sizes,
    explode=explode,
    labels=labels,
    autopct="%1.1f%%",  # 显示百分比
    startangle=90,      # 起始角度
    wedgeprops={"width": 0.3, "edgecolor": "white"},  # 环形宽度、边缘颜色
    textprops={"fontsize": 12}  # 文本字体大小
)
ax.set_title("“双十一”一天中何时最想“剁手”？", fontsize=16, fontweight="bold")

# 让饼图保持圆形（避免拉伸变形）
ax.axis("equal")  

plt.show()