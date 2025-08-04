import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Data: Provinces and corresponding shopping cart quantities
data = {
    "Guangdong": 6,
    "Zhejiang": 3,
    "Beijing": 2
}
# Province coordinates (y-axis position, controlling vertical layout)
province_y = {
    "Guangdong": 2,
    "Zhejiang": 1,
    "Beijing": 0
}
# Basic size of the shopping cart
cart_width = 0.3
cart_height = 0.2

# Create a canvas
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_xlim(0, 7)
ax.set_ylim(-1, 3)
ax.axis('off')  # Hide the axes

# Draw the title - Modified the x-coordinate and alignment
ax.text(
    3.5, 2.8, "Which provinces have stronger 'shopping spree' power?", 
    fontsize=20, fontweight='bold',
    ha='center', va='top'
)

# Define a function to draw a single shopping cart
def draw_cart(x, y):
    """
    Draw a simplified shopping cart icon at position (x, y)
    """
    # Shopping cart basket (rectangle)
    cart_basket = patches.Rectangle(
        (x, y), cart_width, cart_height,
        facecolor='none', edgecolor='black'
    )
    ax.add_patch(cart_basket)
    # Shopping cart handle (simulated by a polygon)
    cart_handle = patches.Polygon(
        [[x - 0.1, y + cart_height],
         [x + cart_width + 0.1, y + cart_height],
         [x + cart_width / 2, y + cart_height + 0.2]],
        facecolor='none', edgecolor='black'
    )
    ax.add_patch(cart_handle)
    # Shopping cart wheels (two small circles)
    wheel1 = patches.Circle((x + 0.1, y - 0.1), 0.05, color='black')
    wheel2 = patches.Circle((x + 0.2, y - 0.1), 0.05, color='black')
    ax.add_patch(wheel1)
    ax.add_patch(wheel2)

# Iterate through the data to draw province names + shopping carts
for province, count in data.items():
    # Draw the province text
    ax.text(
        -1.2, province_y[province] + 0.1, 
        province, fontsize=16, fontweight='bold'
    )
    # Loop to draw shopping carts
    for i in range(count):
        cart_x = 1 + i * (cart_width + 0.2)  # Horizontal spacing between shopping carts
        draw_cart(cart_x, province_y[province])

plt.tight_layout()
plt.show()