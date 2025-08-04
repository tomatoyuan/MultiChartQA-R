import matplotlib.pyplot as plt
import pandas as pd

# 构建数据
data = {
    '渠道': ['线上（网购平台）', '线上（抖音直播）', '线下（超市）', '线下（便利店）', '线下（拼多多）', '线下（小卖部）'],
    '占比': [89, 68, 74, 64, 57, 40]
}
df = pd.DataFrame(data)

# 创建画布
plt.figure(figsize=(12, 6))

# 绘制条形图，区分线上(蓝色)和线下(红色)
colors = ['#4285F4', '#4285F4', '#EA4335', '#EA4335', '#EA4335', '#EA4335']
bars = plt.bar(df['渠道'], df['占比'], color=colors, alpha=0.8)

# 添加数据标签（显示百分比符号）
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height}',
             ha='center', va='bottom', fontsize=10)

# 设置标题和标签
plt.title('渠道占比分布', fontsize=15)
plt.xlabel('渠道类型', fontsize=12)
plt.ylabel('占比', fontsize=12)

# 设置y轴范围
plt.ylim(0, 100)

# 旋转x轴标签以便更好显示
plt.xticks(rotation=45, ha='right')

# 添加网格线
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 添加图例
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='#4285F4', label='线上'),
                   Patch(facecolor='#EA4335', label='线下')]
plt.legend(handles=legend_elements, loc='upper right')

# 优化布局
plt.tight_layout()

# 显示图形
plt.show()