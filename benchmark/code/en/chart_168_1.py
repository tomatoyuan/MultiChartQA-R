import matplotlib.pyplot as plt

# Data
years = ['2019', '2020', '2021', '2022', '2023']
market_size = [1199, 1221, 1404, 1415, 1549]
growth_rate = [3, 2, 15, 1, 9]

# Create a chart and dual y - axes
fig, ax1 = plt.subplots(figsize=(10, 6))

# Set the primary axis (left axis) - Bar chart
bars = ax1.bar(years, market_size, color='red', label='Market Size (Billion Yuan)')
ax1.set_ylabel('Market Size (Billion Yuan)', fontsize=12, color='red')
ax1.tick_params(axis='y', labelcolor='#000000')

# Add data labels to the bar chart
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 10, f'{yval}', ha='center', va='bottom', fontsize=11, color='red')

# Create the secondary axis (right axis) - Line chart
ax2 = ax1.twinx()
ax2.plot(years, growth_rate, color='#F6A700', marker='o', linewidth=2.5, label='Year - on - Year Growth Rate')
ax2.set_ylabel('Year - on - Year Growth Rate (%)', fontsize=14, color='#F6A700')
ax2.tick_params(axis='y', labelcolor='#000000')

# Add data labels to the line chart
for i, txt in enumerate(growth_rate):
    ax2.text(years[i], growth_rate[i] + 0.5, f'{txt}%', ha='center', va='bottom', fontsize=11, color='#F6A700')

# Add a title and legend
plt.title('Trend of the Chinese Tissue Paper Market Size', fontsize=14, pad=20)
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9), fontsize=12)
plt.text(0.5, -0.1, 'Data Source: China National Pulp and Paper Association', fontsize=10, ha='center', transform=ax1.transAxes)

plt.tight_layout()
plt.show()