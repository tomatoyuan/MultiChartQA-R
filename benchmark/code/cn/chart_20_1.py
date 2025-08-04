import matplotlib.pyplot as plt
import numpy as np

# 数据
age_groups = ["19岁以下", "25-34岁", "19-24岁", "35-49岁", "50岁以上"]
percentages = [11, 49, 20, 15, 5]  
colors = ["#1f77b4", "#8dd3c7", "#bebada", "#fb8072", "#80b1d3"]  # 自定义颜色，可调整

# 创建环形图
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(
    percentages,
    labels=age_groups,
    autopct="%1.1f%%",  # 显示百分比格式
    startangle=90,
    colors=colors,
    pctdistance=0.85,  # 百分比标签距离圆心的距离
    wedgeprops={"width": 0.4},  # 环形宽度
)

# 添加中心圆（让环形更明显）
centre_circle = plt.Circle((0, 0), 0.6, color="black", fc="white", linewidth=0)
ax.add_artist(centre_circle)

# 设置标题
ax.set_title("不同年龄段分布", fontsize=16, y=1.05)

# 显示图表
plt.show()