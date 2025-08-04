import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
from matplotlib import font_manager as fm

# 中文字体支持（适配用户的Jupyter环境设定）
chinese_fonts = [
    "SimHei", "Heiti TC", "WenQuanYi Micro Hei", "Microsoft YaHei", "Arial Unicode MS"
]
available_fonts = {f.name for f in fm.fontManager.ttflist}
for font in chinese_fonts:
    if font in available_fonts:
        plt.rcParams["font.family"] = font
        break
plt.rcParams['axes.unicode_minus'] = False

# 数据
categories = ['紧致抗老', '舒缓抗敏', '滋养修护', '美白淡斑', '保湿补水']
q1_2023 = [648, 190, 297, 365, 191]
q1_2024 = [884, 215, 314, 395, 233]
growth = [q1_2024[i] - q1_2023[i] for i in range(len(q1_2023))]

x = np.arange(len(categories))
width = 0.35

# 色彩设置
color_2023 = '#fcd7cc'
color_2024 = '#f29676'

fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - width/2, q1_2023, width, label='23Q1品牌数', color=color_2023)
bars2 = ax.bar(x + width/2, q1_2024, width, label='24Q1品牌数', color=color_2024)

# 数值标签
for i in range(len(x)):
    ax.text(x[i] - width/2, q1_2023[i] + 10, str(q1_2023[i]), ha='center', va='bottom', fontsize=10)
    ax.text(x[i] + width/2, q1_2024[i] + 10, str(q1_2024[i]), ha='center', va='bottom', fontsize=10)
    ax.annotate(f'+{growth[i]}',
                xy=(x[i] + width/2, q1_2024[i] + 40),
                xytext=(x[i] + width/2, q1_2024[i] + 60),
                ha='center',
                arrowprops=dict(facecolor='black', arrowstyle='->'),
                fontsize=10,
                bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='black', lw=1))

# 分组边框区域
ax.add_patch(patches.Rectangle((-0.5, 0), 1.0, 950, fill=False, edgecolor='gray', linestyle='--', linewidth=1))
ax.text(-0.5, 950, '竞争加剧', color='orangered', fontsize=12)

ax.add_patch(patches.Rectangle((1.5, 0), 1.0, 500, fill=False, edgecolor='gray', linestyle='--', linewidth=1))
ax.text(1.5, 500, '竞争较稳', color='peru', fontsize=12)

# 其余设置
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.set_ylabel('品牌数')
ax.set_title('【面霜子类】24Q1面霜分功效品牌竞争格局（主流电商）')
ax.legend()

plt.tight_layout()
plt.show()