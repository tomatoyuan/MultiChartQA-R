import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.font_manager as fm

# 数据准备
categories = [
    "雪地旅行/滑雪", "豪华露营", "水上运动", "高尔夫球", "马术", "热气球",
    "攀岩", "水下运动", "极限运动", "射击",
    "登山/徒步/露营", "骑行", "钓鱼", "City Walk"
]
values = [38, 38, 35, 17, 6, 1, 26, 22, 9, 8, 57, 54, 35, 29]

# 分类颜色
colors = [
    "#EECFA1"] * 6 + ["#F4A259"] * 4 + ["#B1D8B7"] * 4  # 奢华户外/专业户外/大众户外色系

fig, ax = plt.subplots(figsize=(10, 8))
bars = ax.barh(categories, values, color=colors)

# 添加数值标签
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1.5, bar.get_y() + bar.get_height()/2,
            f'{int(width)}%', va='center', fontsize=10)

# 图表标题
ax.set_title("消费者曾经尝试并喜爱的户外运动分布", fontsize=14, fontweight='bold', loc='center', pad=20)

# 去除多余元素
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.tick_params(axis='y', length=0)
ax.set_xlim(0, 65)

# 分类区域标注（右侧）
ax.text(65.5, 12.5, "奢华户外", fontsize=12, weight='bold', color='#D4A55A', va='center')
ax.text(65.5, 8.5, "专业户外", fontsize=12, weight='bold', color='#D98C3A', va='center')
ax.text(65.5, 2.5, "大众户外", fontsize=12, weight='bold', color='#568259', va='center')

# 添加说明文字
plt.figtext(0.01, 0.01,
            "数据来源：CBNData 2024年5月中国奢华户外服饰流行趋势的调研\n"
            "数据说明：请问您尝试并喜爱以下哪些户外运动/活动项目？N=1000",
            ha='left', fontsize=9, linespacing=1.5)

plt.tight_layout()
plt.show()