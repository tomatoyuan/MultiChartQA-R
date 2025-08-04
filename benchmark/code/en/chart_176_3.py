import matplotlib.pyplot as plt

# Pie chart data
labels = ['18-24', '25-29', '30-34', '35-39', '40+']
sizes_uv = [25, 25, 15, 20, 15]  # Age proportion
sizes_growth = [30, 15, 45, 60, 50]  # Year-on-year growth rate (%)

# Create a figure and subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Left pie chart: Age proportion
wedges, texts, autotexts = axs[0].pie(
    sizes_uv,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90
)
axs[0].axis('equal')
axs[0].set_title('Age Proportion of Users Sending Gifts to Friends')

# Set the style of the text inside the pie chart
for text in autotexts:
    text.set_fontsize(10)

# Right bar chart: Year-on-year growth rate
bars = axs[1].bar(labels, sizes_growth, color='lightcoral')
axs[1].set_title('Year-on-Year Growth Rate of Users Sending Gifts to Friends')
axs[1].set_ylabel('Year-on-Year Growth Rate (%)')

# Add numerical labels above the bars
for bar, growth in zip(bars, sizes_growth):
    height = bar.get_height()
    axs[1].text(
        bar.get_x() + bar.get_width() / 2,
        height + 2,
        f"{growth}%",
        ha='center',
        va='bottom',
        fontsize=10
    )

plt.tight_layout()
plt.show()