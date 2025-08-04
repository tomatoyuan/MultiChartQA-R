import matplotlib.pyplot as plt

# Data
brands = [
    "NEC UEFA Euro Night",
    "Xiaomi UEFA Euro Boiling Night",
    "Samsung UEFA Euro Night",
    "Tiguan One Million Owners UEFA Euro Night",
    "Junyue New Era UEFA Euro Night",
    "KanShang Meizu Good Products Youth Super Night",
    "Hisense UEFA Euro One Thousand People Carnival Sleepless Night",
    "Didi Taxi UEFA Euro Night",
    "Chang'an Suzuki Caravan Cool Night",
    "Bovard Embassy UEFA Euro Night"
]
ratings = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Create a canvas and sub - plot
fig, ax = plt.subplots(figsize=(10, 6))  # figsize can adjust the chart size

# Draw a horizontal bar chart
ax.barh(brands[::-1], ratings[::-1], color='royalblue')

# Set the title and axis labels
ax.set_title('Star Ratings of Brand Off - line Marketing Activities Competing for "UEFA Euro Night"', fontsize=14, fontweight='bold')
ax.set_xlabel('Star Rating', fontsize=12)
ax.set_ylabel('Brand Activities', fontsize=12)

# Set the x - axis ticks (from 0 to 10 according to the star ratings)
ax.set_xticks(range(0, 11))

# Display the chart
plt.tight_layout()  # Adjust the layout to avoid label overlap
plt.show()