import matplotlib.pyplot as plt
import numpy as np

# --------------------- 年龄分布数据 ---------------------
age_labels = ["18岁及以下", "19-25岁", "26-30岁", "31-40岁", "41-50岁", "51岁及以上"]
age_sizes = [0.0, 13.0, 36.8, 39.9, 8.2, 2.1]
age_colors = ["#FADBD8", "#F9E79F", "#F5B041", "#F1948A", "#B03A2E", "#8B4513"]

# --------------------- 常住地区分布数据 ---------------------
region_labels = ["一线城市", "新一线城市", "二线城市", "三线城市", "四线及其他城市"]
region_sizes = [27.3, 27.6, 26.9, 12.6, 5.6]
region_colors = ["#FADBD8", "#F9E79F", "#F5B041", "#F1948A", "#8B4513"]

# --------------------- 性别分布数据 ---------------------
gender_labels = ["男", "女"]
gender_sizes = [36.8, 63.2]
gender_colors = ["#F9E79F", "#F1948A"]

# 创建画布，一行三列布局
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

# --------------------- 绘制年龄分布饼图（左图） ---------------------
wedges1, texts1, autotexts1 = ax1.pie(age_sizes, colors=age_colors, autopct='%1.1f%%', startangle=90)
ax1.set_title('2023年中国文创产品消费者年龄分布')
ax1.legend(wedges1, age_labels, title="年龄区间", loc="center left", bbox_to_anchor=(1, 0.5))
# 调整标注文字颜色
for autotext in autotexts1:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

# --------------------- 绘制常住地区分布饼图（中图） ---------------------
wedges2, texts2, autotexts2 = ax2.pie(region_sizes, colors=region_colors, autopct='%1.1f%%', startangle=90)
ax2.set_title('2023年中国文创产品消费者常住地区分布')
ax2.legend(wedges2, region_labels, title="地区类型", loc="center left", bbox_to_anchor=(1, 0.5))
# 调整标注文字颜色
for autotext in autotexts2:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

# --------------------- 绘制性别分布饼图（右图） ---------------------
wedges3, texts3, autotexts3 = ax3.pie(gender_sizes, colors=gender_colors, autopct='%1.1f%%', startangle=90)
ax3.set_title('2023年中国文创产品消费者性别分布')
ax3.legend(wedges3, gender_labels, title="性别", loc="center left", bbox_to_anchor=(1, 0.5))
# 调整标注文字颜色
for autotext in autotexts3:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

plt.tight_layout()
plt.show()