import matplotlib.pyplot as plt

# Set data
months = ['Jan\'23', 'Mid\'23', 'Jan\'24']
life_cost = [57, 63, 63]
economy = [48, 42, 53]
job = [38, 57, 48]

# Create a chart
plt.figure(figsize=(10, 6))
plt.plot(months, life_cost, marker='o', label='Increasing cost of living', color='#2F66FF')
plt.plot(months, economy, marker='o', label='Economic slowdown', color='#0D1C55')
plt.plot(months, job, marker='o', label='Job instability', color='#F97316')

# Add data labels
for i, value in enumerate(life_cost):
    plt.text(months[i], value + 1, f'{value}%', ha='center', va='bottom', fontsize=10, color='#2F66FF')
for i, value in enumerate(economy):
    plt.text(months[i], value + 1, f'{value}%', ha='center', va='bottom', fontsize=10, color='#0D1C55')
for i, value in enumerate(job):
    plt.text(months[i], value + 1, f'{value}%', ha='center', va='bottom', fontsize=10, color='#F97316')

# Set the title and legend
plt.title("Reasons for consumers' deteriorating economic conditions", fontsize=14, pad=20)
plt.legend(loc='upper center', ncol=3, frameon=False, fontsize=10)

# Set axis labels and range
plt.ylim(30, 70)
plt.ylabel('Proportion (%)')

# Add data description and source
plt.figtext(0.5, -0.05, "Q: What are the reasons for the deterioration of your financial situation?\nSource: 2024 NIQ China Consumer Outlook", ha='center', fontsize=10)

# Beautify the layout
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.tight_layout()

plt.show()