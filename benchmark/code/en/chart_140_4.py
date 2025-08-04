import matplotlib.pyplot as plt

# Data
labels = ["Battery Electric Vehicles (On - board Motors)", "Hybrid Electric Vehicles (Hybrid Oil - Electric New Energy)", "Hydrogen Fuel Cell Electric Vehicles", 
          "Fuel Cell Vehicles (Power Generation through Chemical Reactions)", "Gas Vehicles (Natural Gas)", "Alternative Fuel Vehicles (e.g., Ethanol)"]
sizes = [61.3, 22.0, 8.4, 4.7, 2.9, 0.7]
colors = ["#FAD6A5", "#F9CB9C", "#F7B787", "#F4A460", "#E9967A", "#CD5C5C"]

fig, ax = plt.subplots(figsize=(10, 7))

# Draw a pie chart
wedges, texts, autotexts = ax.pie(sizes, colors=colors, autopct='%1.1f%%', startangle=90)

ax.set_title('Types of New - Energy Vehicles Considered Most Promising for Development by Chinese Consumers in 2023')
ax.legend(wedges, labels, title="Vehicle Types", loc="center left", bbox_to_anchor=(1, 0.5))

# Adjust the color of the annotation text to ensure it is clearly visible on dark/light slices
for autotext in autotexts:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

plt.tight_layout()
plt.show()