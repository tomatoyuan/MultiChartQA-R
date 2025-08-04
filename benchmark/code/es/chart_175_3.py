import matplotlib.pyplot as plt
import numpy as np

# 数据
etiquetas = [
    "Establecimiento de marca y \n"
    "aumento de la conciencia", "Adquisición de recursos de\n marketing y desarrollo de actividades de marketing", "Garantía de una cadena de fondos estable",
    "Elaboración de estrategias", "Construcción y operación de canales de venta", "Adquisición de usuarios y conversión de ventas", "Innovación de productos y localización"
]
x = np.arange(len(etiquetas))  # Posición en el eje x
ancho = 0.35  # Ancho de las barras

# Datos de empresas de exportación emergentes y empresas de exportación maduras
empresas_emergentes = [9, 19, 20, 24, 20, 22, 22]
empresas_maduras = [12, 6, 9, 9, 16, 21, 22]

# Dibujar el gráfico
fig, ax = plt.subplots(figsize=(12, 6))
barras1 = ax.barh(x - ancho/2, empresas_emergentes, ancho, label='Empresas de exportación emergentes', color='#0072CE')
barras2 = ax.barh(x + ancho/2, empresas_maduras, ancho, label='Empresas de exportación maduras', color='#7EC0EE')

# Añadir etiquetas de valores
for barra in barras1 + barras2:
    ax.text(barra.get_width() + 0.5, barra.get_y() + barra.get_height()/2,
            f'{barra.get_width()}%', va='center', fontsize=9)

# Ejes y etiquetas
ax.set_yticks(x)
ax.set_yticklabels(etiquetas, fontsize=10)
ax.invert_yaxis()  # Invertir el eje Y
ax.set_xlabel('Proporción (%)')
ax.set_title('Los desafíos de exportación varían según el tipo de empresa de exportación')
ax.legend()

plt.tight_layout()
plt.show()