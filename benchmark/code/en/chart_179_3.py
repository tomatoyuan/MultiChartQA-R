# Chart 2: Year-on-year growth of independent station sales in 2022
labels_2 = ["Over 100%", "80% - 100%", "50% - 80%", "20% - 50%", "0% - 20%", "Negative growth"]
values_2 = [2.3, 3.5, 8.0, 14.6, 40.5, 35.1]

fig2, ax2 = plt.subplots(figsize=(8, 5))
bars2 = ax2.bar(labels_2, values_2, color='coral')
ax2.set_title("B2C Independent Station Operation Status Survey\n- Year-on-year growth of independent station sales in 2022 -", fontsize=14)
ax2.set_ylabel("Proportion (%)")
ax2.set_ylim(0, 50)
for bar in bars2:
    height = bar.get_height()
    ax2.annotate(f'{height:.1f}%', xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3), textcoords="offset points", ha='center')

fig2.text(0.5, -0.05, "Source: GoodsFox research data, statistical time from January to December 2023", ha='center', fontsize=10)
fig2.tight_layout()

plt.show()