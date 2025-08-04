import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 数据准备
data = {
    "品牌类型": ["国产传统品牌", "国内新晋品牌", "国际知名品牌", "国外小众品牌"],
    "减少": [24.0, 21.0, 30.3, 31.4],
    "基本没有变化": [49.1, 52.1, 48.6, 54.7],
    "变多": [26.9, 26.9, 21.1, 13.9]
}
df = pd.DataFrame(data).set_index("品牌类型")

# 创建热力图（带数值标注）
plt.figure(figsize=(8, 6))
sns.heatmap(df, annot=True, fmt=".1f", cmap="Oranges", 
            cbar=False, annot_kws={"size": 10, "color": "black"})

# 调整坐标轴标签与标题
plt.yticks(rotation=0)  # y轴标签横向显示
plt.xlabel("购买频率变化")
plt.ylabel("品牌类型")
plt.title("2023年中国化妆品品牌购买频率变化调查", y=1.03, fontsize=12, fontweight="bold")
# 添加英文标题
plt.suptitle("Survey on the Changes in Purchase Frequency of Cosmetics Brands in China in 2023", 
             y=0.93, fontsize=10, color="gray")

# 模拟原图虚线框（手动标记，需精准坐标可额外计算）
# 标记“变多”列的国产传统、国内新晋品牌
for i in [0, 1]:
    plt.plot([2.2, 2.2], [i+0.5, i+1.5], linestyle="--", color="orange", linewidth=2)
    plt.plot([1.8, 2.6], [i+0.5, i+0.5], linestyle="--", color="orange", linewidth=2)
    plt.plot([1.8, 2.6], [i+1.5, i+1.5], linestyle="--", color="orange", linewidth=2)
# 标记“减少”列的国际知名、国外小众品牌
for i in [2, 3]:
    plt.plot([0.2, 0.2], [i+0.5, i+1.5], linestyle="--", color="orange", linewidth=2)
    plt.plot([-0.2, 0.8], [i+0.5, i+0.5], linestyle="--", color="orange", linewidth=2)
    plt.plot([-0.2, 0.8], [i+1.5, i+1.5], linestyle="--", color="orange", linewidth=2)

plt.tight_layout()
plt.show()