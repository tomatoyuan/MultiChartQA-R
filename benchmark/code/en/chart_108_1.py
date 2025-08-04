import matplotlib.pyplot as plt
import numpy as np

# Information channels
channels = ["Weibo/WeChat", "Short - video platforms like Douyin and Kuaishou", "Information platforms like Toutiao and Baidu Hao", "Radio and TV", 
            "Official websites of financial media", "Newspapers/Magazines", "Financial media clients", "Financial blogs/Personal websites", 
            "Professional financial data providers (Wind Information, Flush, etc.)"]
# Corresponding proportions (%)
proportions = [45.61, 44.08, 43.97, 34.32, 31.91, 24.67, 24.23, 18.64, 13.27]

x = np.arange(len(channels))  # x-axis coordinates

fig, ax = plt.subplots(figsize=(10, 6))
# Draw a bar chart
bars = ax.bar(x, proportions, color='orange')

# Add numerical annotations
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# Set x-axis ticks and labels, rotate the labels
ax.set_xticks(x)
ax.set_xticklabels(channels, rotation=15, ha='right')
ax.set_ylabel('Proportion (%)')
ax.set_title('Channels for Chinese financial news users to obtain financial media information in 2025')

plt.tight_layout()
plt.show()