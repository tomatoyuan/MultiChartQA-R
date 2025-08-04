import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

countries = ["中国", "印度", "日本", "美国", "巴西", "土耳其", "泰国", "印度尼西亚"]
market_size = [6, 1, 1, 1, 1, 0.5, 0.5, 0.5]

x = np.arange(len(countries))
sns.barplot(x=countries, y=market_size, palette=['orange'] + ['green']*(len(countries)-1))

# 添加数值标注
for i, v in enumerate(market_size):
    plt.text(i, v + 0.05, f'{v}', ha='center', fontsize=12)

plt.text(0, market_size[0], "超六倍", ha='center', va='bottom', fontsize=14, color='orange')
plt.title("2022年世界主要茶叶国家市场规模估值", fontsize=14, fontweight='bold')
plt.figtext(0.5, 0.01, "单位：亿美元", ha='center', fontsize=12)
plt.yticks([])
plt.tight_layout()  # 调整布局避免文字被遮挡
plt.show()