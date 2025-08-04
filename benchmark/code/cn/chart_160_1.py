# 重新设置中文字体与绘图配置
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


# 数据
years = ['2020年', '2021年', '2022年', '2023年']
creators = [900, 1100, 1310, 1420]
growth_rates = ['+22%', '+18%', '+8%']

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(years, creators, marker='o', color='#6A78FF', linewidth=3)

# 标注点的值（加粗、蓝色）
for i, value in enumerate(creators):
    plt.text(i, value + 30, f"{value}", ha='center', fontsize=14, color='#1F3BB3', fontweight='bold')

# 标注增长率（更大字体、斜体、紫色）
for i in range(1, len(creators)):
    mid_x = (i - 1 + i) / 2
    mid_y = (creators[i - 1] + creators[i]) / 2 + 20
    plt.text(mid_x, mid_y, growth_rates[i - 1], ha='center', fontsize=16, color='#B03ACC', fontstyle='italic')

# 图表设置
plt.title("主要社交平台万粉以上创作者总数（万）", fontsize=16, fontweight='bold')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()