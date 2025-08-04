import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# List of countries
countries = ["China", "India", "Japan", "USA", "Brazil", "Turkey", "Thailand", "Indonesia"]
# Market size data
market_size = [6, 1, 1, 1, 1, 0.5, 0.5, 0.5]

# Generate an array of indices for the countries
x = np.arange(len(countries))
# Create a bar plot with different color palettes
sns.barplot(x=countries, y=market_size, palette=['orange'] + ['green']*(len(countries)-1))

# Add value labels on the bars
for i, v in enumerate(market_size):
    plt.text(i, v + 0.05, f'{v}', ha='center', fontsize=12)

# Add special text on the first bar
plt.text(0, market_size[0], "More than six times", ha='center', va='bottom', fontsize=14, color='orange')
# Set the title of the plot
plt.title("Estimated Market Size of Major Tea Countries in 2022", fontsize=14, fontweight='bold')
# Add text at the bottom of the figure
plt.figtext(0.5, 0.01, "Unit: Billion US dollars", ha='center', fontsize=12)
# Remove the y - axis tick labels
plt.yticks([])
# Adjust the layout to prevent text from being obscured
plt.tight_layout()
# Display the plot
plt.show()