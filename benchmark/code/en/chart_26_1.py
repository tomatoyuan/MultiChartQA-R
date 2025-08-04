import matplotlib.pyplot as plt

# Data
labels = ['Female', 'Male']
sizes = [35, 65]
colors = ['#FF69B4', '#4169E1']  # Corresponding to pink and blue
explode = (0.05, 0)  # Highlight the female part

# Create a canvas and sub - plot
fig, ax = plt.subplots(figsize=(8, 6), facecolor='#666666')

# Draw a donut chart
wedges, texts, autotexts = ax.pie(
    sizes,
    explode=explode,
    colors=colors,
    autopct=lambda p: f'{p:.1f}%\n({int(p*sum(sizes)/100)})',  # Display percentage and actual quantity
    startangle=90,
    wedgeprops=dict(width=0.4, edgecolor='w', linewidth=2),
    textprops=dict(fontsize=12)
)

# Set the title and subtitle
ax.set_title('Analysis of Gender Ratio of Valentine\'s Day Gift Searches', fontsize=18, fontweight='bold', pad=20)

# Beautify the text style - Fixed version (using texts and autotexts returned by the pie chart)
for text in texts:
    text.set_color('#666666')  # Dark gray text
    text.set_fontsize(14)
    text.set_fontweight('bold')

for autotext in autotexts:
    autotext.set_color('white')  # Keep the percentage text white (for contrast with the dark background)
    autotext.set_fontsize(12)
    autotext.set_fontweight('bold')

# Add a legend and annotation
ax.legend(wedges, labels, title="Gender", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.annotate(
    'Higher proportion of male searches',
    xy=(0.5, 0.5),
    xytext=(0.7, 0.7),
    arrowprops=dict(arrowstyle='->', color='#333333'),
    fontsize=12,
    ha='center'
)

# Set the background and layout
plt.tight_layout()
plt.subplots_adjust(right=0.8)  # Make space for the legend
plt.axis('equal')  # Ensure the pie chart is circular

# Save the chart (optional)
# plt.savefig('valentines_gift_gender_pie.png', dpi=300, bbox_inches='tight')

# Display the chart
plt.show()