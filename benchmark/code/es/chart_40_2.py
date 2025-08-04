import matplotlib.pyplot as plt
import numpy as np

# Años
years = np.array([2022, 2023, 2024, 2025, 2026])
# Datos del tamaño del mercado (en miles de millones de yuanes), simulando aproximadamente la tendencia de los datos originales
market_size = np.array([1804, 2045, 2284, 2510, 2737])

# Crear una figura y establecer un tamaño razonable
fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras y guardar el objeto contenedor devuelto
bars = ax.bar(years, market_size, color='r', label='Tamaño del mercado (en miles de millones de yuanes)')
ax.set_xlabel('Año')
ax.set_ylabel('Tamaño del mercado (en miles de millones de yuanes)', color='r')
ax.tick_params(axis='y', labelcolor='r')

# Establecer las marcas de graduación del eje x como años
ax.set_xticks(years)

# Generar etiquetas de año con 'E'
year_labels = []
for year in years:
    if year in [2025, 2026]:
        year_labels.append(f"{year}E")  # Agregar 'E' para los años pronosticados
    else:
        year_labels.append(str(year))   # Mantener los años reales sin cambios

# Establecer etiquetas de año con 'E'
ax.set_xticklabels(year_labels)

# Etiquetar el valor encima de cada barra (sin 'E')
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2.,  # Coordenada x: centro de la barra
        height + 15,  # Coordenada y: 15 unidades por encima de la parte superior de la barra
        f'{height}',  # Mostrar el valor
        ha='center',  # Alineación horizontal centrada
        va='bottom',  # Alineación vertical en la parte inferior
        color='r',    # Color del texto es el mismo que el de la barra
        fontsize=10   # Tamaño de fuente
    )

# Agregar un título
plt.title('Tamaño del mercado de los aperitivos picantes en China desde 2022 hasta 2026 (en miles de millones de yuanes)')

# Usar el método fig.text() para agregar anotaciones
fig.text(0.5, 0.85, 'Los aperitivos picantes tienen aproximadamente 1.6 veces la TCA de la industria de los aperitivos',
         ha='center', fontsize=10)

fig.text(0.15, 0.80, '*TCA de la industria de los aperitivos = 6.0%', fontsize=8)

# Agregar una leyenda
ax.legend(loc='upper left')

# Ajustar el diseño
plt.tight_layout()
# Mostrar el gráfico
plt.show()