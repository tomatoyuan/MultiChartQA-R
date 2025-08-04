import matplotlib.pyplot as plt

# Revenue composition categories
labels = ["Institutional and Trading", "Wealth Management", "Investment Banking", "Investment Management", "International Business", "Others"]
# Corresponding proportions (%)
sizes = [41.31, 26.99, 9.73, 13.14, 5.99, 2.84]
# Corresponding colors (try to match the original image, can be fine - tuned)
colors = ['#E4725F', '#F6C85F', '#81C784', '#94572E', '#C08B30', '#4F4F4F']

fig, ax = plt.subplots(figsize=(6, 6))
# Draw a pie chart, autopct controls the numerical display format, startangle sets the starting angle
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct='%1.2f%%', startangle=90)

# Adjust the annotation text color to white to make the values clearer on the colored blocks
for autotext in autotexts:
    autotext.set_color('white')

ax.set_title('Revenue Composition of Guotai Junan in 2023')

plt.tight_layout()
plt.show()