import matplotlib.pyplot as plt
import numpy as np

# Province names
provinces = ["Guangdong", "Shandong", "Jiangsu", "Henan", "Zhejiang", "Beijing", "Hubei", "Hebei", "Hunan", "Sichuan"]
# Simulated search index data (can be replaced with real data), the length of the values is consistent with the number of provinces
search_index = [18, 17, 16, 15, 14, 13, 12, 11, 10, 9]  

y_pos = np.arange(len(provinces))

fig, ax = plt.subplots()
# Draw a horizontal bar chart, height controls the height of the bar (here simulated by the search index), width controls the width of the bar, align adjusts the alignment
ax.barh(y_pos, search_index, height=0.6, align='center', color='orange')  
ax.set_yticks(y_pos)
ax.set_yticklabels(provinces)
# Make the bar chart display from left to right (by default, the horizontal bar chart is from bottom to top, after inverting, it fits the visual of the original chart better)
ax.invert_yaxis()  
ax.set_xlabel('Search Index Schematic')
ax.set_title('Search Index Overview')

# You can add numerical labels to display the values at the end of each bar
for i, v in enumerate(search_index):
    ax.text(v + 0.1, i, str(v), va='center')

plt.show()