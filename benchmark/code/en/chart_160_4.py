import matplotlib.pyplot as plt

# Data
labels = ['E-commerce', 'Digital Appliances', 'Mobile Games', 'Automobiles', 'Beauty']
sizes = [45, 13.75, 13.75, 13.75, 13.75]  # The sum is 100
colors = ['#b3cfff', '#c2d6ff', '#d1ddff', '#e0e5ff', '#eff2ff']  # Lighter blue gradient

# Plotting
fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors,
    textprops={'color': 'black', 'fontsize': 10}
)

# Add title
plt.title('Top 5 Cooperation Industries of Bilibili Mid - Tier Influencers in the Past 180 Days', fontsize=14)

# Add explanatory text
plt.text(0, -1.3, "The average number of cooperation industries of Bilibili\n mid - tier influencers in the past 180 days is 2.77", ha='center', fontsize=12, color='#4a64c0')

# Keep the pie chart circular
ax.axis('equal')

plt.tight_layout()
plt.show()