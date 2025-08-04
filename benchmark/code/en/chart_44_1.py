import matplotlib.pyplot as plt

# Data
labels = [
    "There are very few lunch options. I've eaten \nthe same few places so many times that I'm tired of them.",
    "I'm worried about the health issues of takeout, \nbut there are no other options besides takeout.",
    "Due to busy work, I often don't have time \nto eat lunch or can't eat lunch on time.",
    "I want to eat healthy and delicious food, \nbut there are no purchase channels or the prices are expensive."
]
sizes = [53, 44, 41, 40]
colors = ['#7ccf7c', '#7ccf7c', '#7ccf7c', '#7ccf7c']  # Green series

# Create canvas
plt.figure(figsize=(12, 8))

# Draw horizontal bar chart
bars = plt.barh(labels, sizes, color=colors, alpha=0.8)

# Add data labels
for bar in bars:
    width = bar.get_width()
    plt.text(width + 1, bar.get_y() + bar.get_height()/2,
             f'{width}%',
             ha='left', va='center', fontsize=12)

# Set title and labels
plt.title("Short on time, limited options. Hard to ensure 'healthy intake' even with effort.", fontsize=14, fontweight='bold')
plt.xlabel('Percentage (%)', fontsize=12)
plt.ylabel('Problem Type', fontsize=12)

# Set x-axis range
plt.xlim(0, 60)

# Add grid lines
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Optimize layout
plt.tight_layout()

# Show plot
plt.show()