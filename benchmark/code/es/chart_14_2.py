import matplotlib.pyplot as plt
import numpy as np

# Nombres de las provincias y datos simulados (se pueden reemplazar con datos reales)
provincias = ['Guangdong', 'Zhejiang', 'Shandong', 'Jiangsu', 'Beijing', 'Shanghai', 'Fujian', 'Henan', 'Sichuan', 'Hebei']
porcentajes_azules = [100, 95, 80, 75, 60, 55, 50, 45, 40, 30]
porcentajes_blancos = [100 - p for p in porcentajes_azules]

# Ordenar los datos (en orden ascendente)
datos_ordenados = sorted(zip(porcentajes_azules, porcentajes_blancos, provincias))
porcentajes_azules, porcentajes_blancos, provincias = zip(*datos_ordenados)

# Crear un lienzo
fig, ax = plt.subplots(figsize=(10, 6))

# Establecer colores degradados (de azul claro a azul oscuro)
colores = plt.cm.Blues(np.linspace(0.5, 0.9, len(provincias)))

# Dibujar un diagrama de barras apiladas horizontales decorado
bar_blancas = ax.barh(provincias, porcentajes_blancos, color='white', edgecolor='lightgray', linewidth=0.8)
bar_azules = ax.barh(provincias, porcentajes_azules, left=porcentajes_blancos, color=colores, edgecolor='gray', linewidth=0.8)

# Agregar etiquetas de datos
for i, (azul, blanco) in enumerate(zip(porcentajes_azules, porcentajes_blancos)):
    # Agregar etiquetas de porcentaje en el centro del área azul
    ax.text(blanco + azul/2, i, f'{azul}', ha='center', va='center', 
            color='white' if azul > 40 else 'navy', fontweight='bold')

# Establecer el título y el texto explicativo inferior
ax.set_title('Atención de cada provincia a los aires acondicionados', fontsize=14, pad=15)

# Establecer líneas de cuadrícula
ax.grid(axis='x', linestyle='--', alpha=0.3)

# Ocultar los ejes superior, derecho e inferior
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Ajustar los estilos de las marcas y las etiquetas
ax.tick_params(axis='y', which='major', labelsize=10, pad=10)
ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)

# Agregar una línea de referencia izquierda
ax.axvline(x=0, color='gray', linestyle='-', alpha=0.5)

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()