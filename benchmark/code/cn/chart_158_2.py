import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

# 行列标签
age_groups = ['20岁以下', '21-25岁', '26-30岁', '31-34岁', '35-40岁', '41-45岁', '45岁以上']
generations = ['00后', '95后', '90后', '85后', '85前']

# 百分比矩阵
percent_data = np.array([
    [52, 0, 0, 0, 1],
    [42, 29, 5, 5, 2],
    [2, 70, 60, 24, 5],
    [2, 1, 33, 51, 24],
    [0, 0, 2, 17, 38],
    [1, 0, 0, 0, 22],
    [1, 0, 0, 0, 9],
])

# 计算每列最大值位置（用于黄色高亮）
highlight_mask = (percent_data == np.max(percent_data, axis=0))

# 颜色映射
cmap = plt.cm.Purples
norm = mcolors.Normalize(vmin=0, vmax=np.max(percent_data))

# 图像准备
fig, ax = plt.subplots(figsize=(10, 7))
ax.set_xlim(0, len(generations))
ax.set_ylim(0, len(age_groups))

# 绘制单元格
for i in range(len(age_groups)):
    for j in range(len(generations)):
        value = percent_data[i, j]
        if value > 0:
            if highlight_mask[i, j]:
                color = '#FFD700'  # 黄色高亮最大值
                text_color = 'black'
            else:
                color = cmap(norm(value))  # 紫色热力
                text_color = 'white' if value > 30 else 'black'
            ax.add_patch(plt.Rectangle((j, len(age_groups)-1-i), 1, 1, color=color))
            ax.text(j + 0.5, len(age_groups)-1-i + 0.5, f'{value}%',
                    ha='center', va='center', fontsize=11, color=text_color)

# 设置轴标签
ax.set_xticks(np.arange(len(generations)) + 0.5)
ax.set_xticklabels(generations, fontsize=12)
ax.set_yticks(np.arange(len(age_groups)) + 0.5)
ax.set_yticklabels(age_groups[::-1], fontsize=12)
ax.invert_yaxis()

# 标题与数据来源
plt.title('不同代际人群在各年龄段首次感知肌肤衰老的分布', fontsize=14, weight='bold', loc='left')
plt.text(0, -1, '数据来源：2024年7月CBNData问卷调研\nQ5. 请问您在什么年龄阶段开始有肌肤衰老的表现？',
         fontsize=9, color='gray')

# 样式清理
for spine in ax.spines.values():
    spine.set_visible(False)
ax.tick_params(left=False, bottom=False)
plt.grid(False)

# 添加颜色条（只显示紫色映射）
cbar = plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap),
                    ax=ax, orientation='vertical', shrink=0.6, pad=0.02)
cbar.set_label('百分比强度（非最大值）', fontsize=10)

plt.tight_layout()
plt.show()