import matplotlib.pyplot as plt

# 数据
labels = [
    '细纹/皱纹增多', '皮肤弹性下降', '油脂分泌过剩', '粗糙暗黄', '毛孔粗大', '光泽度下降',
    '气色差', '皮肤水分减少', '肤色不均', '长斑', '粉刺痘痘', '易过敏', '长期水肿'
]
percentages = [63, 60, 59, 58, 54, 53, 53, 52, 40, 35, 33, 25, 22]

# 设置颜色
colors = ['#FFCC00' if i < 4 else '#673AB7' for i in range(len(labels))]

x = range(len(labels))
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(x, percentages, color=colors)

# 添加柱上的百分比标签
for i, bar in enumerate(bars):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 1,
            f'{percentages[i]}%', ha='center', va='bottom', fontsize=11)

# 设置x轴标签
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=10, rotation=30, ha='right')

# 标题
ax.set_title('超60%的人感受到睡眠问题导致的细纹/皱纹增多、皮肤弹性下降',
             fontsize=14, weight='bold')

ax.set_ylim(0, 75)
ax.set_ylabel('占比（%）', fontsize=12)

# ✅ 修正标签1：横跨前两列
mid_x = (0 + 1) / 2
ax.text(mid_x, 68, '除00后外\n其他代际的\n首要问题',
        ha='center', va='bottom', fontsize=10,
        bbox=dict(facecolor='#E0E0E0', edgecolor='gray', boxstyle='round,pad=0.3'))

# ✅ 标签2：00/95/90后更显著（保持不变）
ax.text(2.5, 65, '00/95/90后\n更显著',
        ha='center', va='bottom', fontsize=10,
        bbox=dict(facecolor='#E0E0E0', edgecolor='gray', boxstyle='round,pad=0.3'))

# 数据来源脚注
plt.figtext(0.5, -0.08,
            '数据来源：2024年7月CBNData问卷调研\nQ15. 请问您认为睡眠问题（熬夜或睡眠质量差）对您的皮肤产生了什么影响？',
            wrap=True, ha='center', fontsize=9, color='gray')

# 美化
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(axis='y', left=True)

plt.tight_layout()
plt.show()