import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# 日期数据，用序号代表日期（5月7日为第0天，后续依次类推）
x = np.arange(0, 20, 1)
# 模拟成交指数数据，大致模拟原曲线趋势
y = [10, 120, 140, 160, 170, 180, 190, 200, 210, 220, 250, 280, 310, 320, 330, 340, 350, 360, 370, 380]

# 创建更密集的x轴数据点，用于平滑曲线
x_smooth = np.linspace(x.min(), x.max(), 300)

# 使用三次样条插值创建平滑曲线
spl = make_interp_spline(x, y, k=3)  # k=3表示三次样条
y_smooth = spl(x_smooth)

# 创建画布
fig, ax = plt.subplots(figsize=(8, 6))

# 添加主标题
plt.title('618大促成交指数趋势图', fontsize=16, pad=20)

# 绘制平滑曲线，设置颜色接近原图表的渐变
line, = ax.plot(x_smooth, y_smooth, color='pink', linewidth=3)
# 给曲线下方填充渐变颜色
ax.fill_between(x_smooth, y_smooth, color='pink', alpha=0.3)

# 设置 x 轴刻度和标签，对应实际日期
x_labels = ['5月7日', '', '', '', '', '5月13日', '', '', '', '', '', '5月16日', '', '', '', '', '', '', '', '5月26日']
ax.set_xticks(np.arange(0, 20, 1))
ax.set_xticklabels(x_labels, rotation=0, ha='center')

# 添加标注文本
ax.text(5, 50, '第一波预算占比:60%\n抢赢第一波流量先机', fontsize=12, ha='center')
ax.text(5, 30, '预售开启日', fontsize=10, ha='center', color='red')
ax.text(15, 120, '618抢先购售卖', fontsize=12, ha='center', color='red')

# 标注关键数据点
highlight_indices = [0, 5, 10, 15, 19]  # 选择要标注的数据点索引
for i in highlight_indices:
    # 在原始数据点位置标注，而非平滑后的位置
    ax.annotate(f'{y[i]}',  # 标注的文本内容
                xy=(x[i], y[i]),  # 要标注的数据点
                xytext=(x[i], y[i]+15),  # 文本位置（数据点上方）
                arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),  # 箭头样式
                ha='center',  # 水平对齐方式
                fontsize=10)  # 字体大小

# 设置 y 轴标签
ax.set_ylabel('成交指数')

# 隐藏顶部和右侧边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 显示图表
plt.tight_layout()
plt.show()