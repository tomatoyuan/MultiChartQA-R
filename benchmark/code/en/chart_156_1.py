import matplotlib.pyplot as plt
import numpy as np

# Years and share data
years = ['MAT2022', 'MAT2023', 'MAT2024']
top5 = np.array([27, 34, 37])
top6_10 = np.array([15, 13, 11])
top11_20 = np.array([13, 12, 11])
others = 100 - (top5 + top6_10 + top11_20)

x = np.arange(len(years))
bar_width = 0.6

fig, ax = plt.subplots(figsize=(8, 6))

# Draw stacked bars
p1 = ax.bar(x, top5, bar_width, label='TOP5', color='#FF7F7F')
p2 = ax.bar(x, top6_10, bar_width, bottom=top5, label='TOP6-10', color='#FFBFA2')
p3 = ax.bar(x, top11_20, bar_width, bottom=top5+top6_10, label='TOP11-20', color='#FFD6A5')
p4 = ax.bar(x, others, bar_width, bottom=top5+top6_10+top11_20, label='Others', color='#D3D3D3')

# Annotate values
for i in range(len(years)):
    ax.text(x[i], top5[i]/2, f"{top5[i]}%", ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')
    ax.text(x[i], top5[i]+top6_10[i]/2, f"{top6_10[i]}%", ha='center', va='center',
            fontsize=10, color='black')
    ax.text(x[i], top5[i]+top6_10[i]+top11_20[i]/2, f"{top11_20[i]}%", ha='center', va='center',
            fontsize=10, color='black')
    ax.text(x[i], 100 - others[i]/2, f"{others[i]}%", ha='center', va='center',
            fontsize=10, color='black')

# Axis and title
ax.set_title('Change in Brand Share of "Skinny Legs Artifact" on Taobao E - commerce Platform from MAT2022 to MAT2024',
             fontsize=15, weight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=12)
ax.set_ylabel('Brand Share (%)', fontsize=12)
ax.set_ylim(0, 100)
ax.set_facecolor('#f9f9f9')

# ✅ 移动图例，避免柱子遮挡
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.12), ncol=4, frameon=False)

# ✅ 留出更多顶部和底部空间，避免遮挡
plt.subplots_adjust(top=0.85, bottom=0.25)

# ✅ 添加数据源说明文字（不易被遮挡）
source_text = (
    "Data Source: Magic Mirror Market Intelligence Data, MAT2024: July 2023 - June 2024\n"
    "Data Description: The data collection logic is the consumption data of products under the category of 'Tights/Leggings' "
    "on Tmall/Taobao/Douyin platforms, where the product titles contain keywords such as 'Skinny Legs Artifact' or 'Nude - feeling Skinny Legs Artifact';\n"
    "Big Data: Full Insight"
)
plt.figtext(0.5, -0.1, source_text, wrap=True, ha='center', fontsize=9, color='gray')

plt.tight_layout()
plt.show()