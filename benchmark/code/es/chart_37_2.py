import matplotlib.pyplot as plt
import numpy as np

# Nombres de las categorías
categorias = ["Calcetines funcionales para el exterior", "Leggings de tiburón", "Zapatillas de trail running", "Ropa de gabardina suave", 
              "Ropa para mujeres de mediana edad", "Abrigos de algodón cálidos", "Uniformes de pelota deportiva", "Hanfu - Estilo neochino", 
              "Chalecos de plumón", "Camisas deportivas de polo"]
# Datos de la tasa de crecimiento del monto de transacción simulados, aproximadamente cercanos a la proporción del gráfico original
datos = [92, 88, 65, 60, 55, 52, 48, 45, 42, 38]  

x = np.arange(len(categorias))  # Posiciones en el eje x

fig, ax = plt.subplots()
# Dibujar un gráfico de barras, establecer el color a un color similar a marrón y ajustar el ancho de la barra
barras = ax.bar(x, datos, width=0.6, color='#b38878')  

# Establecer el rango del eje y
ax.set_ylim([30, 100])  
# Establecer las marcas y las etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(categorias, rotation=45, ha='right')  

# Agregar etiqueta al eje y
ax.set_ylabel('Tasa de crecimiento del\n monto de transacción', fontsize=10)  
# Agregar título
ax.set_title('Las 10 categorías con mayor crecimiento en la escala de negocios \ndel comercio electrónico de otoño e invierno de Douyin en 2024', fontsize=14, pad=85)  

# Agregar etiquetas de datos
for barra in barras:
    altura = barra.get_height()
    ax.annotate(f'{altura}',
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3),  # Desplazamiento vertical de 3 puntos
                textcoords="offset points",
                ha='center', va='bottom')

# Ocultar los bordes superior y derecho
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()  # Ajustar el diseño
plt.show()