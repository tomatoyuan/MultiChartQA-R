import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Tea products']
mat2023 = [100]  # Hypothetical MAT2023 data, can be replaced with real values
mat2024 = [118]  # Hypothetical MAT2024 data based on +18%, can be replaced with real values
growth_rate = 18  # Growth rate

x = np.arange(len(categories))  # Bar chart x-axis positions
width = 0.35  # Bar chart width

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, mat2023, width, label='MAT2023', color='lightgreen')
rects2 = ax.bar(x + width/2, mat2024, width, label='MAT2024', color='green')

# Add growth rate arrow and text
arrow_x = x[0]
arrow_y = max(mat2023 + mat2024) * 0.6  # Arrow position, can be adjusted
ax.annotate(f'+{growth_rate}%', xy=(arrow_x, mat2023[0]), xytext=(arrow_x, arrow_y),
            arrowprops=dict(facecolor='orange', shrink=0.05),
            ha='center', va='bottom', fontsize=14, color='orange')

# Add value labels function
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

# Add value labels to both bars
add_labels(rects1)
add_labels(rects2)

# Set axis labels, etc.
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()

plt.title('Online Taobao and Tmall Tea Product Consumption Market Size from MAT2023 to MAT2024')
plt.show()