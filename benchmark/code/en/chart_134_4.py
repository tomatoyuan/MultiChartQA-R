import matplotlib.pyplot as plt
import numpy as np

# Data
expectations = ["Long - lasting product effect", "More refined product efficacy", "More beautiful and creative packaging design", 
                "Affordable price", "High product safety", "Launch of products with compound efficacy"]
percentages = [71.4, 47.0, 45.0, 37.1, 32.7, 31.9]

x = np.arange(len(expectations))

fig, ax = plt.subplots(figsize=(10, 6))

# Draw a bar chart
bars = ax.bar(x, percentages, color='orange')

# Add numerical annotations
for i, percentage in enumerate(percentages):
    ax.text(i, percentage + 1, f'{percentage}%', ha='center', va='bottom')

# Set the axes
ax.set_ylabel('Percentage (%)')
ax.set_xlabel('Expectation type')
ax.set_xticks(x)
ax.set_xticklabels(expectations, rotation=15, ha='right')
ax.set_title('Chinese consumers\' expectations for the development of sunscreen cosmetics')

plt.tight_layout()
plt.show()