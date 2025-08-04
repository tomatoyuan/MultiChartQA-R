import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2016, 2021)
# Simulated search heat (only for reproducing the trend, not real data, can be replaced)
search_heat = [10, 30, 50, 70, 100]

# Plotting
plt.figure(figsize=(6, 4))
# Gradient-colored bar chart (simple simulation, more refined customization can be done with colormap)
bars = plt.bar(years, search_heat, color=plt.cm.get_cmap('Purples')(np.linspace(0.3, 0.9, len(years))))

# Data annotation
for bar, heat in zip(bars, search_heat):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 2,
             f'{heat}', ha='center', va='bottom', fontsize=10)

# Title and labels
plt.title('In 2020, the search for teacher qualification certificates skyrocketed! Becoming a teacher is more appealing!', fontsize=12)
plt.xlabel('Year')
plt.ylabel('Search Heat (Simulated)')

# Optimize display
plt.xticks(years)
# Hide the top and right borders
for spine in ['top', 'right']:
    plt.gca().spines[spine].set_visible(False)

plt.show()