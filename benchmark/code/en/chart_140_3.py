import matplotlib.pyplot as plt
import numpy as np

# Expected mileage data
mileage_labels = ["150 - 250 km", "250 - 350 km", "350 - 500 km", "Over 500 km"]
mileage_sizes = [7.1, 41.2, 29.5, 22.2]
mileage_colors = ["#87CEFA", "#C0C0C0", "#4169E1", "#1E3A78"]

# Expected safety performance data
safety_labels = ["Powertrain protection measures", "Tire safety", "Airbags", "Automatic parking system"]
safety_sizes = [65.7, 59.7, 58.8, 56.5]
safety_colors = ["#87CEFA", "#6495ED", "#4682B4", "#1E3A78"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Draw the pie chart for expected mileage
wedges, texts, autotexts = ax1.pie(mileage_sizes, colors=mileage_colors, autopct='%1.1f%%', startangle=90)
ax1.set_title('2023 Expectations of Chinese consumers for new - energy vehicle mileage')
ax1.legend(wedges, mileage_labels, title="Mileage range", loc="center left", bbox_to_anchor=(1, 0.5))
# Adjust the color of annotation text
for autotext in autotexts:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

# Draw the bar chart for expected safety performance (simulated as there is single - proportion data)
x = np.arange(len(safety_labels))
ax2.bar(x, safety_sizes, color=safety_colors, width=0.5)
ax2.set_title('2023 Expectations of Chinese consumers for new - energy vehicle safety performance')
ax2.set_ylabel('Expected proportion (%)')
ax2.set_xticks(x)
ax2.set_xticklabels(safety_labels, rotation=15, ha='right')
# Add numerical annotations for safety performance
for i, size in enumerate(safety_sizes):
    ax2.text(i, size + 1, f'{size}%', ha='center', va='bottom')
ax2.legend(safety_labels, title="Safety performance items", loc="center right")

plt.suptitle('2023 Survey on Chinese consumers\' expectations for new - energy vehicles', fontsize=14)
plt.tight_layout()
plt.show()