import matplotlib.pyplot as plt
import numpy as np

# Preparación de datos
años = ["2018", "2019", "2020", "2021", "2022"]
ingreso_nacional = [28228, 30733, 32189, 35128, 36883]  # Ingreso disponible per cápita nacional (yuan)
ingreso_urbano = [39251, 42359, 43834, 47412, 49283]    # Ingreso disponible per cápita urbano (yuan)
tasas_de_crecimiento = [8.7, 8.9, 4.7, 9.1, 5.0]        # Tasa de crecimiento interanual del ingreso disponible (%)

x = np.arange(len(años))

fig, ax1 = plt.subplots(figsize=(10, 6))

# Dibujar gráficos de barras del ingreso disponible per cápita nacional y urbano
ax1.bar(x - 0.2, ingreso_nacional, width=0.4, color='lightcoral', label='Ingreso disponible per cápita nacional (yuan)')
ax1.bar(x + 0.2, ingreso_urbano, width=0.4, color='coral', label='Ingreso disponible per cápita urbano (yuan)')
ax1.set_ylabel('Ingreso (yuan)')
ax1.set_xlabel('Año')
ax1.set_xticks(x)
ax1.set_xticklabels(años)
ax1.legend(loc='upper left')

# Crear un eje y secundario y dibujar un gráfico de línea de la tasa de crecimiento interanual
ax2 = ax1.twinx()
ax2.plot(x, tasas_de_crecimiento, marker='o', color='gray', label='Tasa de crecimiento interanual (%)', linewidth=2)
ax2.set_ylabel('Tasa de crecimiento interanual (%)')
ax2.legend(loc='center right')

# Agregar etiquetas de valor para el ingreso nacional y urbano
for i, (nacional, urbano) in enumerate(zip(ingreso_nacional, ingreso_urbano)):
    ax1.text(i - 0.2, nacional + 500, f'{nacional}', ha='center', va='bottom', color='black')
    ax1.text(i + 0.2, urbano + 500, f'{urbano}', ha='center', va='bottom', color='black')

# Agregar etiquetas de valor para la tasa de crecimiento interanual
for i, tasa in enumerate(tasas_de_crecimiento):
    ax2.text(i, tasa + 0.5, f'{tasa}%', ha='center', va='bottom', color='black')

ax1.set_title('Ingreso disponible per cápita en China desde 2018 hasta 2022')
plt.tight_layout()
plt.show()