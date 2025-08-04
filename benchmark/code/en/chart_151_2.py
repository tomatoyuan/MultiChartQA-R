import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), gridspec_kw={'width_ratios': [1, 1.2]})
fig.suptitle('Overall Online | Proportion of Health Food Sub - categories and Sales Growth Rate % | MAT2406', fontsize=14)

# Pie chart
labels = ['Dietary Nutritional Supplements', 'Traditional Tonic']
sizes = [74.9, 25.1]
colors = ['#003399', '#99bbff']
explode = (0, 0.05)

wedges, texts, autotexts = ax1.pie(
    sizes, labels=labels, autopct='%1.1f%%', startangle=90, counterclock=False,
    colors=colors, wedgeprops=dict(width=0.4, edgecolor='w'), explode=explode, textprops={'fontsize': 10}
)
ax1.set_title('Category Proportion')

# Bar chart
sub_categories = ['Health Food', 'Dietary Nutritional Supplements', 'Traditional Tonic']
growth_rates = [10.1, 11.5, 5.9]
bar_colors = ['#002060', '#0056d6', '#7faaff']

bars = ax2.bar(sub_categories, growth_rates, color=bar_colors)

for bar, value in zip(bars, growth_rates):
    ax2.text(bar.get_x() + bar.get_width()/2, value + 0.3, f'{value}%', ha='center', va='bottom', fontsize=11)

# 样式调整
ax2.set_ylim(0, 13)
ax2.set_ylabel('Year - on - Year Growth Rate (%)')
ax2.set_title('Sales Growth Rate')
ax2.grid(axis='y', linestyle='--', alpha=0.5)
ax2.set_facecolor('#f5f7fa')

# 关键调整：倾斜横坐标文字
ax2.tick_params(axis='x', labelrotation=20)

plt.tight_layout()
plt.show()