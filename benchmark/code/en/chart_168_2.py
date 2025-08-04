import matplotlib.pyplot as plt

# Data
labels = ['Very familiar', 'Fairly familiar', 'Moderately familiar', 'Not familiar']
sizes = [35, 50, 10, 5]
colors = ['#955c23', '#d8b77f', '#f3e7d3', '#f5f3ef']

# Plotting
fig, ax = plt.subplots(figsize=(10, 10))
wedges, texts = ax.pie(
    sizes, labels=labels, startangle=90, counterclock=False,
    wedgeprops=dict(width=0.4, edgecolor='w'), colors=colors
)

# Add title
plt.title('Consumers\' awareness of virgin wood pulp', fontsize=14)

# Add text explanations
plt.text(-1.6, -1.0, '50%', fontsize=24, color='#d8b77f', weight='bold')
plt.text(-2.1, -1.3, 'of consumers are fairly familiar with the concept of virgin wood pulp,\nknow its characteristics and are willing to buy products made from it.', color='#d8b77f',  fontsize=12)

plt.text(1.1, -0.2, '35%', fontsize=24, color='#955c23', weight='bold')
plt.text(1.0, -0.7, 'of consumers are very familiar \n'
                    'with the concept of virgin wood pulp\n'
                    'and say they will give priority to \n'
                    'tissues made from this raw material\n when shopping.',  color='#955c23', fontsize=12)

# Add data source
plt.text(-2.2, -1.8,
         'Data source: CBNData\'s survey on the trends of '
         'Chinese consumers\' household paper products in March 2024.\n'
         'Data description: Which of the following statements is closest '
         'to your awareness of virgin wood pulp '
         '(wood pulp made from natural wood without adding other fibers)?\n'
         ' N = 1000',
         fontsize=8, color='gray')

plt.tight_layout()
plt.show()