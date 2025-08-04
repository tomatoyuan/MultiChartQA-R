import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# 时段（x 轴数据）
hours = np.arange(0, 25, 4)
# 搜索热度（y 轴数据，单位：万）
heat_values = [1100, 1100, 3000, 1200, 3000, 1100, 1000]

# 创建画布
plt.figure(figsize=(8, 5), facecolor="#f5f5f5")

# 使用三次样条插值生成平滑曲线
x_smooth = np.linspace(hours.min(), hours.max(), 300)
spl = make_interp_spline(hours, heat_values, k=3)  # k=3 表示三次样条
y_smooth = spl(x_smooth)

# 绘制平滑曲线
plt.plot(x_smooth, y_smooth, color="#0077b6", linewidth=2.5)
# 绘制数据点
plt.scatter(hours, heat_values, color="#023e8a", s=60, zorder=5)

# 设置标题
plt.title("世界杯搜索热度最高时段", fontsize=16, fontweight="bold", color="#03045e")
# 设置 x 轴标签
plt.xlabel("时段", fontsize=12, color="#333333")
# 设置 y 轴标签
plt.ylabel("搜索热度（万）", fontsize=12, color="#333333")

# 设置 x 轴刻度
plt.xticks(hours)
# 设置 y 轴刻度
plt.yticks([1000, 2000, 3000])

# 添加网格线
plt.grid(True, linestyle="--", alpha=0.7)

# 美化图表
plt.tight_layout()  # 自动调整布局
plt.ylim(0, 3500)   # 设置y轴范围

# 显示图表
plt.show()