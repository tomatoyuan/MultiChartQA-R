import matplotlib.pyplot as plt

# Age share data (estimated)
age_labels = ['18-24', '25-29', '30-34', '35-39', '40+']
age_shares = [25, 25, 20, 15, 15]

# Year-on-year growth rate data (estimated)
growth_rates = [80, 10, 50, 85, 70]  # Estimated bar height representing the growth rate

# Set the chart style
colors = ['#FF4C88', '#FFA6C1', '#FDBACD', '#FECEDC', '#FEE5EA']

# Create side-by-side plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Draw a pie chart
ax1.pie(age_shares, labels=age_labels, autopct='%1.1f%%', startangle=90, colors=colors)
ax1.set_title("Age Proportion of People Giving Gifts to Their Lovers in 2023")
ax1.axis('equal')

# Draw a bar chart
bars = ax2.bar(age_labels, growth_rates, color=colors)
ax2.set_title("Year-on-Year Growth Rate")
ax2.set_ylabel("Growth Rate Index")
ax2.set_ylim(0, 100)

# Add numerical labels
for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2, height + 2, f'{height}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()