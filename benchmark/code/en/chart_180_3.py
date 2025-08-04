import matplotlib.pyplot as plt

# Efficacy categories and their proportions
labels = ['Enhance immunity', 'Anti - fatigue', 'Protect liver', 'Protect eyes', 'Aid sleep', 'Others']
sizes = [42, 15, 13, 8, 2, 20]
colors = ['#0057FF', '#7DECF6', '#00B388', '#93B6FF', '#CED6F8', '#EDEDED']

# Draw a pie chart
fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, colors=colors, autopct='%1.0f%%',
    startangle=90, textprops={'fontsize': 10}, pctdistance=0.8
)

# Set the title
ax.set_title("Distribution of registered efficacy of new health food products in H1 2023", fontsize=14, fontweight='bold')

# Add data source description
plt.figtext(
    0.5, -0.01,
    'Note: Anti - fatigue corresponds to the "Relieve physical fatigue" function in health foods. Protect liver corresponds to the "Assist in protecting against chemical liver damage" function. Protect eyes corresponds to the "Relieve visual fatigue" function.\nData source: State Administration for Market Regulation, compiled from public information',
    wrap=True, horizontalalignment='center', fontsize=9
)

plt.tight_layout()
plt.show()