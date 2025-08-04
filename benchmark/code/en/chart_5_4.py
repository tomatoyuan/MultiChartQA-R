import matplotlib.pyplot as plt
import numpy as np

# Dates (x-axis, converted to numbers for plotting, original dates will be shown)
dates = np.arange(1, 29, 2)
date_labels = ['Feb 1', 'Feb 3', 'Feb 5', 'Feb 7', 'Feb 9', 'Feb 11', 'Feb 13', 'Feb 15', 'Feb 17', 'Feb 19', 'Feb 21', 'Feb 23', 'Feb 25', 'Feb 27']

# Search attention of various types of milk powder (y-axis)
children_milk = [1000, 1200, 1300, 1500, 1400, 1450, 1420, 1430, 1400, 4000, 1300, 1200, 1100, 1000]
pregnant_milk = [15000, 20000, 25000, 30000, 28000, 28500, 29000, 29500, 28000, 25000, 30000, 25000, 40000, 18000]
infant_milk = [2000, 2200, 2300, 2400, 2350, 2400, 2420, 2430, 2400, 2500, 2300, 2200, 2100, 2000]
student_milk = [2500, 2600, 2700, 2800, 2750, 2800, 2820, 2830, 2800, 2900, 2700, 2600, 2500, 2400]

# Plotting
plt.figure(figsize=(14, 8))

# Draw line charts
children_line, = plt.plot(dates, children_milk, color='orange', label='Children\'s Milk Powder', linewidth=2)
infant_line, = plt.plot(dates, infant_milk, color='blue', label='Infant Milk Powder', linewidth=2)
pregnant_line, = plt.plot(dates, pregnant_milk, color='pink', label='Pregnant Women\'s Milk Powder', linewidth=2)
student_line, = plt.plot(dates, student_milk, color='lightblue', label='Student Milk Powder', linewidth=2)

# Set x-axis ticks and labels
plt.xticks(dates, date_labels, rotation=45)

# Set title and axis labels
plt.title('Search Attention Trends by Category in February', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Search Attention', fontsize=12)

# Add grid lines
plt.grid(True, linestyle='--', alpha=0.7)

# Add smart annotations to data points to avoid overlap
def add_smart_annotations(x, y, color, label, is_pregnant=False):
    """Add smart annotations to data points to avoid overlap"""
    # Collect all placed annotation positions
    placed_annotations = []

    for i, (date, value) in enumerate(zip(x, y)):
        # Format the value with thousands separators
        value_str = f"{value:,}"

        # Base offset
        base_offset = 15

        # Set a larger base offset for pregnant women's milk powder
        if is_pregnant:
            base_offset = 30

        # Check if it overlaps with existing annotations
        overlaps = True
        attempts = 0
        max_attempts = 8
        offset = base_offset

        while overlaps and attempts < max_attempts:
            # Try different angles and distances to place the annotation
            angle = (attempts % 4) * 90  # 0, 90, 180, 270 degrees
            distance = base_offset + (attempts // 4) * 10  # Increase distance every two attempts

            # Calculate the offset
            if angle == 0:  # Right
                xytext = (distance, 0)
                ha = 'left'
                va = 'center'
            elif angle == 90:  # Top
                xytext = (0, distance)
                ha = 'center'
                va = 'bottom'
            elif angle == 180:  # Left
                xytext = (-distance, 0)
                ha = 'right'
                va = 'center'
            else:  # Bottom
                xytext = (0, -distance)
                ha = 'center'
                va = 'top'

            # Check for overlap
            overlaps = False
            for (x_annot, y_annot) in placed_annotations:
                # Calculate the distance
                dist = np.sqrt((date - x_annot)**2 + (value - y_annot)**2)
                # Consider it overlapping if the distance is too close
                if dist < 30:  # The threshold can be adjusted
                    overlaps = True
                    break

            if not overlaps:
                # No overlap, record this position
                placed_annotations.append((date + xytext[0]/10, value + xytext[1]/10))
                break

            attempts += 1

        # If unable to find a non - overlapping position after multiple attempts, use the default position
        if overlaps:
            xytext = (0, base_offset)
            ha = 'center'
            va = 'bottom'

        # Add annotation
        plt.annotate(value_str,
                     (date, value),
                     textcoords="offset points",
                     xytext=xytext,
                     ha=ha,
                     va=va,
                     fontsize=8,
                     color=color,
                     bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=color, alpha=0.8))


# Add smart annotations for various types of milk powder
add_smart_annotations(dates, children_milk, 'orange', 'Children\'s Milk Powder')
add_smart_annotations(dates, infant_milk, 'blue', 'Infant Milk Powder')
add_smart_annotations(dates, pregnant_milk, 'pink', 'Pregnant Women\'s Milk Powder', True)
add_smart_annotations(dates, student_milk, 'lightblue', 'Student Milk Powder')

# Add legend
plt.legend(fontsize=10, loc='upper left')

# Add data source description
plt.figtext(0.1, 0.01, 'Data Source: Fictitious data for demonstration only', ha="left", fontsize=9, bbox={"facecolor": "white", "alpha": 0.5, "pad": 5})

# Optimize layout
plt.tight_layout()

# Display the chart
plt.show()