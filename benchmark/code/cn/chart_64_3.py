import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# 设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 数据定义
factors = [
    {"name": "提升用户转化促进业绩增长", "percent": 50.4},
    {"name": "私域搭建与运营成本", "percent": 48.8},
    {"name": "有效实现公域引流", "percent": 46.3},
    {"name": "提升用户对品牌的粘性", "percent": 43.9},
    {"name": "丰富的运营玩法", "percent": 39.8},
    {"name": "便捷的私域触达", "percent": 37.4},
    {"name": "线上与线下渠道的融合打通", "percent": 29.3},
    {"name": "私域数据可沉淀、可分析", "percent": 27.6},
]

# 准备热力图数据
factor_names = [f["name"] for f in factors][::-1]  # y轴方向反转
percent_values = np.array([f["percent"] for f in factors])[::-1].reshape(-1, 1)

# 创建画布
fig, ax = plt.subplots(figsize=(6, 7))

# 使用自定义暖色调颜色映射
cmap = sns.light_palette("orangered", as_cmap=True)

# 绘制热力图
sns.heatmap(
    percent_values,
    annot=True,
    fmt=".1f",
    cmap=cmap,
    cbar=False,
    yticklabels=factor_names,
    xticklabels=["关注度 (%)"],
    linewidths=0.5,
    linecolor="white",
    annot_kws={"fontsize": 10, "weight": "bold", "color": "#4B1E00"},
    ax=ax
)

# 设置标题
ax.set_title("2022年品牌/商户私域布局与经营关注因素", fontsize=14, fontweight="bold", pad=20)

# 美化坐标轴
ax.tick_params(axis='y', labelsize=10)
ax.tick_params(axis='x', labelsize=10)
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()