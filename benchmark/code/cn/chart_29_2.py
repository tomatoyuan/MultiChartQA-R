import matplotlib.pyplot as plt
import numpy as np

# 赛事数据（比赛对阵、比分、热度值）
matches = ["俄罗斯 5:0 沙特阿拉伯", 
           "葡萄牙 3:3 西班牙", 
           "埃及 0:1 乌拉圭", 
           "巴西 1:1 瑞士", 
           "突尼斯 1:2 英格兰"]
hot_values = [150, 136, 103, 78, 65]  # 热度值（单位：万，简化为数值）

# 用于在 X 轴显示
x = np.arange(len(matches))  

# 创建画布
fig, ax = plt.subplots(figsize=(10, 6))
# 绘制柱状图
rects = ax.bar(x, hot_values, width=0.6, color="#7B68EE")  

# 设置 X 轴刻度与标签
ax.set_xticks(x)
ax.set_xticklabels(matches, rotation=45, ha="right", fontsize=10)  

# 设置 Y 轴标签
ax.set_ylabel("热度值（万）", fontsize=12)  
# 设置标题
ax.set_title("世界杯小组赛首轮赛事热度排行榜Top5", fontsize=14, fontweight="bold")  

# 在柱子上标注数值
for rect in rects:
    height = rect.get_height()
    ax.annotate(f"{height}万", 
                xy=(rect.get_x() + rect.get_width() / 2, height), 
                xytext=(0, 3),  # 向上偏移 3 个像素
                textcoords="offset points", 
                ha="center", va="bottom")

# 优化布局（避免标签显示不全）
plt.tight_layout()  
# 显示图表
plt.show()