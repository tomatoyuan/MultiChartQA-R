import matplotlib.pyplot as plt
import numpy as np

# Datos de los partidos (confrontación del partido, marcador, valor de popularidad)
partidos = ["Rusia 5:0 Arabia Saudí", 
            "Portugal 3:3 España", 
            "Egipto 0:1 Uruguay", 
            "Brasil 1:1 Suiza", 
            "Túnez 1:2 Inglaterra"]
valores_popularidad = [150, 136, 103, 78, 65]  # Valor de popularidad (unidad: diez mil, simplificado a valor numérico)

# Usado para mostrar en el eje X
x = np.arange(len(partidos))  

# Crear un lienzo
fig, ax = plt.subplots(figsize=(10, 6))
# Dibujar un gráfico de barras
rectangulos = ax.bar(x, valores_popularidad, width=0.6, color="#7B68EE")  

# Establecer las marcas y etiquetas del eje X
ax.set_xticks(x)
ax.set_xticklabels(partidos, rotation=45, ha="right", fontsize=10)  

# Establecer la etiqueta del eje Y
ax.set_ylabel("Valor de Popularidad (Diez Mil)", fontsize=12)  
# Establecer el título
ax.set_title("Ranking de Popularidad Top 5 de la Primera Ronda de la Fase de Grupos de la Copa del Mundo", fontsize=14, fontweight="bold")  

# Anotar los valores en las barras
for rectangulo in rectangulos:
    altura = rectangulo.get_height()
    ax.annotate(f"{altura}K", 
                xy=(rectangulo.get_x() + rectangulo.get_width() / 2, altura), 
                xytext=(0, 3),  # Desplazamiento hacia arriba de 3 píxeles
                textcoords="offset points", 
                ha="center", va="bottom")

# Optimizar el diseño (evitar que las etiquetas se muestren incompletas)
plt.tight_layout()  
# Mostrar el gráfico
plt.show()