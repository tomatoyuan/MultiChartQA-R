import matplotlib.pyplot as plt
import numpy as np

# Data definition
categories = ["First-tier cities", "Second-tier cities", "Third-tier cities", "Fourth-tier cities"]
percentages = [42, 20, 17, 12]  # Proportion data
growth_rates = [2, 3, -8, -7]   # Growth rate data

# Create a canvas and dual Y axes
fig, ax1 = plt.subplots(figsize=(8, 5))
ax2 = ax1.twinx()

# Draw a bar chart for proportions
x = np.arange(len(categories))
bars = ax1.bar(
    x, percentages, 
    color="blue", 
    width=0.5, 
    label="Proportion"
)
ax1.set_ylabel("Proportion (%)", fontsize=12, color="blue")
ax1.set_ylim(0, 45)
ax1.tick_params(axis="y", labelcolor="blue")

# Draw a line chart for growth rates
ax2.plot(
    x, growth_rates, 
    color="orange", 
    marker="o", 
    label="Growth rate"
)
ax2.set_ylabel("Growth rate (%)", fontsize=12, color="orange")
ax2.set_ylim(-10, 4)
ax2.tick_params(axis="y", labelcolor="orange")

# Set X-axis ticks and labels
ax1.set_xticks(x)
ax1.set_xticklabels(categories)

# Set the title
plt.title("Attention proportion and growth rate of the legal service industry by city level in May", fontsize=14, y=1.02)

# Add proportion data labels to the bar chart (only keep bar data labels)
for bar in bars:
    height = bar.get_height()
    ax1.annotate(
        f'{height}%',  # Display the percentage symbol
        xy=(bar.get_x() + bar.get_width() / 2, height),
        xytext=(0, 5),  # Offset upward by 5 points to avoid overlapping with the top of the bar
        textcoords="offset points",
        ha='center', va='bottom',
        fontsize=10,
        color='blue',  # Same color as the bar chart to enhance relevance
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="blue", alpha=0.8)  # White background box for prominent display
    )

# Adjust the legend position to the bottom of the chart
fig.legend(
    loc="lower center", 
    bbox_to_anchor=(0.5, -0.05),
    ncol=2, 
    frameon=False
)

# Optimize the layout
plt.subplots_adjust(bottom=0.2)
plt.tight_layout()

# Display the chart
plt.show()