import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# 数据
labels = ["防脱胎发", "去油推松", "补水保湿", "深层清洁", "发色亮澄",
          "改善发开发", "强挽防断发", "改善毛囊", "去屉去痒"]
columns = ["05后", "00后", "95后", "90后", "85后", "80前"]
data = [
    [96, 120, 105, 114, 95, 49],
    [101, 130, 82, 100, 96, 121],
    [160, 88, 119, 90, 58, 123],
    [104, 95, 72, 96, 120, 124],
    [121, 93, 109, 67, 122, 87],
    [78, 43, 117, 113, 147, 116],
    [45, 74, 132, 106, 85, 100],
    [95, 78, 107, 132, 60, 85],
    [85, 93, 105, 96, 115, 98]
]

# 创建 DataFrame
df = pd.DataFrame(data, index=labels, columns=columns)

# 设置低于100为白色
masked_df = df.copy()
masked_df[df < 100] = np.nan

# 选择色系
cmap = sns.light_palette("deeppink", as_cmap=True)

# 绘制热力图
plt.figure(figsize=(10, 6))
sns.heatmap(masked_df, annot=df, fmt="d", cmap=cmap, linewidths=0.5, linecolor='grey', cbar=True,
            mask=df < 100, annot_kws={"size": 10}, square=False)

# 设置标题和样式
plt.title("不同代际女性对头皮健康需求调研 (TGI>100)", fontsize=14)
plt.xticks(rotation=0)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()