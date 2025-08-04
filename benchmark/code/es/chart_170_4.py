import matplotlib.pyplot as plt
import numpy as np

# Datos
grupos_edad = ["Menos de 20 años", "20 - 29 años", "30 - 39 años", "40 - 49 años", "50 - 59 años", "Más de 60 años"]
datos_2022 = np.array([6.6, 48.6, 35.8, 6.5, 2.1, 0.4])
datos_2023 = np.array([6.8, 46.9, 37.1, 6.9, 1.9, 0.4])

# Configurar posiciones
x = np.arange(len(grupos_edad))
ancho = 0.35

# Dibujar gráfico
fig, ax = plt.subplots(figsize=(10, 6))
barra1 = ax.bar(x - ancho/2, datos_2022, ancho, label='Año 2022', color="#efbfc2")
barra2 = ax.bar(x + ancho/2, datos_2023, ancho, label='Año 2023', color="#5c419d")

# Agregar etiquetas
ax.set_ylabel('Proporción (%)')
ax.set_title('Distribución de edades de los visitantes de Simple Psicología Consulta entre 2022 - 2023')
ax.set_xticks(x)
ax.set_xticklabels(grupos_edad)
ax.legend()

# Agregar etiquetas de datos
for barra in barra1 + barra2:
    altura = barra.get_height()
    ax.annotate(f'{altura}%',
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()