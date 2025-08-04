import matplotlib.pyplot as plt
import numpy as np

# 年份
years = [2022, 2023, 2024]
# 线上渠道份额
online_shares = [41, 41, 43]
# 线下渠道份额（通过 100 - 线上渠道份额计算得出，因为整体为100% ）
offline_shares = [100 - x for x in online_shares]

x = np.arange(len(years))  # 柱状图 x 轴位置
width = 0.35  # 每个柱子的宽度

fig, ax = plt.subplots()
# 绘制线下渠道柱子
rects_offline = ax.bar(x - width/2, offline_shares, width, label='线下渠道', color='#D9C8B1')  
# 绘制线上渠道柱子
rects_online = ax.bar(x + width/2, online_shares, width, label='线上渠道', color='#F7C8AA')  

# 设置 x 轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(years)
# 设置 y 轴标签
ax.set_ylabel('份额 (%)')
# 设置标题
ax.set_title('2022 - 2024年护肤品线上与线下渠道份额对比')
# 添加图例
ax.legend()

# 在柱子上标注数值
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}%'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 数值标注位置偏移
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects_offline)
autolabel(rects_online)

plt.show()