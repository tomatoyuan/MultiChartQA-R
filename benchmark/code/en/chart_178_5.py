import matplotlib.pyplot as plt

# Set data
labels = ['Consumption upgrade: \n'
          'More willing to spend a large amount\n'
          ' on New Year gifts',
          'Consumption level remains the same:\n'
          ' Not exceeding usual consumption level',
          'Consumption downgrade:\n'
          ' Gifts are non - essential expenses, \n'
          'save as much as possible']
sizes = [42, 49, 8]
colors = ['#a32020', '#f25e41', '#ffa768']

# Draw a donut chart
fig, ax = plt.subplots(figsize=(10, 6))
wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, autopct='%1.0f%%', startangle=90, colors=colors,
    wedgeprops={'width': 0.4}, textprops={'fontsize': 10}
)

# Add center text
plt.text(0, 0, "New Year Gift - Giving\nConsumption Attitude", ha='center', va='center', fontsize=14, fontweight='bold')

# Add data source and description
plt.figtext(0.5, 0.01,
            "Data source: CBNData questionnaire survey in January 2024  \nData description: Compared with your usual consumption, "
            "which of the following options best describes your consumption change when purchasing New Year gifts? N = 1500",
            wrap=True, horizontalalignment='center', fontsize=9)

# Set the title
plt.title("Distribution of public consumption attitudes towards\n New Year gift - giving compared to daily life", fontsize=13, fontweight='bold')
plt.tight_layout()
plt.show()