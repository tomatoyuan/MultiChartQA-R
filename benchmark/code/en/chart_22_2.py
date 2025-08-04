import matplotlib.pyplot as plt
import numpy as np

# Data
total_revenue = 15
media_rights = 10
sponsors = {
    "Ping An Insurance": 1.815,
    "Nike": 1,
    "Ford": 0.4,
    "JD.com": 0.35,
    "Carlsberg": 0.2,
    "DHL": 0.2,
    "Red Bull": 0.2
}
partners = {
    "Shell": 0.2,
    "TAG Heuer": 0.4
}

# Calculate other revenue
other_revenue = total_revenue - media_rights - sum(sponsors.values()) - sum(partners.values())

# Create figure
plt.figure(figsize=(12, 10))

# Prepare bar chart data
categories = ["Media Rights", "Sponsors", "Official Partners", "Other"]
values = [media_rights, sum(sponsors.values()), sum(partners.values()), other_revenue]
colors = ['#4e79a7', '#f28e2b', '#e15759', '#76b7b2']

# Plot main bar chart - revenue by category
plt.subplot(2, 1, 1)
bars = plt.bar(categories, values, color=colors)
plt.title('Chinese Super League Company Revenue Distribution (by Category)')
plt.ylabel('Amount (CNY 100 million)')

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.2f} CNY ({height/total_revenue*100:.1f}%)',
             ha='center', va='bottom')

# Plot detailed bar chart for sponsors and partners
plt.subplot(2, 1, 2)

# Combine sponsor and partner data
sponsor_names = list(sponsors.keys())
sponsor_values = list(sponsors.values())
partner_names = list(partners.keys())
partner_values = list(partners.values())

# Set bar positions
x_sponsor = np.arange(len(sponsor_names))
x_partner = np.arange(len(partner_names)) + len(sponsor_names) + 1

# Plot sponsor bars
plt.bar(x_sponsor, sponsor_values, width=0.6, label='Sponsors', color='#59a14f')
# Plot partner bars
plt.bar(x_partner, partner_values, width=0.6, label='Partners', color='#af7aa1')

# Set x-axis labels and ticks
plt.xticks(list(x_sponsor) + list(x_partner), sponsor_names + partner_names, rotation=45, ha='right')
plt.title('Detailed Revenue from Sponsors and Partners')
plt.ylabel('Amount (CNY 100 million)')
plt.legend()

# Add value labels on bars
for i, v in enumerate(sponsor_values):
    plt.text(x_sponsor[i], v + 0.02, f'{v:.2f}', ha='center')
for i, v in enumerate(partner_values):
    plt.text(x_partner[i], v + 0.02, f'{v:.2f}', ha='center')

plt.tight_layout()
plt.show()