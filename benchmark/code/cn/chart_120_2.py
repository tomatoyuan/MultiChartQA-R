import matplotlib.pyplot as plt

# 左侧：中国券商自营类APP用户拥有APP数量调查数据
left_labels = ["3-4个", "1-2个", "5个及以上"]
left_sizes = [54.55, 39.57, 5.88]
left_colors = ["gold", "coral", "green"]

# 右侧：中国券商自营类APP用户每天打开次数调查数据
right_labels = ["平均每日打开几次", "平均每周打开几次", "平均每日打开很多次", 
                "平均每月打开几次", "平均一年打开不了几次"]
right_sizes = [44.39, 32.09, 14.97, 7.49, 1.06]
right_colors = ["gold", "green", "coral", "brown", "olive"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 绘制左侧拥有APP数量的饼图
wedges, texts, autotexts = ax1.pie(left_sizes, labels=left_labels, colors=left_colors, autopct="%1.2f%%",
                                   startangle=90)
# 调整左侧标注文字颜色
for autotext in autotexts:
    autotext.set_color("white")

ax1.set_title("中国券商自营类APP用户拥有APP数量调查")

# 绘制右侧每日打开次数的饼图
wedges, texts, autotexts = ax2.pie(right_sizes, labels=right_labels, colors=right_colors, autopct="%1.2f%%",
                                   startangle=90)
# 调整右侧标注文字颜色
for autotext in autotexts:
    autotext.set_color("white")

ax2.set_title("中国券商自营类APP用户每天打开次数调查")

plt.tight_layout()
plt.show()