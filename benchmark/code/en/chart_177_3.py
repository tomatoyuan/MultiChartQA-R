import matplotlib.pyplot as plt

# Support for English display
plt.rcParams['font.sans-serif'] = ['Arial']  # Use Arial font
plt.rcParams['axes.unicode_minus'] = False    # Solve the problem of minus sign display

# Data
labels = [
    "AI's capabilities are becoming \n"
    "more and more powerful\n(42%)",
    "Use AI moderately\n(23%)",
    "AI should complement \n"
    "family education\n(22%)",
    "Skeptical about AI\n(13%)"
]
sizes = [42, 23, 22, 13]
colors = ['#FF0000', '#FF6666', '#FF9999', '#CCCCCC']

# Draw a donut chart
fig, ax = plt.subplots(figsize=(10, 6))
wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, autopct='%1.0f%%', startangle=90,
    colors=colors, wedgeprops=dict(width=0.4), textprops={'fontsize': 12}
)

# Add central text
plt.text(0, 0.1, "87%", fontsize=26, fontweight='bold', ha='center')
plt.text(0, -0.1, "of parents have a \npositive attitude towards AI", fontsize=14, ha='center')

# Set to equal ratio
ax.axis('equal')
plt.title("Parents' Attitudes towards AI Education", fontsize=16)
plt.tight_layout()
plt.show()