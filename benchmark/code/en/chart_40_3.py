import matplotlib.pyplot as plt
import pandas as pd

# Build data
data = {
    'Channel': ['Online (Online Shopping Platform)', 'Online (Douyin Live)', 'Offline (Supermarket)', 'Offline (Convenience Store)', 'Offline (Pinduoduo)', 'Offline (Canteen)'],
    'Proportion': [89, 68, 74, 64, 57, 40]
}
df = pd.DataFrame(data)

# Create a canvas
plt.figure(figsize=(12, 6))

# Draw a bar chart
colors = ['#4285F4', '#4285F4', '#EA4335', '#EA4335', '#EA4335', '#EA4335']  # 区分线上(蓝色)和线下(红色)
bars = plt.bar(df['Channel'], df['Proportion'], color=colors, alpha=0.8)

# Add data labels
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height}',
             ha='center', va='bottom', fontsize=10)

# Set title and labels
plt.title('Channel Proportion Distribution', fontsize=15)
plt.xlabel('Channel Type', fontsize=12)
plt.ylabel('Proportion', fontsize=12)

# Set y-axis range
plt.ylim(0, 100)

# Rotate x-axis labels for better display
plt.xticks(rotation=45, ha='right')

# Add grid lines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add legend
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='#4285F4', label='Online'),
                   Patch(facecolor='#EA4335', label='Offline')]
plt.legend(handles=legend_elements, loc='upper right')

# Optimize layout
plt.tight_layout()

# Show the plot
plt.show()