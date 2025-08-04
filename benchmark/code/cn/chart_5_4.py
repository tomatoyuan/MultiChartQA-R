import matplotlib.pyplot as plt
import numpy as np

# 日期（x 轴，转换为数字方便绘图，实际显示仍用原始日期）
dates = np.arange(1, 29, 2)
date_labels = ['2.1', '2.3', '2.5', '2.7', '2.9', '2.11', '2.13', '2.15', '2.17', '2.19', '2.21', '2.23', '2.25', '2.27']

# 各类奶粉搜索关注度（y 轴）
children_milk = [1000, 1200, 1300, 1500, 1400, 1450, 1420, 1430, 1400, 4000, 1300, 1200, 1100, 1000]
pregnant_milk = [15000, 20000, 25000, 30000, 28000, 28500, 29000, 29500, 28000, 25000, 30000, 25000, 40000, 18000]
infant_milk = [2000, 2200, 2300, 2400, 2350, 2400, 2420, 2430, 2400, 2500, 2300, 2200, 2100, 2000]
student_milk = [2500, 2600, 2700, 2800, 2750, 2800, 2820, 2830, 2800, 2900, 2700, 2600, 2500, 2400]

# 绘图
plt.figure(figsize=(14, 8))

# 绘制折线图
children_line, = plt.plot(dates, children_milk, color='orange', label='儿童奶粉', linewidth=2)
infant_line, = plt.plot(dates, infant_milk, color='blue', label='婴儿奶粉', linewidth=2)
pregnant_line, = plt.plot(dates, pregnant_milk, color='pink', label='孕妇奶粉', linewidth=2)
student_line, = plt.plot(dates, student_milk, color='lightblue', label='学生奶粉', linewidth=2)

# 设置 x 轴刻度与标签
plt.xticks(dates, date_labels, rotation=45)

# 设置标题、坐标轴标签
plt.title('2月分品类搜索关注度趋势', fontsize=16)
plt.xlabel('日期', fontsize=12)
plt.ylabel('搜索关注度', fontsize=12)

# 添加网格线
plt.grid(True, linestyle='--', alpha=0.7)

# 为数据点添加智能标注，避免重叠
def add_smart_annotations(x, y, color, label, is_pregnant=False):
    """为数据点添加智能标注，避免重叠"""
    # 收集所有已放置的标注位置
    placed_annotations = []
    
    for i, (date, value) in enumerate(zip(x, y)):
        # 格式化数值，添加千位分隔符
        value_str = f"{value:,}"
        
        # 基础偏移量
        base_offset = 15
        
        # 为孕妇奶粉设置更大的基础偏移量
        if is_pregnant:
            base_offset = 30
        
        # 检查是否与已有标注重叠
        overlaps = True
        attempts = 0
        max_attempts = 8
        offset = base_offset
        
        while overlaps and attempts < max_attempts:
            # 尝试不同的角度和距离来放置标注
            angle = (attempts % 4) * 90  # 0, 90, 180, 270 度
            distance = base_offset + (attempts // 4) * 10  # 每两次尝试增加距离
            
            # 计算偏移量
            if angle == 0:  # 右侧
                xytext = (distance, 0)
                ha = 'left'
                va = 'center'
            elif angle == 90:  # 上方
                xytext = (0, distance)
                ha = 'center'
                va = 'bottom'
            elif angle == 180:  # 左侧
                xytext = (-distance, 0)
                ha = 'right'
                va = 'center'
            else:  # 下方
                xytext = (0, -distance)
                ha = 'center'
                va = 'top'
            
            # 检查是否重叠
            overlaps = False
            for (x_annot, y_annot) in placed_annotations:
                # 计算距离
                dist = np.sqrt((date - x_annot)**2 + (value - y_annot)**2)
                # 如果距离太近，认为重叠
                if dist < 30:  # 阈值可以调整
                    overlaps = True
                    break
            
            if not overlaps:
                # 不重叠，记录这个位置
                placed_annotations.append((date + xytext[0]/10, value + xytext[1]/10))
                break
            
            attempts += 1
        
        # 如果尝试多次仍无法找到不重叠的位置，使用默认位置
        if overlaps:
            xytext = (0, base_offset)
            ha = 'center'
            va = 'bottom'
        
        # 添加标注
        plt.annotate(value_str,
                    (date, value),
                    textcoords="offset points",
                    xytext=xytext,
                    ha=ha,
                    va=va,
                    fontsize=8,
                    color=color,
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=color, alpha=0.8))

# 为各类奶粉添加智能标注
add_smart_annotations(dates, children_milk, 'orange', '儿童奶粉')
add_smart_annotations(dates, infant_milk, 'blue', '婴儿奶粉')
add_smart_annotations(dates, pregnant_milk, 'pink', '孕妇奶粉', True)
add_smart_annotations(dates, student_milk, 'lightblue', '学生奶粉')

# 添加图例
plt.legend(fontsize=10, loc='upper left')

# 添加数据来源说明
plt.figtext(0.1, 0.01, '数据来源：虚构数据，仅作示例', ha="left", fontsize=9, bbox={"facecolor":"white", "alpha":0.5, "pad":5})

# 优化布局
plt.tight_layout()

# 显示图表
plt.show()