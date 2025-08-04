import matplotlib.pyplot as plt

# 数据 - 按图表顺序：人体工学椅、护眼灯、升降桌；代际顺序 05后→00后→95后→90后→85后→80后
categories = ["人体工学椅", "护眼灯", "升降桌"]
generations = ["05后", "00后", "95后", "90后", "85后", "80后"]
# 1 表示有方格填充，0 表示无，与图表对应
data = {
    "人体工学椅": [0, 0, 1, 1, 1, 1],  
    "护眼灯": [1, 0, 0, 0, 1, 1],     
    "升降桌": [1, 0, 1, 0, 1, 0]      
}

# 总百分比（与图表一致）
total_percentages = {
    "人体工学椅": 66,
    "护眼灯": 55,
    "升降桌": 53
}

# 自定义颜色（贴近原图橙色系）
colors = {
    "人体工学椅": "#F8C4B4",  # 浅橙色，贴近原图人体工学椅颜色
    "护眼灯": "#F8C4B4",    # 浅橙色，护眼灯颜色
    "升降桌": "#F8C4B4"     # 浅橙色，升降桌颜色
}

# 创建画布
fig, ax = plt.subplots(figsize=(10, 5))  # 调整画布大小适配

# 设置网格参数
grid_size = 0.8   # 方格大小
spacing = 0.2     # 方格间距
label_width = 2   # 左侧标签区域宽度

# 绘制内容
for i, cat in enumerate(categories):
    # 左侧标签背景（浅橙色半透）
    rect_bg = plt.Rectangle(
        (0, i * (grid_size + spacing)),
        label_width, grid_size,
        facecolor=colors[cat],
        alpha=0.3,
        edgecolor='none'
    )
    ax.add_patch(rect_bg)
    
    # 物品名称
    ax.text(
        label_width * 0.25,  
        i * (grid_size + spacing) + grid_size/2,
        cat,
        ha='left',
        va='center',
        color='black',
        fontweight='bold',
        fontsize=12
    )
    
    # 百分比标签
    ax.text(
        label_width * 0.75,  
        i * (grid_size + spacing) + grid_size/2,
        f'{total_percentages[cat]}%',
        ha='right',
        va='center',
        color='black',
        fontweight='bold',
        fontsize=12
    )
    
    # 绘制数据方格
    for j, value in enumerate(data[cat]):
        if value == 1:  # 有值则绘制方格
            rect = plt.Rectangle(
                (label_width + j * (grid_size + spacing), i * (grid_size + spacing)),
                grid_size, grid_size,
                facecolor=colors[cat],
                edgecolor='white',
                alpha=1
            )
            ax.add_patch(rect)

# 设置坐标轴范围
ax.set_xlim(0, label_width + len(generations) * (grid_size + spacing))
ax.set_ylim(0, len(categories) * (grid_size + spacing))

# X轴标签（代际）
x_ticks = [label_width + j * (grid_size + spacing) + grid_size/2 for j in range(len(generations))]
ax.set_xticks(x_ticks)
ax.set_xticklabels(generations, fontsize=11, rotation=0)

# 标题
ax.set_title('消费者最想在书房配备的家具(高亮部分TGI>100表示高偏好)', fontsize=14, pad=20)

# 隐藏多余边框，保留X轴标签
ax.yaxis.set_visible(False)  # 隐藏Y轴
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# 调整布局避免截断
plt.tight_layout()
plt.show()