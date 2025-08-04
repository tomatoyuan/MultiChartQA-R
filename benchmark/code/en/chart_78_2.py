import matplotlib.pyplot as plt
import numpy as np

# Region names
regions = ["Oceania", "Europe", "Eastern Asia", "Latin America and the Caribbean", "Sub - Saharan Africa"]
# High school enrollment rate (%)
high_school_enrollment = [95.0, 93.6, 86.4, 78.7, 41.9]
# Vocational education participation rate (%)
vocational_education = [17.5, 18.1, 7.2, 6.9, 1.3]
# GDP per capita (USD)
gdp_per_capita = [49999.0, 34148.9, 13463.6, 7244.7, 1501.2]

# Create a figure and subplot
fig, ax = plt.subplots(figsize=(10, 6))

ax.set_ylim(0, 120)

# Draw a grouped bar chart
x = np.arange(len(regions))
bar_width = 0.35
# High school enrollment rate (green)
high_school_bars = ax.bar(x - bar_width/2, high_school_enrollment, width=bar_width, color="#A4C639", label="High school enrollment rate in each region (%)")
# Vocational education participation rate (blue)
vocational_bars = ax.bar(x + bar_width/2, vocational_education, width=bar_width, color="#64B5F6", label="Vocational education participation rate of 15 - 24 years old in each region (%)")

# Add data labels for high school enrollment rate
for bar in high_school_bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Adjust the annotation position
                textcoords="offset points",
                ha='center', va='bottom')

# Add data labels for vocational education participation rate
for bar in vocational_bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Adjust the annotation position
                textcoords="offset points",
                ha='center', va='bottom')

# Set x - axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(regions)
# Set y - axis label
ax.set_ylabel("Percentage (%)")
# Set the title
ax.set_title("Vocational education participation rate and high school enrollment rate in each region in 2020", fontsize=14, fontweight="bold")

# Add a legend
ax.legend()

# Beautify the chart, hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()