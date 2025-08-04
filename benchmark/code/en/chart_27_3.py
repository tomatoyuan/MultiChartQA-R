import matplotlib.pyplot as plt
import numpy as np

# TV drama names
labels = ["State Prosecution", "Absolute Power", "I Am the Master of the Ups and Downs", "State Cadre"]
# Search index data
values = [526.24, 183.28, 128.79, 111.05]
# Used to position each thermometer on the x - axis
x_positions = np.arange(len(labels))  

# Create a canvas and subplots
fig, axes = plt.subplots(1, len(labels), figsize=(12, 5), sharey=True)

# The maximum scale of the thermometer (can be adjusted according to the data, set to 600 here for easy display)
max_temp = 600  
for i in range(len(labels)):
    ax = axes[i]
    # Draw the outer frame of the thermometer (simulated by a rectangle, here it is simplified, vertical lines can also be used, and more complex custom shapes can be used)
    # First draw the "glass tube" of the thermometer, using a white - filled background for simulation
    ax.bar(0, max_temp, width=0.5, color='white', edgecolor='black')
    # Draw the red "mercury" part, with the height equal to the corresponding data value
    ax.bar(0, values[i], width=0.5, color='red')
    # Set the y - axis range
    ax.set_ylim(0, max_temp)
    # Hide the x - axis ticks
    ax.set_xticks([])  
    # Add the TV drama name as the title
    ax.set_title(labels[i], y=-0.2)  
    # Display the percentage value above the thermometer
    ax.text(0, values[i] + 10, f"{values[i]}", ha='center')  

# Overall title
fig.suptitle("Comparison of Search Indexes of Popular TV Dramas after the Broadcast of In the Name of the People", fontsize=16, y=1.05)
# Adjust the layout
plt.tight_layout()
# Display the chart
plt.show()