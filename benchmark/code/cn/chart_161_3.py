import matplotlib.pyplot as plt

# 数据
quarters = ['23Q1', '24Q1']
categories = ['均值', '国货品牌', '国际品牌']
data = {
    '均值': [39, 39],
    '国货品牌': [37, 43],
    '国际品牌': [38, 37]
}
colors = ['#A0522D', '#FF8C00', '#FFA07A']  # 使用类似原图的配色

# 绘图
fig, ax = plt.subplots(figsize=(7, 5))
for idx, cat in enumerate(categories):
    ax.plot(quarters, data[cat], marker='^', label=cat, color=colors[idx], linewidth=2)

# 添加文本标签
for idx, cat in enumerate(categories):
    for i, quarter in enumerate(quarters):
        ax.text(quarter, data[cat][i] + 0.5, f"{data[cat][i]}%", color=colors[idx], ha='center', fontsize=12)



# 样式设置
ax.set_ylim(35, 46)
ax.set_title("【面霜】24Q1 vs 23Q1 TOP15品牌赠品深度（主流电商）", fontsize=14, weight='bold')
ax.legend(loc='best')
ax.set_ylabel("赠品促销深度（%）")
ax.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
plt.show()