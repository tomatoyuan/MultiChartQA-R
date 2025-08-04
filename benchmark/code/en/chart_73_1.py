import matplotlib.pyplot as plt

# Data
labels = ["$10 - $20", "$21 - $30", "$31 - $40", "$41 or above"]
data = [18.4, 50.3, 26.5, 4.8]
colors = ['#FFA07A', '#FF4500', '#FF8C00', '#FFD700']  # Warm color tones

# Draw a donut chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    data,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    wedgeprops=dict(width=0.4, edgecolor='white')  # Control the width to form a donut shape
)

# Set the title
ax.set_title("Single - payment fees of users' commonly used instant delivery platforms", fontsize=14, fontweight="bold")

plt.tight_layout()
plt.show()