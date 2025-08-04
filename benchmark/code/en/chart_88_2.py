import matplotlib.pyplot as plt
import numpy as np

# Years
years = [2007, 2013, 2017, 2020]
diabetes_rates = [9.7, 10.4, 11.2, 11.9]
cholesterol_rates = [3.1, 6.0, 8.0, 8.2]

# Color settings
diabetes_color = "#6ab04c"      # Mild olive green
cholesterol_color = "#45aaf2"   # Light bright blue

# Create a canvas
fig, ax = plt.subplots(figsize=(8, 5))

# Draw the area chart
ax.fill_between(
    years, diabetes_rates, 
    color=diabetes_color, alpha=0.3, label="Prevalence of diabetes among adults (%)"
)
ax.plot(years, diabetes_rates, color=diabetes_color, linewidth=2.5, marker="o")

ax.fill_between(
    years, cholesterol_rates, 
    color=cholesterol_color, alpha=0.3, label="Prevalence of hypercholesterolemia among adults (%)"
)
ax.plot(years, cholesterol_rates, color=cholesterol_color, linewidth=2.5, marker="o")

# Add data labels
for x, y in zip(years, diabetes_rates):
    ax.text(x, y - 0.8, f"{y}%", ha='center', va='bottom', fontsize=10, color=diabetes_color)

for x, y in zip(years, cholesterol_rates):
    ax.text(x, y - 0.8, f"{y}%", ha='center', va='top', fontsize=10, color=cholesterol_color)

# Set the axes
ax.set_xticks(years)
ax.set_ylabel("Prevalence (%)")
ax.set_title("Prevalence of diabetes and hypercholesterolemia among Chinese adults from 2007 to 2020", fontsize=14, fontweight='bold')

# Legend
ax.legend(loc="upper left", fontsize=10)

# Beautify
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
ax.grid(alpha=0.2)

plt.tight_layout()
plt.show()