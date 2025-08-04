# Figure 2: Lifecycle (months) of stores in different formats in 2024
labels = ['T1', 'T2', 'T3+']
x = np.arange(len(labels))
width = 0.2

# Data for: Dining, Retail, Leisure and Entertainment
dining_nonchain = [20.7, 22.3, 25.3]
dining_chain = [24.1, 25.0, 25.4]
retail_nonchain = [38.2, 41.2, 43.9]
retail_chain = [38.0, 40.5, 43.3]
leisure_nonchain = [29.4, 33.7, 34.2]
leisure_chain = [32.7, 34.5, 35.9]

fig2, ax2 = plt.subplots(figsize=(12, 6))
ax2.bar(x - 0.3, dining_nonchain, width, label='Dining - Non - chain', color='#B3DE69')
ax2.bar(x - 0.1, dining_chain, width, label='Dining - Chain', color='#FCCDE5')
ax2.bar(x + 0.1, retail_nonchain, width, label='Retail - Non - chain', color='#8DD3C7')
ax2.bar(x + 0.3, retail_chain, width, label='Retail - Chain', color='#D9D9D9')

for i in range(len(x)):
    ax2.text(x[i] - 0.3, dining_nonchain[i] + 0.5, str(dining_nonchain[i]), ha='center', fontsize=9)
    ax2.text(x[i] - 0.1, dining_chain[i] + 0.5, str(dining_chain[i]), ha='center', fontsize=9)
    ax2.text(x[i] + 0.1, retail_nonchain[i] + 0.5, str(retail_nonchain[i]), ha='center', fontsize=9)
    ax2.text(x[i] + 0.3, retail_chain[i] + 0.5, str(retail_chain[i]), ha='center', fontsize=9)

ax2.set_xticks(x)
ax2.set_xticklabels(labels)
ax2.set_title('Lifecycle (months) of stores in different formats in 2024 - Dining and Retail', fontsize=14)
ax2.set_ylabel('Lifecycle (months)')
ax2.legend()

plt.tight_layout()
plt.show()