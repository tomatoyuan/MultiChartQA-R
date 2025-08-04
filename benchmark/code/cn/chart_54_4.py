import matplotlib.pyplot as plt
import numpy as np

# -------------------- 数据定义 --------------------
categories = [
    "视力问题",
    "生长发育问题",
    "免疫力问题",
    "强健骨骼/促进骨骼发育",
    "专注力",
    "精神压力大",
    "记忆力问题",
    "促进肠胃消化",
    "情绪低落",
    "睡眠问题（如失眠、睡眠浅）",
    "皮肤健康（如冒痘等）问题",
    "容易疲劳/精力不足",
    "肥胖/超重",
    "头发问题（如脱发）",
    "抑郁",
    "三高问题（高血脂/血压/血糖）",
    "糖尿病"
]

# 模拟数据（前4项为绿色，其余为灰色）
percentages = [61.1, 55.6, 52.5, 49.1, 41.3, 36.2, 34.6, 34.2, 26.6, 24.5, 24.3, 21.2, 19.7, 12.3, 10.9, 6.7, 4.5]

# 颜色配置（前4项绿色，其余灰色）
colors = ["#a5d6a7"]*4 + ["#dcdcdc"]*(len(categories)-4)

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
    "7-17岁青少年阶段的健康关注（%）",
    fontsize=14,
    fontweight="bold",
    pad=20,
    loc="right"  # 模拟原图标题位置
)

# 调整布局
plt.tight_layout()

plt.show()