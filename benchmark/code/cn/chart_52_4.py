import matplotlib.pyplot as plt
import numpy as np

# -------------------- 数据定义 --------------------
categories = [
    "学术交流活动",
    "科研机会",
    "学术资源获取",
    "科研工具与方法",
    "学科前沿动态",
    "完全不关注学术类内容"
]

values = [67.2, 52.6, 51.4, 40.6, 37.1, 0.9]

# 贴近原图的绿色系
colors = [
    "#a5d6a7", "#81c784", "#c8e6c9", 
    "#e8f5e9", "#b9f6ca", "#f5f5f5"
]

# -------------------- 创建画布 --------------------
fig, ax = plt.subplots(figsize=(8, 5))

# -------------------- 绘制横向条形图 --------------------
y = np.arange(len(categories))

# 绘制基础条形图
bars = ax.barh(
    y, 
    values, 
    color=colors, 
    edgecolor='white',
    linewidth=1
)

# 添加数值标注
for bar in bars:
    width = bar.get_width()
    ax.text(
        width + 1,  # 右侧偏移1个单位
        bar.get_y() + bar.get_height()/2,
        f'{width}%',
        va='center',
        fontsize=10,
        fontweight='bold',
        color='#424242'
    )

# -------------------- 美化图表 --------------------
# 设置y轴标签
ax.set_yticks(y)
ax.set_yticklabels(categories, fontsize=12, color='#424242')

# 隐藏x轴
ax.set_xticks([])

# 隐藏边框
for spine in ax.spines.values():
    spine.set_visible(False)

# 调整y轴位置（让条形图贴近左侧）
ax.tick_params(axis='y', left=False)

# 添加标题
ax.set_title(
    "大学生对学术内容的关注情况", 
    fontsize=14, 
    fontweight='bold', 
    pad=20
)

# 调整布局
plt.subplots_adjust(left=0.3, right=0.9, top=0.85, bottom=0.2)

plt.show()