import matplotlib.pyplot as plt

# Data
labels = ["Meta", "Pico", "DPVR", "HTC", "HP Inc", "Others"]
sizes = [75, 6, 6, 5, 3, 5]
colors = ["#FF7F24", "#FFD700", "#32CD32", "#8B4513", "#808000", "#228B22"]

fig, ax = plt.subplots(figsize=(8, 8))
# Draw a pie chart, autopct shows the percentage, pctdistance adjusts the position of the percentage, startangle sets the starting angle
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", 
                                  pctdistance=0.8, startangle=90)

# Adjust the annotation text color to white (optional, to make the values clearer)
for autotext in autotexts:
    autotext.set_color("white")

ax.set_title("Global VR Headset Device Shipment Market Share")

plt.tight_layout()
plt.show()