import matplotlib.pyplot as plt
import numpy as np

# 数据（示例，需按实际替换）
labels = ['MAT2022', 'MAT2023', 'MAT2024']
taobao = [60, 55, 45]  # 淘天占比（示例）
jingdong = [10, 10, 10]  # 京东占比（示例）
douyin = [30, 35, 45]  # 抖音占比（示例）

x = np.arange(len(labels))  # x轴位置
width = 0.35  # 柱状图宽度

fig, ax = plt.subplots()
# 绘制各渠道柱状图，注意bottom参数实现堆叠效果
rects_taobao = ax.bar(x, taobao, width, label='淘天', color='#E67E22')
rects_jingdong = ax.bar(x, jingdong, width, bottom=taobao, label='京东', color='#E74C3C')
rects_douyin = ax.bar(x, douyin, width, bottom=np.add(taobao, jingdong), label='抖音', color='#6DD9E0')

# 标注增速
ax.annotate('+28%', 
            xy=(2, 100),  # 将xy位置调整到第三个柱子的顶部
            xytext=(0, 10),  # 添加偏移量，使文本在柱子上方
            textcoords="offset points",
            ha='center', 
            va='bottom',
            fontsize=12,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", linestyle="--", alpha=0.8))

# 在每个柱子上标注数值
def add_labels(rects, bottom_values=None):
    for i, rect in enumerate(rects):
        height = rect.get_height()
        if bottom_values is not None:
            bottom = bottom_values[i]
        else:
            bottom = 0
        # 计算文本位置（柱子中间）
        y_position = bottom + height / 2
        # 添加数值标注
        ax.text(
            rect.get_x() + rect.get_width() / 2,  # x坐标：柱子中心
            y_position,                          # y坐标：柱子中间
            f'{height}%',                        # 显示的数值
            ha='center', va='center',            # 水平和垂直居中
            color='white', fontweight='bold',    # 白色文本，加粗
            fontsize=9                           # 字体大小
        )

# 为每个渠道添加标注
add_labels(rects_taobao)
add_labels(rects_jingdong, taobao)
add_labels(rects_douyin, np.add(taobao, jingdong))

# 设置x轴刻度与标签
ax.set_xticks(x)
ax.set_xticklabels(labels)
# 设置y轴范围
ax.set_ylim(0, 110)  # 增加y轴上限，避免文本被遮挡
# 添加y轴百分比刻度
ax.set_yticks(np.arange(0, 101, 20))
ax.set_yticklabels([f'{i}%' for i in range(0, 101, 20)])
# 添加图例与标题
ax.legend()
ax.set_title('护肤线上渠道核心渠道生意占比及增速')

plt.tight_layout()  # 优化布局
plt.show()