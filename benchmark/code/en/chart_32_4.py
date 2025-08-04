import matplotlib.pyplot as plt

# Data (hypothetical search volume values, can be replaced with actual data)
cities = ['Beijing', 'Shanghai', 'Chengdu']
search_volumes = [2200000, 950000, 780000]  # Hypothetical search volume values

# Create a bar chart
plt.figure(figsize=(10, 6))  # Set the chart size
bars = plt.bar(cities, search_volumes, color=['#b378d8', '#4b79e2', '#4b79e2'])

# Add title and labels
plt.title('Comparison of Teacher Qualification Certificate Search Volumes in Cities', fontsize=16, fontweight='bold')
plt.xlabel('Cities', fontsize=14)
plt.ylabel('Search Volume (times)', fontsize=14)

# Add numerical labels
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 10000,
             f'{height:,}', ha='center', va='bottom', fontsize=12)

# Set the y-axis tick format to be more readable
plt.ticklabel_format(axis='y', style='plain')

# Display grid lines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the chart
plt.tight_layout()  # Ensure labels and titles are fully displayed
plt.show()