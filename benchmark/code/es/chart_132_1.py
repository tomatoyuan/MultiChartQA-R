import matplotlib.pyplot as plt
import numpy as np

# Datos
categorias = ["Ingeniería", "Ciencia", "Economía", "Educación", "Administración", "Medicina", "Literatura", 
              "Historia", "Derecho", "Arte", "Agricultura", "Filosofía", "Otros"]
proporciones = [26.75, 25.81, 23.63, 23.48, 23.32, 19.75, 16.69, 
               15.86, 15.71, 12.59, 11.50, 11.35, 0.31]
# Proporciones de humanidades y ciencias
humanidades = 43.5
ciencias = 56.5

fig, (ax_izquierdo, ax_derecho) = plt.subplots(1, 2, figsize=(16, 8), gridspec_kw={'width_ratios': [1, 3]})

# Izquierda: Proporciones de humanidades y ciencias (texto + visualización simple)
ax_izquierdo.text(0.5, 0.6, f'Humanidades {humanidades}%', ha='center', va='center', fontsize=16, color='orange')
ax_izquierdo.text(0.5, 0.4, f'Ciencias {ciencias}%', ha='center', va='center', fontsize=16, color='blue')
ax_izquierdo.axis('off')

# Derecha: Gráfico de barras horizontales de preferencias por cada materia/carrera
y = np.arange(len(categorias))
ax_derecho.barh(y, proporciones, color='orange')
ax_derecho.set_yticks(y)
ax_derecho.set_yticklabels(categorias)
ax_derecho.set_xlabel('Proporción (%)')

# Agregar etiquetas de valor para cada proporción de materia/carrera
for i, prop in enumerate(proporciones):
    ax_derecho.text(prop + 0.5, i, f'{prop}%', va='center')

ax_derecho.set_title('Preferencias de los candidatos al examen de ingreso a la universidad en China por materias y carreras')

plt.tight_layout()
plt.show()