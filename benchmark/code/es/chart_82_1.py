import matplotlib.pyplot as plt
import numpy as np

# Años
years = np.arange(2015, 2022)

# Datos (ejemplo, se pueden ajustar según la situación real)
# Nivel de alfabetización en salud de los residentes (%)
health_literacy = [10.4, 11.6, 14.3, 17.1, 19.5, 23.2, 25.4]
# Nivel de alfabetización en estilos de vida saludables y conductas saludables (%)
lifestyle_literacy = [10.3, 9.8, 14.2, 17.0, 19.2, 26.4, 28.1]

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 6))

# Trazar la línea para el nivel de alfabetización en salud de los residentes (con etiquetas superiores)
health_line, = ax.plot(years, health_literacy, marker='o', color='#A4C639', label='Nivel de alfabetización en salud de los residentes (%)', linewidth=2)
# Trazar la línea para el nivel de alfabetización en estilos de vida saludables y conductas saludables (con etiquetas inferiores)
lifestyle_line, = ax.plot(years, lifestyle_literacy, marker='o', color='#64B5F6', label='Nivel de alfabetización en estilos de vida saludables y conductas saludables (%)', linewidth=2)

# Agregar etiquetas superiores a la línea del nivel de alfabetización en salud de los residentes
for x, y in zip(years, health_literacy):
    ax.annotate(f'{y}%',
                xy=(x, y),
                xytext=(0, 5),  # Desplazamiento hacia arriba
                textcoords='offset points',
                ha='center',
                va='bottom',
                color='#A4C639')

# Agregar etiquetas inferiores a la línea del nivel de alfabetización en estilos de vida saludables y conductas saludables
for x, y in zip(years, lifestyle_literacy):
    ax.annotate(f'{y}%',
                xy=(x, y),
                xytext=(0, -10),  # Desplazamiento hacia abajo
                textcoords='offset points',
                ha='center',
                va='top',
                color='#64B5F6')

# Configurar los ejes y el título
ax.set_xlabel('Año')
ax.set_ylabel('Nivel de alfabetización (%)')
ax.set_title('Nivel de alfabetización en salud de los residentes de China de 2015 a 2021', fontsize=14, fontweight='bold')
ax.set_xticks(years)
ax.set_xticklabels(years)

# Agregar una leyenda
ax.legend(loc='upper left')

# Embellimiento: Ocultar los bordes superior y derecho
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()