import matplotlib.pyplot as plt
import numpy as np

# Años
años = ["2010", "2014", "2018", "2020"]
# Número de estudiantes miopes en cada etapa educativa (en diez miles de personas), 
# los datos son consistentes con los niveles correspondientes en el gráfico y se pueden ajustar según sea necesario
datos = {
    "Estudiantes de primaria": [3107.13, 4458.78, 3722.13, 3818.24],
    "Estudiantes de secundaria": [3061.82, 3262.66, 3331.25, 3493.92],
    "Estudiantes de bachillerato": [3554.52, 3616.31, 3187.08, 3351.23]
}
# Configuración de colores para coincidir con el esquema de colores del gráfico
colores = ["#A4C639", "#a8dda8", "#87CEEB"]  

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar un gráfico de barras apiladas
base = np.zeros(len(años))
for i, (categoria, valores) in enumerate(datos.items()):
    ax.bar(años, valores, bottom=base, color=colores[i], label=categoria)
    # Agregar etiquetas de datos
    for x, y in zip(np.arange(len(años)), valores):
        ax.text(x, base[x] + y / 2, f'{y}', ha='center', va='center', color='black')
    base += np.array(valores)

# Establecer la etiqueta del eje y
ax.set_ylabel("Número de estudiantes miopes (en diez miles de personas)")
# Establecer el título
ax.set_title('Número total de estudiantes miopes de primaria, secundaria y bachillerato en China desde 2010 - 2020', fontsize=14, fontweight='bold')

# Agregar una leyenda
ax.legend()

# Mejora visual: Ocultar los bordes superior y derecho
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()