import matplotlib.pyplot as plt

# Data
labels = ['Medical and Healthcare', 'Information Technology', 'Advanced Manufacturing', 'Automobile and Transportation', 'New Consumption', 'Culture and Entertainment', 'Fintech']
sizes = [29.5, 25.1, 13.9, 11.7, 10.0, 9.6, 0.2]

# Plotting
fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    textprops={'fontsize': 10}
)
ax.axis('equal')

# Add title and data source
plt.title('Industry Distribution of Overall Overseas - Going Enterprises', fontsize=15, loc='center', pad=20)
plt.figtext(0.01, 0, 'Data Source: Bailian Intelligence, Compiled by 36Kr Research Institute',
            fontsize=10, ha='left')
plt.tight_layout()
plt.show()