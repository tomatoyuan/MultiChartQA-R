import matplotlib.pyplot as plt
import numpy as np

# Datos
categorias = ['Labios de bajo saturación', 'Sombras de ojos con destellos finos', 'Sombras de ojos rosadas', 'Perfumes para conquistar hombres', 'Mascarillas para otoño e invierno', 'Aparatos de belleza domésticos']
crecimiento_comercio = [39.5, 22.7, 323.2, 4.4, 382.8, 151.7]
crecimiento_pago = [32.7, 22.2, 20.0, 168.1, 163.0, 32.1]

x = np.arange(len(categorias))
ancho = 0.35

# Dibujo
fig, ax = plt.subplots(figsize=(12, 6))
barras1 = ax.bar(x - ancho/2, crecimiento_comercio, ancho, label='Tasa de crecimiento del índice de transacción', color='orange')
barras2 = ax.bar(x + ancho/2, crecimiento_pago, ancho, label='Tasa de crecimiento de conversión de pago', color='orangered')

# Configuración de texto
ax.set_ylabel('Tasa de crecimiento (%)')
ax.set_title('Datos de búsqueda y transacción de categorías relacionadas en Taobao')
ax.set_xticks(x)
ax.set_xticklabels(categorias, rotation=30)
ax.legend()

# Agregar etiquetas de datos
for barra in barras1 + barras2:
    altura = barra.get_height()
    ax.annotate(f'{altura:.1f}%',
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom')

plt.ylim(0, 420)
plt.tight_layout()
plt.show()