import matplotlib.pyplot as plt

# Years and average counseling session data
years = [2020, 2021, 2022, 2023]
avg_sessions = [10.8, 11.8, 12.8, 12.7]

# Color gradient: Transition from orange to pink
colors = ['#F6C143', '#F6A844', '#F4767E', '#EF6D95']

# Create a chart
plt.figure(figsize=(8, 5))
for i in range(len(years)-1):
    plt.plot([years[i], years[i+1]], [avg_sessions[i], avg_sessions[i+1]], color=colors[i], linewidth=2.5)
plt.scatter(years, avg_sessions, color=colors, s=100, zorder=5)

# Label the values
for x, y in zip(years, avg_sessions):
    plt.text(x, y + 0.3, f'{y}', ha='center', fontsize=12, fontweight='bold')

# Style settings
plt.title("Average Counseling Sessions of Client at JianDanXinLi from 2020 to 2023", fontsize=14, fontweight='bold', color='#4B3083')
plt.xticks(years)
plt.yticks(range(0, 16, 5))
plt.ylim(0, 15)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

# Display the chart
plt.show()