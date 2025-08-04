import matplotlib.pyplot as plt
import numpy as np

# Data
expectations = [
    "Long - lasting product effects", "Products with compound efficacy", "Increased promotion/discounts",
    "More beautiful and creative packaging design", "Affordable products", "More new domestic brands",
    "More purchasing channels for convenient shopping", "Improved service attitude of shopping guides/salespersons", "Improved after - sales service"
]
percentages = [61.1, 41.2, 40.9, 39.6, 31.0, 29.5, 28.7, 17.0, 10.4]

x = np.arange(len(expectations))

fig, ax = plt.subplots(figsize=(10, 7))

# Draw a bar chart
bars = ax.barh(x, percentages, color='orange')  # Horizontal bar chart is more suitable for displaying this type of data
ax.set_xlabel('Expected proportion (%)')
ax.set_ylabel('Expected content')
ax.set_yticks(x)
ax.set_yticklabels(expectations)
ax.invert_yaxis()  # Display the first expectation at the top
ax.set_title('Survey on Chinese consumers\' expectations for the development of the cosmetics industry in 2023')

# Add numerical labels
for bar in bars:
    length = bar.get_width()
    ax.text(length + 1, bar.get_y() + bar.get_height() / 2,
            f'{length}%', ha='left', va='center')

plt.tight_layout()
plt.show()