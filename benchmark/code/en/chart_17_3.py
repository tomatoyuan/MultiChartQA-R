import matplotlib.pyplot as plt
import numpy as np

# List of common telecom fraud methods
fraud_methods = [
    "Guess who I am", "Impersonate public security, procuratorate and law court\n'Assist in investigation'",
    "Impersonate\nTelecom/Post Office", "Consumption tax refund",
    "Pretend to be an acquaintance\nand defraud", "Fake\nwinning text message",
    "'Ring once'\nand trick to call back", "Mass - send\nbank card number/name"
]
values = np.array([15, 30, 10, 5, 20, 8, 7, 5])  # Use more realistic data ratios
total = sum(values)

# Create a canvas
fig, ax = plt.subplots(figsize=(10, 8), facecolor='#f8f9fa')
fig.patch.set_alpha(0.9)  # Set the transparency of the canvas

# Define the explosion effect to highlight the largest part
explode = [0.05 if v == max(values) else 0 for v in values]

# Custom color scheme (use brighter color matching)
colors = [
    '#ff6b6b', '#4ecdc4', '#ffd166', '#06d6a0',
    '#118ab2', '#ef476f', '#9381ff', '#ff9f1c'
]

# Draw a pie chart
wedges, texts, autotexts = ax.pie(
    values,
    explode=explode,
    labels=None,  # Do not display labels temporarily, show them through the legend
    autopct=lambda p: f'{p:.1f}%\n({int(p*total/100)})',  # Display both the percentage and the actual quantity
    startangle=140,
    colors=colors,
    wedgeprops=dict(width=0.7, edgecolor='w', linewidth=1),  # Ring - shaped pie chart effect
    pctdistance=0.85,  # Position of the percentage label
    textprops={'fontsize': 10, 'weight': 'bold', 'color': 'w'}
)

# Add a title and subtitle
ax.set_title("Distribution of common telecom fraud methods", fontsize=18, fontweight="bold", pad=20)

# Add a legend
legend = ax.legend(
    wedges, fraud_methods,
    title="Fraud methods",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1),
    fontsize=11,
    title_fontsize=13
)
legend.get_frame().set_alpha(0.8)  # Make the legend background semi - transparent

# Beautify the layout
plt.tight_layout(pad=4)  # Increase the margin
plt.subplots_adjust(right=0.75)  # Make space for the legend

# Display the chart
plt.show()