import matplotlib.pyplot as plt



# Data
labels = ['Flesh-colored/Skin-tone style', 'Black style', 'Buy both colors']
sizes = [61, 32, 7]
colors = ['#ffd6d6', '#ff8080', '#ffeaea']  # Gradient pink color matching close to the original image
explode = (0, 0.05, 0.1)  # Highlight the last two items

# Create a figure
fig, ax = plt.subplots(figsize=(6, 6))
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=sizes,
    explode=explode,
    colors=colors,
    startangle=90,
    counterclock=False,
    autopct='%1.0f%%',
    textprops={'fontsize': 12, 'color': 'white'},
    wedgeprops=dict(width=0.9, edgecolor='white')
)

# Set the title
ax.set_title("Research on consumers' color preference for sheer thigh-high stockings", fontsize=14, weight='bold')

# Add a legend
ax.legend(wedges, labels, loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=3, frameon=False, fontsize=10)

# Add the data source
source_text = "Data source: CBNData survey data in July 2024"
plt.figtext(0.5, -0.12, source_text, wrap=True, horizontalalignment='center', fontsize=9, color='gray')

plt.tight_layout()
plt.show()