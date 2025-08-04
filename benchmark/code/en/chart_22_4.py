import matplotlib.pyplot as plt
import numpy as np

# Official partner data
partners = {
    "Shell": 0.2,
    "Tag Heuer": 0.4
}

# Calculate total amount
total = sum(partners.values())

# Create a figure
plt.figure(figsize=(10, 6))

# Official partners horizontal bar chart
partner_names = list(partners.keys())
partner_values = list(partners.values())

# Plot horizontal bar chart
y_pos = np.arange(len(partner_names))
bars = plt.barh(y_pos, partner_values, align='center', color='#4e79a7', height=0.6)
plt.yticks(y_pos, partner_names, fontsize=12)
plt.xlabel('Amount (100 million yuan)', fontsize=12)
plt.title('Distribution of Official Partners and Suppliers', fontsize=14)
plt.xlim(0, max(partner_values) * 1.3)  # Adjust x-axis range to leave space for labels

# Add value labels on the bars
for i, v in enumerate(partner_values):
    plt.text(v + 0.01, i, f'{v:.2f} 100 million yuan', va='center', fontsize=11)
    plt.text(v + 0.01, i - 0.3, f'({v/total*100:.1f}%)', va='center', fontsize=9, color='gray')

# Add total information
plt.axvline(x=total, color='r', linestyle='--', alpha=0.5)
plt.text(total + 0.01, len(partner_names), f'Total: {total:.2f} 100 million yuan', va='center', fontsize=11, color='red')

plt.tight_layout()
plt.show()