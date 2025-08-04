import matplotlib.pyplot as plt

# 数据准备
labels = ["1-3次", "4-6次", "7-9次", "10次及以上"]
sizes = [41.0, 45.0, 10.0, 4.0]  # 占比（%）
colors = ["lightpink", "coral", "sandybrown", "brown"]  # 配色，贴近原图风格

fig, ax = plt.subplots(figsize=(8, 6))

# 绘制饼图
wedges, texts, autotexts = ax.pie(
    sizes, 
    colors=colors, 
    autopct='%1.1f%%', 
    startangle=140,  # 调整起始角度，让饼图分布更合理
    pctdistance=0.8  # 调整标注位置，避免与图例重叠
)

ax.set_title('2023年中国本地生活服务用户服务消费周频率分布', fontsize=14)

# 设置图例（与原图一致的位置和样式）
ax.legend(
    wedges, 
    labels, 
    title="消费周频率", 
    loc="center left", 
    bbox_to_anchor=(1, 0.5)
)

# 优化标注文字颜色（深色切片用白色字，浅色用黑色字）
for autotext in autotexts:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

plt.tight_layout()
plt.show()