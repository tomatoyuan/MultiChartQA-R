import matplotlib.pyplot as plt
import numpy as np

# -------------------- 数据定义 --------------------
categories = [
    "睡眠问题",
    "容易疲劳/精力不足",
    "精神压力大",
    "免疫力（少生病/不生病）问题",
    "皮肤健康问题",
    "视力问题",
    "头发问题（如脱发）",
    "肩颈酸痛",
    "情绪低落/焦虑",
    "记忆力问题",
    "延缓衰老",
    "内分泌问题",
    "三高问题",
    "肥胖/超重",
    "心脑血管问题",
    "骨骼关节问题",
    "抑郁",
    "糖尿病"
]

# 模拟数据（前3项为绿色，其余为灰色）
percentages = [61.1, 50.5, 48.9, 45.9, 44.2, 43.3, 42.2, 42.1, 40.8, 36.9, 28.1, 22.9, 20.7, 20.7, 15.5, 15.5, 9.3, 5.3]

# 颜色配置（前3项绿色，其余灰色）
colors = ["#a5d6a7"]*3 + ["#dcdcdc"]*(len(categories)-3)

# -------------------- 创建画布 --------------------
fig, ax = plt.subplots(figsize=(10, 8))

# -------------------- 绘制横向条形图 --------------------
y = np.arange(len(categories))

bars = ax.barh(
    y, 
    percentages, 
    color=colors, 
    height=0.6,
    edgecolor="white",
    linewidth=1
)

# -------------------- 添加百分比标注 --------------------
for bar in bars:
    width = bar.get_width()
    ax.text(
        width + 1,  # 右侧偏移1个单位
        bar.get_y() + bar.get_height()/2,
        f"{width}",
        va="center",
        fontsize=9,
        fontweight="bold",
        color="#424242"
    )

# -------------------- 美化图表 --------------------
# 设置y轴标签
ax.set_yticks(y)
ax.set_yticklabels(categories, fontsize=11, color="#424242")

# 隐藏x轴
ax.set_xticks([])

# 隐藏边框
for spine in ax.spines.values():
    spine.set_visible(False)

ax.tick_params(axis="y", left=False)  # 隐藏y轴刻度线

# 添加标题
ax.set_title(
    "18-65岁成年阶段的健康关注（%）",
    fontsize=14,
    fontweight="bold",
    pad=20,
    loc="right"  # 模拟原图标题位置
)

# 调整布局
plt.tight_layout()

plt.show()