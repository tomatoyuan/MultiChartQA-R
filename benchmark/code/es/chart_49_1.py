import matplotlib.pyplot as plt
import numpy as np

# Años
años = np.array([2019, 2020, 2021, 2022, 2023, 2024, 2025])
# Tamaño del mercado (en miles de millones de dólares estadounidenses), valores de 2023 - 2025 son valores pronosticados (E)
tamaño_mercado = np.array([2011, 1787, 2071, 2293, 2470, 2566, 2667])
# Marcar colores especiales para los años pronosticados (2023 - 2025)
colores = ['green'] * 4 + ['orange'] * 3

plt.figure(figsize=(10, 6))  # Establecer el tamaño del gráfico
barras = plt.bar(años, tamaño_mercado, color=colores)

# Agregar etiquetas numéricas sobre cada barra
for barra, valor in zip(barras, tamaño_mercado):
    altura = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2., altura + 15,
             f'{valor}', ha='center', va='bottom', fontsize=10)

# Agregar título y etiquetas de los ejes
plt.title('Tamaño y pronóstico del mercado global de té de 2019 - 2025', fontsize=14)
plt.xlabel('Año', fontsize=12)
plt.ylabel('Tamaño del mercado (en miles de millones de dólares estadounidenses)', fontsize=12)

# Establecer las marcas del eje x en años
plt.xticks(años)

# Agregar líneas de cuadrícula
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar el gráfico
plt.tight_layout()  # Ajustar el diseño
plt.show()