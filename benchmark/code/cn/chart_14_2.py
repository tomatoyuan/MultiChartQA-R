import matplotlib.pyplot as plt
import numpy as np

# 省份名称和模拟数据（可根据实际数据替换）
provinces = ['广东', '浙江', '山东', '江苏', '北京', '上海', '福建', '河南', '四川', '河北']
blue_percents = [100, 95, 80, 75, 60, 55, 50, 45, 40, 30]
white_percents = [100 - p for p in blue_percents]

# 数据排序（升序排列）
sorted_data = sorted(zip(blue_percents, white_percents, provinces))
blue_percents, white_percents, provinces = zip(*sorted_data)

# 创建画布
fig, ax = plt.subplots(figsize=(10, 6))

# 设置渐变色（从浅蓝到深蓝）
colors = plt.cm.Blues(np.linspace(0.5, 0.9, len(provinces)))

# 绘制美化后的横向堆叠条形图
bar_white = ax.barh(provinces, white_percents, color='white', edgecolor='lightgray', linewidth=0.8)
bar_blue = ax.barh(provinces, blue_percents, left=white_percents, color=colors, edgecolor='gray', linewidth=0.8)

# 添加数据标签
for i, (blue, white) in enumerate(zip(blue_percents, white_percents)):
    # 在蓝色区域中间添加百分比标签
    ax.text(white + blue/2, i, f'{blue}', ha='center', va='center', 
            color='white' if blue > 40 else 'navy', fontweight='bold')

# 设置标题和底部说明文字
ax.set_title('各省份对空调的关注情况', fontsize=14, pad=15)

# 设置网格线
ax.grid(axis='x', linestyle='--', alpha=0.3)

# 隐藏上、右、下坐标轴
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# 调整刻度和标签样式
ax.tick_params(axis='y', which='major', labelsize=10, pad=10)
ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)

# 添加左侧参考线
ax.axvline(x=0, color='gray', linestyle='-', alpha=0.5)

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()