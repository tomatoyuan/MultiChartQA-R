import matplotlib.pyplot as plt
import numpy as np

# --------------------- Datos del gráfico circular de frecuencia de compra ---------------------
etiquetas_frecuencia = ["Una vez al mes", "Una vez cada 2 - 3 meses", "Una vez a la semana", "2 - 3 veces a la semana o más", "Una vez cada seis meses", "Casi nunca compra"]
tamaños_frecuencia = [31.0, 23.7, 16.2, 6.2, 9.6, 2.7]  # Ordenar los datos en el orden de la leyenda
colores_frecuencia = ["#32CD32", "#8B4513", "#FFD700", "#FF7F50", "#D2B48C", "#8F9779"]

# --------------------- Datos del gráfico de barras del precio unitario aceptable ---------------------
etiquetas_precio = ["10 yuanes o menos", "11 - 30 yuanes", "31 - 50 yuanes", "51 - 100 yuanes", "101 - 150 yuanes", "151 - 200 yuanes", "Más de 200 yuanes"]
porcentajes_precio = [2.1, 10.2, 25.5, 32.3, 15.7, 8.3, 5.9]

# Crear un lienzo con un diseño de 1 fila y 2 columnas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# --------------------- Dibujar el gráfico circular de frecuencia de compra (gráfico izquierdo) ---------------------
trozos, textos, textos_automaticos = ax1.pie(tamaños_frecuencia, colors=colores_frecuencia, autopct='%1.1f%%', startangle=90)
ax1.set_title('Frecuencia de compra de productos culturales y creativos por los consumidores chinos en 2023')
# Ajustar la leyenda (coincidir en el orden del gráfico original)
ax1.legend(trozos, etiquetas_frecuencia, title="Frecuencia de compra", loc="center left", bbox_to_anchor=(1, 0.5))
# Ajustar el color del texto de la anotación
for texto_automatico in textos_automaticos:
    texto_automatico.set_color('white' if texto_automatico.get_position()[1] > 0.5 else 'black')

# --------------------- Dibujar el gráfico de barras del precio unitario aceptable (gráfico derecho) ---------------------
x = np.arange(len(etiquetas_precio))
barras = ax2.bar(x, porcentajes_precio, color='orange')
ax2.set_title('Precio unitario aceptable de productos culturales y creativos para los consumidores chinos en 2023')
ax2.set_ylabel('Porcentaje (%)')
ax2.set_xticks(x)
ax2.set_xticklabels(etiquetas_precio, rotation=45, ha='right')
# Agregar anotaciones numéricas
for i, porcentaje in enumerate(porcentajes_precio):
    ax2.text(i, porcentaje + 1, f'{porcentaje}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()