import matplotlib.pyplot as plt
import numpy as np

# Data definition
brands = ['Apple', 'Huawei', 'Honor', 'Xiaomi', 'OPPO', 'vivo']
tgi_data = [95, 105, 110, 95, 92, 95]  # Attention (TGI) data
search_ratio_raw = [100, 110, 85, 87, 90, 89]  # Raw values of search ratio line chart
search_percent_labels = [30, 44, 5, 7, 10, 8]  # Actual search percentages to be labeled
highlight_huawei = (1, 44)  # Special label for Huawei (index, label value)
highlight_honor = (2, 110)  # Special label for Honor (index, label value)

# Initialize the chart and dual - axis
fig, ax1 = plt.subplots(figsize=(7, 5), dpi=100)
ax2 = ax1.twinx()

# Draw the bar chart (TGI)
x = np.arange(len(brands))  # Specify tick positions clearly
bar_plot = ax1.bar(x, tgi_data, color='#4CAF50', width=0.6, edgecolor='white')
ax1.set_ylim(80, 120)
ax1.set_ylabel('(Attention/TGI)', color='#1f77b4', fontsize=9)
ax1.tick_params(axis='y', labelcolor='#1f77b4', labelsize=8, length=0)  # Remove y - axis tick lines
ax1.set_xticks(x)  # New: Explicitly set tick positions
ax1.set_xticklabels(brands, fontsize=9)
ax1.tick_params(axis='x', length=0)  # Remove x - axis tick lines

# Draw the line chart (Search ratio)
line_plot, = ax2.plot(x, search_ratio_raw, color='#FF9800', marker='o', markersize=5, linewidth=2)
ax2.set_ylim(80, 120)
ax2.set_ylabel('(Search Ratio)', color='#FF9800', fontsize=9)
ax2.tick_params(axis='y', labelcolor='#FF9800', labelsize=8, length=0)  # Remove y - axis tick lines

# Map the right - hand axis to percentages
def map_to_percent(tick):
    return ((tick - 80) / (120 - 80)) * 60

# Customize the right - hand axis ticks and labels
ax2.set_yticks([80, 90, 100, 110, 120])
ax2.set_yticklabels([f'{map_to_percent(tick):.0f}%' for tick in [80, 90, 100, 110, 120]], fontsize=8)

# Add dashed auxiliary lines (refer to the original chart)
for y in [90, 100, 110]:
    ax1.axhline(y, color='gray', linestyle='--', linewidth=0.8)

# Special data labels (Huawei 44%, Honor 110)
# Label for Huawei's line chart point
ax2.text(highlight_huawei[0], search_ratio_raw[highlight_huawei[0]], 
         f'{highlight_huawei[1]}%', 
         ha='center', va='bottom', fontsize=8, color='#FF9800',
         bbox=dict(facecolor='white', edgecolor='gray', pad=2, alpha=0.8))
# Label for Honor's bar chart
ax1.text(highlight_honor[0], tgi_data[highlight_honor[0]] + 1, 
         f'{highlight_honor[1]}', 
         ha='center', va='bottom', fontsize=8, color='black',
         bbox=dict(facecolor='white', edgecolor='gray', pad=2, alpha=0.8))

# Title and annotation
plt.title('Attention (TGI) and Search Ratio of Major Mobile Brands\' Users to New Domestic Products', fontsize=10, fontweight='bold', pad=15)

annotation_text = (
    'Note: During our data statistics period (2019 - 2020), the Honor brand was not independent of Huawei.\n'
    'TGI: Measures attention. A value higher than 100 means the user group\'s attention is higher than the average level.'
)
plt.figtext(0.12, 0.01, annotation_text, fontsize=8, color='gray', wrap=True)

# Legend and layout optimization
ax1.legend([bar_plot, line_plot], ['Attention/TGI', 'Search Ratio'], 
           loc='upper left', fontsize=8, frameon=True, facecolor='white')
plt.tight_layout(pad=3)

# Remove the chart border
for spine in ax1.spines.values():
    spine.set_visible(False)
for spine in ax2.spines.values():
    spine.set_visible(False)

plt.show()