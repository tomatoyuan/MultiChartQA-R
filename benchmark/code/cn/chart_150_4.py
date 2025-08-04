import matplotlib.pyplot as plt
import numpy as np

# 数据整理（按指标、满意度等级顺序：非常满意、较满意、一般、较不满意、非常不满意 ）
metrics = [
    "服务便捷度", "清洁卫生情况", "服务体验感", 
    "与宣传信息一致度", "价格合理度", "安全性", "优惠促销活动"
]
# 每个指标下各满意度等级的占比（%）
data = np.array([
    [57, 34, 7, 2, 0],   # 服务便捷度
    [50, 41, 7, 2, 0],   # 清洁卫生情况
    [50, 40, 10, 0, 0],  # 服务体验感
    [49, 40, 8, 3, 0],   # 与宣传信息一致度
    [44, 44, 10, 4, 0],  # 价格合理度
    [51, 37, 10, 3, 0],  # 安全性
    [49, 38, 11, 2, 0]   # 优惠促销活动
])
# 各满意度等级的配色（贴近原图）
colors = ["#f8cecc", "#f4a460", "#ff8c00", "#cd5c5c", "#8b0000"]
# 满意度等级标签
labels = ["非常满意", "较满意", "一般", "较不满意", "非常不满意"]

x = np.arange(len(metrics))  # x轴坐标（每个指标对应一个位置）
bar_width = 0.8  # 柱子宽度，让分段更紧凑

fig, ax = plt.subplots(figsize=(12, 8))

# 绘制分段堆积柱状图
bottom = np.zeros(len(metrics))  # 堆积的起始位置
for i in range(5):
    ax.bar(
        x, 
        data[:, i], 
        width=bar_width, 
        color=colors[i], 
        bottom=bottom, 
        label=labels[i] if i == 0 else ""  # 仅第一个等级显示图例，避免重复
    )
    bottom += data[:, i]  # 更新下一段的起始位置

ax.set_title('2023年中国本地服务用户到店服务体验满意情况调查', fontsize=14)
ax.set_ylabel('占比（%）')
ax.set_xticks(x)
ax.set_xticklabels(metrics, rotation=45, ha='right')
ax.legend(title='满意度等级', loc='upper right')

# 添加数值标注（仅标注“非常满意”和“较满意”，因原图仅显示这两部分数值；若需全标注可扩展循环）
for i in range(len(metrics)):
    # 标注“非常满意”数值
    ax.text(x[i], data[i, 0]/2, f'{data[i, 0]}%', ha='center', va='center', color='black')
    # 标注“较满意”数值
    ax.text(x[i], data[i, 0] + data[i, 1]/2, f'{data[i, 1]}%', ha='center', va='center', color='black')
    # 若需标注“一般”“较不满意”“非常不满意”，可继续添加：
    # ax.text(x[i], data[i, 0]+data[i, 1]+data[i, 2]/2, f'{data[i, 2]}%', ...) 

plt.tight_layout()
plt.show()