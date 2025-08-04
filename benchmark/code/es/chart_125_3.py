import matplotlib.pyplot as plt
import numpy as np

# Gráfico circular a la izquierda
etiquetas_pastel = ["Centrado en", "Visto pero no profundamente entendido", "No preocupado"]
tamaños_pastel = [53.4, 42.2, 4.4]
colores_pastel = ["#FF9933", "#B34D4D", "#4D88B3"]

# Gráfico de barras a la derecha
canales_barra = ["Plataformas de comercio electrónico", "Plataformas sociales", "Plataformas de videos cortos", 
                 "Plataformas de compartición de contenido", "Tiendas especializadas físicas", 
                 "Exhibiciones de productos inteligentes", "Informado por amigos/familiares/compañeros de clase", "Otros"]
proporciones_barra = [60.2, 53.4, 41.4, 41.2, 32.5, 17.1, 9.6, 0.4]

fig = plt.figure(figsize=(16, 6))
# Subgráfico izquierdo
ax1 = fig.add_subplot(121)
porciones, textos, textos_automaticos = ax1.pie(tamaños_pastel, labels=etiquetas_pastel, colors=colores_pastel, autopct="%1.1f%%", 
                                               startangle=90, hatch="////")
for texto_automatico in textos_automaticos:
    texto_automatico.set_color("black")
ax1.set_title("Comprensión de los consumidores chinos \nsobre teléfonos móviles de pantalla pequeña")

# Subgráfico derecho
ax2 = fig.add_subplot(122)
x = np.arange(len(canales_barra))
barras = ax2.bar(x, proporciones_barra, color="#FF9933", hatch="////")
for i, proporcion in enumerate(proporciones_barra):
    ax2.text(i, proporcion + 1, f"{proporcion}%", ha="center", va="bottom")
ax2.set_ylabel("Proporción (%)")
ax2.set_xlabel("Canales de comprensión")
ax2.set_xticks(x)
ax2.set_xticklabels(canales_barra, rotation=15, ha="right")
ax2.set_title("Canales a través de los cuales los consumidores chinos se informan sobre teléfonos móviles de pantalla pequeña")

plt.tight_layout()
plt.show()