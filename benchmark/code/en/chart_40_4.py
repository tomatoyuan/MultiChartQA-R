import matplotlib.pyplot as plt

# Data
channels = ['Online', 'Both Online and Offline', 'Offline']
percentages = [89, 68, 74]

# Create a canvas
plt.figure(figsize=(10, 6))

# Draw a bar chart
bars = plt.bar(channels, percentages, color=['#ff9999', '#66b3ff', '#99ff99'], alpha=0.8)

# Add data labels
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height}%',
             ha='center', va='bottom', fontsize=12)

# Set title and labels
plt.title('Percentage of Consumers Including Channels in Purchase Decisions', fontsize=15)
plt.xlabel('Channel Type', fontsize=12)
plt.ylabel('Percentage (%)', fontsize=12)

# Set y-axis range
plt.ylim(0, 100)

# Add grid lines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Optimize layout
plt.tight_layout()

# Show the plot
plt.show()