import matplotlib.pyplot as plt

# Data
labels = ['Price discount', 'Hotel points', 'Others']
sizes = [58.7, 36.9, 4]
colors = ['#009C8A', '#A1D4A2', '#F3ECD9']

# Plotting
plt.figure(figsize=(8, 6))
plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    textprops={'fontsize': 14}
)

plt.title('Incentive measures expected by consumers', fontsize=16)
plt.axis('equal')  # Make the pie chart a perfect circle
plt.tight_layout()
plt.show()