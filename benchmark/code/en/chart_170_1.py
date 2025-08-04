import matplotlib.pyplot as plt

# Data
labels = ['Mild', 'Moderate', 'Moderately Severe', 'Severe', 'None']
sizes = [29.3, 25.3, 17.7, 11.9, 15.8]
colors = ['#65D1DD', '#6449A6', '#FF7B9C', '#FFA01B', '#F5C447']
explode = (0.05, 0.05, 0.05, 0.05, 0.05)  # Make each part slightly prominent

# Plotting
fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, autopct='%1.1f%%',
    startangle=90, counterclock=False, colors=colors,
    explode=explode, textprops={'fontsize': 12}, wedgeprops={'width': 0.3}
)

ax.set_title('Depression Assessment of Psychological Evaluation Users', fontsize=16, pad=20)
ax.axis('equal')  # Keep the pie chart circular
plt.tight_layout()
plt.show()