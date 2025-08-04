import matplotlib.pyplot as plt

# 应用类别
labels = [
    "视频服务", "通讯聊天", "综合资讯", 
    "游戏服务", "社交网络", "电子商务", 
    "实用工具", "其他"
]
# 各应用使用时间占比（%），数据大体一致即可
sizes = [43.9, 19.7, 7.3, 5.8, 4.1, 3.7, 3.6, 11.9]
# 饼图各部分颜色，尽量贴近原图
colors = [
    "#A4C639", "#A4D68C", "#BCE1A3", 
    "#87D3F2", "#74BCEF", "#F2D387", 
    "#F2B987", "#ECECEC"
]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(8, 8))

# 绘制饼图
wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, autopct='%1.1f%%', 
    startangle=140, colors=colors, 
    textprops={'color': 'black'}
)

# 美化标注文本（调整大小和颜色等）
for text in texts + autotexts:
    text.set_fontsize(12)

# 模拟绿色外边框
for spine in ax.spines.values():
    spine.set_color('#A4C639')
    spine.set_linewidth(2)

# 设置标题
ax.set_title("mUserTracker-2022年Q1用户应用使用时间分布", fontsize=14, fontweight="bold", y=1.05)

plt.tight_layout()  # 自动调整布局
plt.show()