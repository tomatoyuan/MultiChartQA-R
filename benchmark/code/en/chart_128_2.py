import matplotlib.pyplot as plt
import numpy as np

# Company names
companies = ["Samsung", "Tencent", "Baidu", "Sony", "OPPO", "Ping An Group", "SenseTime", "Canon", "Huawei", "Microsoft"]
# Number of patents (items)
patent_counts = [4094, 4085, 3094, 2637, 2301, 2260, 2194, 2163, 2126, 2108]

x = np.arange(len(companies))

fig, ax = plt.subplots(figsize=(12, 7))
# Draw a bar chart
bars = ax.bar(x, patent_counts, color='orange', label='Number of patents (items)')

# Add numerical labels above the bars
for i, count in enumerate(patent_counts):
    ax.text(i, count + 50, f'{count}', ha='center', va='bottom')

ax.set_ylabel('Number of patents (items)')
ax.set_xlabel('Company names')
ax.set_xticks(x)
ax.set_xticklabels(companies, rotation=45)  # Rotate the x-axis labels to avoid overlap
ax.legend()
ax.set_title('Global VR/AR Invention Patent Counts (Top 10 Companies)')

plt.tight_layout()
plt.show()