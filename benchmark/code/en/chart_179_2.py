import matplotlib.pyplot as plt

# Chart 1: Survey on the operating time of independent websites
labels_1 = ["Less than 1 year", "1 - 3 years", "3 - 5 years", "5 - 10 years", "Over 10 years"]
values_1 = [26.6, 45.3, 22.3, 4.2, 1.6]

fig1, ax1 = plt.subplots(figsize=(8, 5))
bars1 = ax1.bar(labels_1, values_1, color='coral')
ax1.set_title("B2C Independent Website Operation Status Survey\n- Survey on the Operating Time of Independent Websites -", fontsize=14)
ax1.set_ylabel("Proportion (%)")
ax1.set_ylim(0, 50)
for bar in bars1:
    height = bar.get_height()
    ax1.annotate(f'{height:.1f}%', xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3), textcoords="offset points", ha='center')

fig1.text(0.5, -0.05, "Source: GoodsFox research data, statistical time from January to December 2023", ha='center', fontsize=10)
fig1.tight_layout()

plt.show()