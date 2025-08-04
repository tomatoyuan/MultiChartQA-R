import matplotlib.pyplot as plt
import numpy as np

# Data
years = ['2022', '2023']
medical_health = [4.08, 4.64]
supplements = [67.09, 70.83]
traditional = [28.83, 24.53]

bar_width = 0.5
x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(8, 6))

# Draw a stacked bar chart
p1 = ax.bar(x, traditional, bar_width, label='Traditional tonics and nutritional products', color='#b2df8a')
p2 = ax.bar(x, supplements, bar_width, bottom=traditional, label='Health supplements/dietary nutritional supplements', color='#fdbf6f')
bottom2 = [traditional[i] + supplements[i] for i in range(len(x))]
p3 = ax.bar(x, medical_health, bar_width, bottom=bottom2, label='Medical care', color='#1f78b4')

# Add text labels
for i in range(len(x)):
    ax.text(x[i], traditional[i] / 2, f'{traditional[i]:.2f}%', ha='center', va='center', fontsize=10)
    ax.text(x[i], traditional[i] + supplements[i] / 2, f'{supplements[i]:.2f}%', ha='center', va='center', fontsize=10)
    ax.text(x[i], bottom2[i] + medical_health[i] / 2, f'{medical_health[i]:.2f}%', ha='center', va='center', fontsize=10)

# Set labels and title
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=12)
ax.set_ylabel('Sales proportion (%)')
ax.set_title('Sales proportion of different categories on Douyin and Kuaishou e - commerce platforms from 2022 to 2023', fontsize=14, weight='bold')
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Data source annotation
plt.figtext(0.5, -0.05, 'Data source: Feigua Data (feigua.cn), Statistical platforms: Douyin, Kuaishou, Data period: 2022.01 - 2024.03',
            wrap=True, horizontalalignment='center', fontsize=9)

plt.tight_layout()
plt.show()