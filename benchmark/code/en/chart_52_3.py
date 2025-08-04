import matplotlib.pyplot as plt
import numpy as np

# -------------------- Data definition --------------------
# Pie chart data
pie_labels = ["Have a clear plan for post - graduation development", "No clear plan"]
pie_sizes = [94.6, 5.4]
pie_colors = ["#81c784", "#b0bec5"]  # Green color scheme similar to the original image

# Bar chart data (Sub - categories of clear plans)
bar_categories = ["Further education", "Employment", "Civil service exam", "Study abroad"]
bar_values = [41.0, 34.8, 15.5, 3.3]
bar_colors = ["#a5d6a7", "#81c784", "#c8e6c9", "#e8f5e9"]  # Gradient of the same color scheme

# -------------------- Create the canvas and sub - plots --------------------
fig, (ax_pie, ax_bar) = plt.subplots(1, 2, figsize=(12, 5), 
                                     gridspec_kw={'width_ratios': [1, 2]})

# -------------------- Draw the pie chart --------------------
wedges, text_labels, auto_texts = ax_pie.pie(
    pie_sizes, 
    labels=None,  # Do not display labels temporarily, show through the legend
    autopct='%1.1f%%',
    startangle=90,
    colors=pie_colors,
    textprops={'fontsize': 12},
    wedgeprops={'linewidth': 2, 'edgecolor': 'white'}
)

# Set the color of percentage texts
for text in auto_texts:
    text.set_color('white')
    text.set_fontweight('bold')

# Add a legend to show full labels
ax_pie.legend(
    wedges, 
    pie_labels, 
    loc='center left', 
    bbox_to_anchor=(-1.1, 0.5),
    fontsize=10
)

# Adjust the position of the pie chart
ax_pie.set_position([0.05, 0.1, 0.3, 0.8])

# -------------------- Draw the bar chart --------------------
bar_width = 0.6
x = np.arange(len(bar_categories))

# Draw the basic bar chart
bars = ax_bar.barh(
    x, 
    bar_values, 
    color=bar_colors, 
    height=0.6,
    edgecolor='white',
    linewidth=1
)

# Add numerical annotations
for bar in bars:
    width = bar.get_width()
    ax_bar.text(
        width + 1,  # Offset 1 unit to the right
        bar.get_y() + bar.get_height()/2,
        f'{width}%',
        va='center',
        fontsize=10,
        fontweight='bold',
        color='#424242'
    )

# Beautify the bar chart
ax_bar.set_yticks(x)
ax_bar.set_yticklabels(bar_categories, fontsize=12, color='#424242')
ax_bar.set_xlim(0, 50)  # Similar to the original image ratio
ax_bar.set_xticks([])   # Hide the x - axis ticks
ax_bar.spines['top'].set_visible(False)
ax_bar.spines['right'].set_visible(False)
ax_bar.spines['bottom'].set_visible(False)
ax_bar.spines['left'].set_visible(False)
ax_bar.tick_params(axis='y', left=False)

# Adjust the position of the bar chart
ax_bar.set_position([0.4, 0.1, 0.5, 0.8])

# -------------------- Global beautification --------------------
# Add the main title
fig.suptitle(
    "College students' plans for post - graduation development", 
    fontsize=16, 
    fontweight='bold', 
    y=0.95,
    x=0.3
)

# Add a connecting arrow
import matplotlib.patches as patches
arrow = patches.FancyArrow(
    0.35, 0.5, 0.05, 0, 
    width=0.02, 
    head_width=0.05, 
    head_length=0.03, 
    color='#81c784',
    transform=fig.transFigure,
    figure=fig
)
fig.patches.append(arrow)

# Adjust the layout
plt.subplots_adjust(wspace=0.2)

plt.show()