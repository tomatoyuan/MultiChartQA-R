import matplotlib.pyplot as plt
import numpy as np

# Datos
etiquetas = ['MAT TY', 'YTD TY', 'Ene', 'Feb']
valores_2023 = [-3.3, 2.1, 16.0, -10.4]
valores_2024 = [-3.5, -5.6, -22.5, 14.2]

x = np.arange(len(etiquetas))  # Posición en el eje X
ancho = 0.35  # Ancho de las barras

# Crear la figura y los ejes
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar el gráfico de barras
barras1 = ax.bar(x - ancho / 2, valores_2023, ancho, label='2023', color='#A9C6FB')  # Azul claro
barras2 = ax.bar(x + ancho / 2, valores_2024, ancho, label='2024', color='#1346D3')  # Azul oscuro

# Agregar texto de porcentaje
for i in range(len(etiquetas)):
    ax.text(x[i] - ancho / 2, valores_2023[i] + (0.8 if valores_2023[i] >= 0 else -2),
            f'{valores_2023[i]}%', ha='center', va='bottom' if valores_2023[i] >= 0 else 'top',
            fontsize=10, color='red' if valores_2023[i] < 0 else 'black')
    ax.text(x[i] + ancho / 2, valores_2024[i] + (0.8 if valores_2024[i] >= 0 else -2),
            f'{valores_2024[i]}%', ha='center', va='bottom' if valores_2024[i] >= 0 else 'top',
            fontsize=10, color='red' if valores_2024[i] < 0 else 'black')

# Agregar línea de división
ax.axvline(x=1.5, color='gray', linestyle='--', linewidth=1)

# Embellir el gráfico
ax.set_xticks(x)
ax.set_xticklabels(etiquetas)
ax.set_title('Incremento año con año en ventas minoristas de productos de consumo rápido %', fontsize=14, weight='bold')
ax.legend(loc='upper left')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)


# Agregar información sobre la fuente de los datos
plt.figtext(0.5, -0.05, 'Nota: El alcance son 79 categorías minoristas (sin incluir tiendas de bebé), Febrero 2024',
            wrap=True, horizontalalignment='center', fontsize=9, color='gray')
plt.ylim(-27.5, 20)
plt.tight_layout()
plt.show()