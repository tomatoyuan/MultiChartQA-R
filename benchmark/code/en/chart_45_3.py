import matplotlib.pyplot as plt
import numpy as np

# Decision factors
labels = ['Function - related parameters', 'Appearance design/Fashion degree', 'User reviews/Word - of - mouth', 'Price/Promotion activities', 
          'Brand awareness', 'After - sales service', 'Celebrity/KOL endorsement', 'Limited/Co - branded editions']
# Corresponding proportion data for each factor
values = [89, 61, 45, 35, 27, 19, 5, 3]

# Set the x - coordinate positions for the bar chart
x = np.arange(len(labels))  
# Draw the bar chart and set the bar width, etc.
fig, ax = plt.subplots()
rects = ax.bar(x, values, width=0.5, color=['pink', 'pink', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray'])

# Set the axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha='right')  # Rotate the labels to avoid overlap
ax.set_ylabel('Proportion (%)')
ax.set_title('Decision factors when consumers buy functional clothing')

# Annotate the values on the bars
for rect in rects:
    height = rect.get_height()
    ax.annotate('{}%'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # Vertical distance of the value from the top of the bar
                textcoords="offset points",
                ha='center', va='bottom')

plt.tight_layout()  # Automatically adjust the layout to avoid incomplete display of labels, etc.
plt.show()