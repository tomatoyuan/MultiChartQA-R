import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import matplotlib.colors as mcolors
import numpy as np

# Extract chart content
cases = [
    {
        "date": datetime(2024, 8, 21),
        "desc": "18-year-old college freshman Xu Yuyu\npassed away from cardiac arrest after being scammed out of 9,900 yuan",
        "severity": "Extremely High",  # New severity field
        "color": "#e41a1c"  # New color mapping
    },
    {
        "date": datetime(2024, 8, 23),
        "desc": "Sophomore Song from Shandong University of Technology\ndied suddenly after losing 1,996 yuan to telecom fraud",
        "severity": "High",
        "color": "#ff7f00"
    },
    {
        "date": datetime(2024, 8, 29),
        "desc": "A teacher from Tsinghua University fell victim to telecom fraud\nwith the involved amount reaching 17.6 million yuan",
        "severity": "Medium",
        "color": "#4daf4a"
    },
    {
        "date": datetime(2024, 8, 31),
        "desc": "19-year-old girl Cai Yanyan from Jieyang, Guangdong\ndrowned herself after being scammed out of over 10,000 yuan in tuition and living expenses via text message",
        "severity": "High",
        "color": "#ff7f00"
    },
    {
        "date": datetime(2024, 9, 6),
        "desc": "Sophomore Duan from Jilin Business and Technology College\ntook his own life after being scammed out of 5,000 yuan in tuition fees",
        "severity": "High",
        "color": "#ff7f00"
    }
]

# Split data for easier plotting
dates = [case["date"] for case in cases]
descriptions = [case["desc"] for case in cases]
colors = [case["color"] for case in cases]
severities = [case["severity"] for case in cases]

# Create canvas
fig, ax = plt.subplots(figsize=(14, 8))
fig.patch.set_facecolor('#f8f9fa')  # Set canvas background color
ax.set_facecolor('#ffffff')  # Set plotting area background color

# Draw horizontal bar chart, set colors according to severity
y_ticks = range(len(descriptions))
bars = ax.barh(y_ticks, [1]*len(descriptions), 
               left=mdates.date2num(dates), 
               height=0.6, 
               color=colors,
               alpha=0.8,
               edgecolor='black',
               linewidth=0.5)

# Add data labels
for i, (date, bar) in enumerate(zip(dates, bars)):
    ax.text(mdates.date2num(date) + 0.1, i, 
            date.strftime('%m-%d'), 
            va='center', 
            fontsize=10,
            fontweight='bold')

# Set x-axis to date format
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))  # Display a tick every 2 days
ax.set_xlabel("Date", fontsize=12, fontweight='bold')
ax.set_xlim(mdates.date2num(min(dates)) - 1, mdates.date2num(max(dates)) + 2)  # Adjust x-axis range

# Set y-axis to case descriptions
ax.set_yticks(y_ticks)
ax.set_yticklabels(descriptions, fontsize=10)

# Add title
ax.set_title("Timeline of Typical Telecom Fraud Cases", fontsize=18, fontweight="bold", pad=20)
ax.title.set_color('#333333')

# Add grid
ax.grid(axis="x", linestyle="--", alpha=0.6, color='#cccccc')

# Add severity legend
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label='Extremely High',
                          markerfacecolor='#e41a1c', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='High',
                          markerfacecolor='#ff7f00', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='Medium',
                          markerfacecolor='#4daf4a', markersize=10)]

ax.legend(handles=legend_elements, title='Case Severity', loc='lower right')

# Add bottom note
plt.figtext(0.5, 0.01, 'Data Source: Compiled from public reports', ha='center', fontsize=9, color='#666666')

# Optimize layout
plt.tight_layout()
plt.subplots_adjust(bottom=0.08)  # Adjust bottom margin
plt.show()