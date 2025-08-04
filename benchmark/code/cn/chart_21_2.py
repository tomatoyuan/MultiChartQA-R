import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline  

# 1. 模拟原始数据（日期、人群规模）
dates = np.array(['1-10', '1-13', '1-16', '1-19', '1-22', '1-25', '1-28', 
                  '1-31', '2-3', '2-6', '2-9', '2-12', '2-15', '2-18', '2-21'])  

# 学生回家数据（峰值在1-19和1-25，1-22为峰值一半，1-10和2-21为0）
student_go = np.array([0, 30, 60, 50, 30, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0])  

# 务工人员回家数据（峰值在1-25附近）
worker_go = np.array([0, 0, 0, 30, 80, 85, 0, 0, 0, 0, 0, 0, 0, 0, 0])  

# 白领回家数据（峰值在1-22附近）
white_collar_go = np.array([0, 0, 0, 0, 70, 75, 0, 0, 0, 0, 0, 0, 0, 0, 0])  

# 返程数据（均匀分布在2月）
student_back = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 60, 70, 75, 70])  
worker_back = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 60, 65, 64, 45, 0, 0])  
white_collar_back = np.array([0, 0, 0, 0, 0, 0, 0, 0, 75, 70, 0, 0, 0, 0, 0])  

# 2. 创建均匀分布的时间轴
x_uniform = np.arange(len(dates))  # 均匀分布的数值轴

# 3. 插值平滑处理
def smooth_curve(y):  
    x_new = np.linspace(x_uniform.min(), x_uniform.max(), 300)  
    spline = make_interp_spline(x_uniform, y, k=3)  
    return x_new, spline(x_new)

# 平滑处理
x_smooth, student_go_smooth = smooth_curve(student_go)
_, worker_go_smooth = smooth_curve(worker_go)
_, white_collar_go_smooth = smooth_curve(white_collar_go)

_, student_back_smooth = smooth_curve(student_back)
_, worker_back_smooth = smooth_curve(worker_back)
_, white_collar_back_smooth = smooth_curve(white_collar_back)

# 4. 绘制曲线图
fig, ax = plt.subplots(figsize=(14, 7), facecolor='#f8f9fa')
ax.set_facecolor('#f8f9fa')

# 回家阶段曲线及填充
student_go_line, = ax.plot(x_smooth, student_go_smooth, color='#A8D8EA', linewidth=2.5, label='学生（回家）')
ax.fill_between(x_smooth, student_go_smooth, color='#A8D8EA', alpha=0.3)  # 填充学生回家曲线

worker_go_line, = ax.plot(x_smooth, worker_go_smooth, color='#AA96DA', linewidth=2.5, label='务工（回家）')
ax.fill_between(x_smooth, worker_go_smooth, color='#AA96DA', alpha=0.3)  # 填充务工回家曲线

white_collar_go_line, = ax.plot(x_smooth, white_collar_go_smooth, color='#FCBAD3', linewidth=2.5, label='白领（回家）')
ax.fill_between(x_smooth, white_collar_go_smooth, color='#FCBAD3', alpha=0.3)  # 填充白领回家曲线

# 返程阶段曲线及填充
student_back_line, = ax.plot(x_smooth, student_back_smooth, color='#CDEAC0', linewidth=2.5, label='学生（返程）')
ax.fill_between(x_smooth, student_back_smooth, color='#CDEAC0', alpha=0.3)  # 填充学生返程曲线

worker_back_line, = ax.plot(x_smooth, worker_back_smooth, color='#FFDAC1', linewidth=2.5, label='务工（返程）')
ax.fill_between(x_smooth, worker_back_smooth, color='#FFDAC1', alpha=0.3)  # 填充务工返程曲线

white_collar_back_line, = ax.plot(x_smooth, white_collar_back_smooth, color='#FFB7B2', linewidth=2.5, label='白领（返程）')
ax.fill_between(x_smooth, white_collar_back_smooth, color='#FFB7B2', alpha=0.3)  # 填充白领返程曲线

# 5. 设置x轴刻度
plt.xticks(x_uniform, dates)
plt.xticks(rotation=30)  

# 6. 添加标题、图例、装饰
ax.set_title('2017春运期人群趋势', fontsize=18, fontweight='bold', color='#333')
ax.set_xlabel('日期', fontsize=14, color='#555')
ax.set_ylabel('人群规模', fontsize=14, color='#555')
ax.legend(loc='upper right', fontsize=11)  

# 7. 添加分隔线（春节位置）
plt.axvline(x=6.0, color='red', linestyle='--', alpha=0.5)
plt.text(5.6, max(student_go.max(), worker_go.max(), white_collar_go.max()) * 0.95, 
         '春节', fontsize=13, color='red')

# 8. 添加网格线
plt.grid(True, linestyle='--', alpha=0.6)

# 9. 隐藏顶部、右侧边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 10. 显示图表
plt.tight_layout()  
plt.show()