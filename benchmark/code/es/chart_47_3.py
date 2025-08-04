import matplotlib.pyplot as plt
import numpy as np

# Años
años = [2022, 2023, 2024]
# Monto de transacciones (mil millones de yuanes)
montos = [2763, 2818, 2959]

x = np.arange(len(años))
ancho = 0.5

fig, ax = plt.subplots(figsize=(10, 6))
rects = ax.bar(x, montos, ancho, label='Monto de Transacción', color='#D9B3A6')

# Etiquetar el monto de transacción
for rect, monto in zip(rects, montos):
    altura = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2., altura + 5,
            f'{monto}', ha='center', va='bottom')

# Establecer el rango del eje Y para magnificar la diferencia de altura
ax.set_ylim(2700, 3000)

ax.set_ylabel('Unidad: Mil Millones de Yuanes')
ax.set_title('Tendencia de la Escala de Ventas Minoristas de Productos de Cuidado de la Piel de 2022 a 2024')
ax.set_xticks(x)
ax.set_xticklabels(años)
ax.legend()

plt.tight_layout()
plt.show()