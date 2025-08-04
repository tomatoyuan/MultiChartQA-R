# Chart 1.2 - 10: Other skin problems caused by large pores

labels = [
    "Oily skin", "Excessive blackheads \nand clogged pores", "Dull complexion",
    "Roughness", "Acne breakouts", "Redness"
]
values = [77.33, 74.33, 61.33, 55.33, 45.00, 34.33]

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(labels[::-1], values[::-1], color=['#245b5b'] * 3 + ['#b4d4d4'] * 3)

# Add percentage labels
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height()/2, f'{width:.2f}%', va='center', fontsize=10)

ax.set_xlabel('Proportion (%)')
ax.set_title("Figure 1.2 - 10 Other skin problems caused by large pores")
fig.text(0.9, 0.02, "N = 300", ha='right', fontsize=10)

plt.tight_layout()
plt.show()