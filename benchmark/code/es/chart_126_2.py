import matplotlib.pyplot as plt
import numpy as np

# Datos de distribución regional en el lado izquierdo
regiones = ["Este de China", "Sur de China", "Suroeste de China", "Norte de China", "Centro de China", "Noroeste de China", "Noreste de China", "Hong Kong, Macao y Taiwán"]
proporciones_region = [24.2, 21.5, 17.6, 17.0, 9.8, 6.8, 3.0, 0.1]

# Datos de distribución por nivel de ciudad en el lado derecho
tipos_ciudad = ["Ciudades de primer nivel", "Nuevas ciudades de primer nivel", "Ciudades de segundo nivel", "Ciudades de tercer nivel", "Ciudades de cuarto nivel y otras"]
proporciones_ciudad = [20.2, 27.4, 29.6, 14.8, 8.0]
colores_ciudad = ["#FFD700", "#FF7F50", "#32CD32", "#8B4513", "#808000"]

fig = plt.figure(figsize=(16, 8))
# Subgráfico izquierdo (Distribución regional)
ax1 = fig.add_subplot(121)
x = np.arange(len(regiones))
barras = ax1.bar(x, proporciones_region, color=plt.cm.autumn(np.linspace(0, 1, len(regiones))))
for i, proporcion in enumerate(proporciones_region):
    ax1.text(i, proporcion + 1, f"{proporcion}%", ha="center", va="bottom")
ax1.set_ylabel("Proporción (%)")
ax1.set_xlabel("Región")
ax1.set_xticks(x)
ax1.set_xticklabels(regiones, rotation=45, ha="right")
ax1.set_title("Distribución regional de los consumidores chinos en 2024")

# Subgráfico derecho (Distribución por nivel de ciudad)
ax2 = fig.add_subplot(122)
porciones, textos, textos_automaticos = ax2.pie(proporciones_ciudad, labels=tipos_ciudad, colors=colores_ciudad, autopct="%1.1f%%", 
                                  pctdistance=0.8, startangle=90)
for texto_automatico in textos_automaticos:
    texto_automatico.set_color("white")
ax2.set_title("Distribución por nivel de ciudad de los consumidores chinos en 2024")

plt.tight_layout()
plt.show()