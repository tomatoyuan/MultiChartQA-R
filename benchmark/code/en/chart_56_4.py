import matplotlib.pyplot as plt
import numpy as np

# Data
factors = ["Product Quality", "Product Price", "Brand", "Platform Image", "Anchor's Credit"]
percentages = [76.9, 64.1, 59.3, 42.5, 39.3]
colors = ["#a5d6a7"]  # Uniform green color, can be adjusted as needed

# Create a canvas
fig, ax = plt.subplots(figsize=(6, 4))

# Draw a horizontal bar chart
bars = ax.barh(factors, percentages, color=colors*len(factors))

# Add data labels
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height()/2,
            f'{width}%', ha='left', va='center', fontsize=9, fontweight='bold')

# Beautify the settings
ax.set_title("Factors Influencing Consumers' Purchase Decisions in Live - Streaming E - commerce", fontsize=12, fontweight='bold')
ax.set_xlabel("Factors Influencing Purchase Decisions (%)", fontsize=10)
ax.set_xticks(np.arange(0, max(percentages)+10, 10))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(["Factors Influencing Purchase Decisions (%)"], loc='lower right')

plt.tight_layout()
plt.show()