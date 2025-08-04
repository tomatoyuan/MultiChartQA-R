import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np


# 数据
activities = ['马术', '高尔夫球', '豪华露营', '水上运动', '极限运动', '攀岩']
values = [181, 123, 120, 111, 120, 117]
categories = ['奢华户外']*4 + ['专业户外']*2
colors = ['#d7a970']*4 + ['#f2c56d']*2

# 绘图
fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.barh(activities, values, color=colors)

# 添加数值标签
for bar in bars:
    width = bar.get_width()
    ax.text(width + 2, bar.get_y() + bar.get_height()/2, f'{int(width)}',
            va='center', ha='left', fontsize=10, color='white', weight='bold')

# 分类背景色块（右侧标记区域）
ax.axhspan(-0.5, 3.5, facecolor='#3b2d44', alpha=0.6)
ax.text(150, 1.5, '奢华户外', va='center', ha='center', fontsize=12, color='#FFFFFF', weight='bold')

ax.axhspan(3.5, 5.5, facecolor='#3a2b1f', alpha=0.6)
ax.text(150, 4.5, '专业户外', va='center', ha='center', fontsize=12, color='#FFFFFF', weight='bold')

# 图表标题和说明
plt.title('高偏好的户外场景', fontsize=16, weight='bold')


# 美化图表
ax.invert_yaxis()
ax.set_xlim(0, 200)
ax.set_xticks([])
ax.set_yticklabels(activities, fontsize=12)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.text(0, -1.2, '数据来源：CBNData 5月调研\n数据说明：偏好度TGI=该人群选择该场景的比例/整体消费者选择该场景的比例*100，TGI>100表示偏好',
         fontsize=9, ha='left', va='bottom')

plt.tight_layout()
plt.show()