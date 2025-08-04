import matplotlib.pyplot as plt

# Years
years = list(range(2015, 2027))

# Global retail growth rate (black line)
retail_growth = [6.2, 6.0, 6.5, 4.5, 5.3, -2.6, 5.0, 6.9, 3.9, 4.3, 3.7, 3.4]

# Global e - commerce retail growth rate (orange line)
ecommerce_growth = [23.0, 26.8, 28.4, 22.0, 20.9, 26.7, 16.8, 7.1, 8.9, 9.4, 8.8, 8.1]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(years, retail_growth, marker='o', color='black', label='Global Retail Growth')
plt.plot(years, ecommerce_growth, marker='o', color='orange', label='Global E - commerce Retail Growth')

# Label the data of each point
for i, (r, e) in enumerate(zip(retail_growth, ecommerce_growth)):
    plt.text(years[i], r + 0.5, f'{r}%', ha='center', va='bottom', fontsize=9, color='black')
    plt.text(years[i], e + 0.5, f'{e}%', ha='center', va='bottom', fontsize=9, color='orange')

plt.title("Changes in Global Retail and Global E - commerce Retail Growth Rates", fontsize=14)
plt.xlabel("Year")
plt.ylabel("Growth Rate (%)")
plt.ylim(-5, 30)
plt.xticks(years)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()