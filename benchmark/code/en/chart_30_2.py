import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Data
labels = ['19 - 24 years old', '25 - 34 years old', '18 years old and below', '35 - 49 years old', '50 years old']
sizes = [41, 33, 15, 10, 1]
# Custom colors, using a more professional color - matching scheme
colors = ['#3498db', '#2ecc71', '#f39c12', '#e74c3c', '#9b59b6']
# Highlight the largest sector
explode = (0.1, 0, 0, 0, 0)  

# Create a canvas and a sub - plot
fig, ax = plt.subplots(figsize=(10, 7))

# Draw a pie chart, add shadow and custom percentage style
wedges, texts, autotexts = ax.pie(
    sizes, 
    explode=explode,
    labels=labels,
    colors=colors,
    autopct=lambda p: f'{p:.1f}%\n({int(p*sum(sizes)/100)})',  # Display both percentage and actual number of people
    shadow=True,
    startangle=90,
    textprops={'fontsize': 12}
)

# Set the title
ax.set_title('The portrait of AIDS - related population tends to be young', fontsize=16, pad=20)

# Make the pie chart a perfect circle
ax.axis('equal')  

# Add a legend
plt.legend(wedges, labels, title="Age groups", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Add a note
plt.figtext(0.5, 0.01, f"Total data: {sum(sizes)} people", ha="center", fontsize=12)

# Adjust the layout
plt.tight_layout()

# Display the graph
plt.show()