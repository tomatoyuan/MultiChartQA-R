import matplotlib.pyplot as plt

# 数据
countries = ["美国", "日本", "欧洲"]
percentages = [48, 45, 7]  
colors = ["pink", "lightgreen", "lightblue"]  

# 创建饼图
plt.pie(
    percentages, 
    labels=countries, 
    colors=colors, 
    autopct="%1.1f%%",  # 显示百分比
    startangle=90,      # 起始角度
    textprops={"fontsize": 12}
)

# 添加标题
plt.title("海外就医去哪里？", fontsize=16, fontweight="bold")

# 调整布局（避免标签挤压）
plt.tight_layout()

# 显示图表
plt.show()