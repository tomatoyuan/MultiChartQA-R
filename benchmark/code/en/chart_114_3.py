import matplotlib.pyplot as plt

# Reasons for physical examination
reasons = ["Personal regular health check", "Mandatory check (e.g., pre - marriage check, pre - employment check)",
           "Suddenly want to know one's own health status", "Need to check due to illness"]
# Corresponding proportions (%)
proportions = [50.82, 44.83, 44.46, 31.22]
# Corresponding colors (consistent with the orange in the chart)
colors = ['#FF7F27', '#1E90FF', '#4B53FF', '#32CD32'] * len(reasons)

fig, ax = plt.subplots(figsize=(8, 8))
# Draw a donut chart, set the width to make the center hollow, and wedgeprops control the donut style
wedges, texts, autotexts = ax.pie(proportions, labels=reasons, colors=colors, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# Adjust the position of the annotation text to make it in the appropriate area of the donut (adapted for this donut layout)
for autotext in autotexts:
    autotext.set_horizontalalignment('center')
    autotext.set_verticalalignment('center')

ax.set_title('Reasons for Chinese health - check consumers to participate in physical examinations in 2025')

plt.show()