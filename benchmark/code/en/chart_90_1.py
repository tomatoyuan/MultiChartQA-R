import matplotlib.pyplot as plt

# Data
quarters = ["2021Q2", "2021Q3", "2021Q4", "2022Q1"]
sales = [7.0, 5.0, 4.2, 10.9]
colors = ['#AED581', '#81C784', '#4DB6AC', '#9575CD']  # Soft color scheme

# Create a canvas
fig, ax = plt.subplots(figsize=(7, 5))

# Draw a donut chart
wedges, texts, autotexts = ax.pie(
    sales, 
    labels=quarters, 
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    wedgeprops=dict(width=0.6, edgecolor='white')
)

# Beautify the percentage texts
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(10)

# Add the total sales text to the center
total_sales = sum(sales)
ax.text(0, 0, f'{total_sales:.1f} Billion\nTotal Sales',
        ha='center', va='center',
        fontsize=13, fontweight='bold',
        color='#424242')

# Set the title
ax.set_title("Proportion of Beer E - commerce Sales from 2021Q2 to 2022Q1 (Unit: Billion Yuan)", fontsize=14, fontweight="bold", pad=20)

plt.tight_layout()
plt.show()