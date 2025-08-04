import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime

# 原始关键数据点
dates = [
    datetime.datetime(2024, 8, 16),
    datetime.datetime(2024, 8, 30),
    datetime.datetime(2024, 9, 15),
    datetime.datetime(2024, 9, 25),  # 激增点
    datetime.datetime(2024, 10, 15),
    datetime.datetime(2024, 11, 4),
    datetime.datetime(2024, 11, 24),
    datetime.datetime(2024, 12, 11)
]

ai_index = [0, -5, -3, 23, 20, 36, 35, 42.3]
sh_index = [0, 1, -2, 17, 18, 12, 16, 19.3]

# 将日期转换为数值
x = mdates.date2num(dates)

# 生成更密集的日期点（每日数据）
start_date = dates[0]
end_date = dates[-1]
delta = end_date - start_date
all_dates = [start_date + datetime.timedelta(days=i) for i in range(delta.days + 1)]
all_x = mdates.date2num(all_dates)

# 市场波动生成函数（全曲线均匀波动）
def generate_market_volatility(x, y, all_x, volatility=0.03, persistence=0.7):
    """
    生成全曲线均匀波动的市场数据
    
    参数:
    x: 原始数据点的x坐标
    y: 原始数据点的y坐标
    all_x: 需要生成数据的所有x坐标
    volatility: 波动强度系数
    persistence: 波动方向持续性（0-1之间）
    """
    # 对原始数据进行三次样条插值，得到基础曲线
    from scipy.interpolate import make_interp_spline
    spl = make_interp_spline(x, y, k=3)
    base_curve = spl(all_x)
    
    # 计算每日波动幅度（基于基础曲线的百分比）
    daily_volatility = np.abs(base_curve) * volatility
    
    # 生成具有方向持续性的随机游走波动
    n_points = len(all_x)
    noise = np.zeros(n_points)
    direction = 1  # 初始方向
    
    for i in range(1, n_points):
        # 以(1-persistence)的概率改变方向
        if np.random.random() > persistence:
            direction = -direction
        
        # 生成该点的波动值（使用拉普拉斯分布增加极端值）
        noise[i] = np.random.laplace(0, daily_volatility[i]) * direction
    
    # 累积波动，形成随机游走
    cumulative_noise = np.cumsum(noise)
    
    # 确保端点与原始数据一致
    # 计算需要调整的偏移量，使最终点回到原始值
    offset = y[-1] - (base_curve[-1] + cumulative_noise[-1])
    adjusted_noise = cumulative_noise + offset * np.linspace(0, 1, n_points)
    
    # 最终波动曲线 = 基础曲线 + 调整后的波动
    final_curve = base_curve + adjusted_noise
    
    return final_curve

# 生成全曲线均匀波动的数据
ai_volatile = generate_market_volatility(x, ai_index, all_x, volatility=0.04, persistence=0.6)
sh_volatile = generate_market_volatility(x, sh_index, all_x, volatility=0.025, persistence=0.7)

# 创建图表
fig, ax = plt.subplots(figsize=(16, 9))

# 绘制波动曲线
line_ai, = ax.plot(all_x, ai_volatile, label='AI眼镜指数 (886085)', 
                   color='#32CD32', linewidth=1.6, alpha=0.9)
line_sh, = ax.plot(all_x, sh_volatile, label='上证指数 (000001)', 
                   color='#1E90FF', linewidth=1.6, alpha=0.9, linestyle='--')

# 标注最终涨跌幅
ax.text(all_x[-1], ai_volatile[-1], f'{ai_volatile[-1]:.1f}%', ha='left', va='bottom', 
        color='#32CD32', fontweight='bold', fontsize=12, bbox=dict(facecolor='white', alpha=0.7))
ax.text(all_x[-1], sh_volatile[-1], f'{sh_volatile[-1]:.1f}%', ha='left', va='bottom', 
        color='#1E90FF', fontweight='bold', fontsize=12, bbox=dict(facecolor='white', alpha=0.7))

# 设置x轴为日期格式，控制显示密度
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))  # 每周显示一个日期
plt.xticks(rotation=45, fontsize=10)

# 设置标题和图例
ax.set_title('AI眼镜指数及上证指数累计涨跌幅对比\n(2024/8/16-2024/12/11)', 
             fontsize=17, pad=15, fontweight='bold')
ax.legend(loc='upper left', frameon=True, framealpha=0.9, fontsize=12)

# 设置y轴为百分比格式
ax.set_ylabel('累计涨跌幅 (%)', fontsize=13)
ax.set_ylim(-30, 70)  # 进一步扩大y轴范围，适应更大波动

# 显示网格
ax.grid(True, linestyle='--', alpha=0.6, which='both')

# 突出显示关键日期的垂直线
ax.axvline(x[3], color='gray', linestyle='-.', alpha=0.5)  # 2024/9/25

# 添加背景色区分不同时间段
for i in range(len(x)-1):
    if i == 3:  # 激增点之后的区域
        ax.axvspan(x[i], x[i+1], color='lightgreen', alpha=0.1)
    else:
        ax.axvspan(x[i], x[i+1], color='white' if i%2==0 else 'lightgray', alpha=0.1)

# 美化图表边框
for spine in ax.spines.values():
    spine.set_color('gray')
    spine.set_linewidth(1)

# 添加波动说明
ax.text(0.02, 0.02, '注：波动均匀作用于整条曲线，符合市场连续波动特性', 
        transform=ax.transAxes, fontsize=10, color='gray')

# 调整布局
plt.tight_layout()
plt.show()