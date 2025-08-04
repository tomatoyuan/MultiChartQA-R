import matplotlib.pyplot as plt
import numpy as np

# -------------------- 数据定义 --------------------
motivations = [
    "眼镜磨损、老化或损坏，影响使用",
    "眼镜佩戴不舒适（视物不舒适/镜框不舒适）",
    "对眼镜的功能需求改变，配功能性眼镜",
    "视力/眼睛度数变化",
    "镜框局部松动，佩戴不稳定",
    "专业医生建议更换/定期换镜",
    "想改变形象/尝试新风格",
    "原来的眼镜使用时间久，失去新鲜感",
    "为日常穿搭搭配新的款式",
    "追随当下潮流或明星/达人同款",
    "满足不同场景需要，在不同场景分别放置眼镜方便使用"
]
percentages = [39.2, 35.9, 35.5, 30.6, 30.6, 28.3, 24.0, 23.7, 19.5, 18.3, 14.8]  # 占比（%）

# 颜色配置（贴近原图绿色渐变）
bar_color = "#a5d6a7"

# -------------------- 创建画布 --------------------
fig, ax = plt.subplots(figsize=(8, 6))

# -------------------- 绘制横向条形图 --------------------
y = np.arange(len(motivations))

bars = ax.barh(
    y, 
    percentages, 
    color=bar_color, 
    height=0.6,
    edgecolor="white",
    linewidth=1
)

# -------------------- 添加数据标注 --------------------
for i, bar in enumerate(bars):
    width = bar.get_width()
    ax.text(
        width + 1,  # 右侧偏移1个单位
        bar.get_y() + bar.get_height()/2,
        f"{width}%",
        va="center",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

# -------------------- 美化图表 --------------------
# 设置y轴标签（动机描述）
ax.set_yticks(y)
ax.set_yticklabels(motivations, fontsize=10, color="#424242")

# 隐藏x轴
ax.set_xticks([])

# 隐藏顶部和右侧边框
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# 添加标题
ax.set_title(
    "更换眼镜的动机",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# 调整布局
plt.tight_layout()

plt.show()