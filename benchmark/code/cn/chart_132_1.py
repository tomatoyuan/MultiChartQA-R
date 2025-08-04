import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ["工学", "理学", "经济学", "教育学", "管理学", "医学", "文学", 
              "历史学", "法学", "艺术学", "农学", "哲学", "其他"]
proportions = [26.75, 25.81, 23.63, 23.48, 23.32, 19.75, 16.69, 
               15.86, 15.71, 12.59, 11.50, 11.35, 0.31]
# 偏文科、偏理科占比
liberal_arts = 43.5
science = 56.5

fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(16, 8), gridspec_kw={'width_ratios': [1, 3]})

# 左侧：偏文科、偏理科占比（文本 + 简单可视化）
ax_left.text(0.5, 0.6, f'偏文科 {liberal_arts}%', ha='center', va='center', fontsize=16, color='orange')
ax_left.text(0.5, 0.4, f'偏理科 {science}%', ha='center', va='center', fontsize=16, color='blue')
ax_left.axis('off')

# 右侧：各科目/专业偏好横向柱状图
y = np.arange(len(categories))
ax_right.barh(y, proportions, color='orange')
ax_right.set_yticks(y)
ax_right.set_yticklabels(categories)
ax_right.set_xlabel('占比（%）')

# 添加各科目/专业占比数值标注
for i, prop in enumerate(proportions):
    ax_right.text(prop + 0.5, i, f'{prop}%', va='center')

ax_right.set_title('中国高考生偏好科目及专业')

plt.tight_layout()
plt.show()