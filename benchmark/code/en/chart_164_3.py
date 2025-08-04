import matplotlib.pyplot as plt

# Data
labels = ['Soft fabric', 'Fits well and is skin - friendly', 'Breathable and keeps dry', 'Lightweight and easy to carry', 'Elastic and convenient for stretching', 'Warm']
values = [75, 72, 69, 66, 57, 55]
colors = ['#c49e6c', '#b88d59', '#a87d4a', '#98703d', '#88612f', '#7a5325']

# Create a bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(labels, values, color=colors)

# Add numerical labels
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom')

# Beautify the chart
ax.set_title("Consumers' specific requirements for comfort (shown in a bar chart)", fontsize=14)
ax.set_ylabel("Proportion (%)")
ax.set_ylim(0, 80)
plt.xticks(rotation=30)
plt.tight_layout()

# Add data source description
plt.figtext(0.5, -0.05,
            "Data source: CBNData's survey on the trendy of luxury outdoor clothing in China in May 2024.\nData description: What specific requirements do you have for the comfort of outdoor clothing? N = 571",
            wrap=True, horizontalalignment='center', fontsize=10)

plt.show()