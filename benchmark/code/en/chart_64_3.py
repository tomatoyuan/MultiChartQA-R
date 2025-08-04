import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Set the font
plt.rcParams['font.sans-serif'] = ['Arial']
plt.rcParams['axes.unicode_minus'] = False

# Data definition
factors = [
    {"name": "Improve user conversion and boost performance", "percent": 50.4},
    {"name": "Cost of private domain construction and operation", "percent": 48.8},
    {"name": "Effectively achieve public domain drainage", "percent": 46.3},
    {"name": "Enhance user stickiness to the brand", "percent": 43.9},
    {"name": "Diverse operation methods", "percent": 39.8},
    {"name": "Convenient private domain reach", "percent": 37.4},
    {"name": "Integration of online and offline channels", "percent": 29.3},
    {"name": "Private domain data can be precipitated and analyzed", "percent": 27.6},
]

# Prepare heatmap data
factor_names = [f["name"] for f in factors][::-1]  # Reverse the y-axis direction
percent_values = np.array([f["percent"] for f in factors])[::-1].reshape(-1, 1)

# Create a canvas
fig, ax = plt.subplots(figsize=(6, 7))

# Use a custom warm - toned color map
cmap = sns.light_palette("orangered", as_cmap=True)

# Draw a heatmap
sns.heatmap(
    percent_values,
    annot=True,
    fmt=".1f",
    cmap=cmap,
    cbar=False,
    yticklabels=factor_names,
    xticklabels=["Attention (%)"],
    linewidths=0.5,
    linecolor="white",
    annot_kws={"fontsize": 10, "weight": "bold", "color": "#4B1E00"},
    ax=ax
)

# Set the title
ax.set_title("Factors of concern for brand/merchant private domain layout and operation in 2022", fontsize=14, fontweight="bold", pad=20)

# Beautify the axes
ax.tick_params(axis='y', labelsize=10)
ax.tick_params(axis='x', labelsize=10)
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()