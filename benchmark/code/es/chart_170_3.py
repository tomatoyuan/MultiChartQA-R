import matplotlib.pyplot as plt

# Años y datos de sesiones de consulta promedio
años = [2020, 2021, 2022, 2023]
sesiones_promedio = [10.8, 11.8, 12.8, 12.7]

# Degradado de colores: de naranja a rosa
colores = ['#F6C143', '#F6A844', '#F4767E', '#EF6D95']

# Crear la gráfica
plt.figure(figsize=(8, 5))
for i in range(len(años)-1):
    plt.plot([años[i], años[i+1]], [sesiones_promedio[i], sesiones_promedio[i+1]], color=colores[i], linewidth=2.5)
plt.scatter(años, sesiones_promedio, color=colores, s=100, zorder=5)

# Etiquetar los valores
for x, y in zip(años, sesiones_promedio):
    plt.text(x, y + 0.3, f'{y}', ha='center', fontsize=12, fontweight='bold')

# Configuración de estilo
plt.title("Número promedio de sesiones de consulta de los \nvisitantes de Simple Psychology entre 2020 y 2023", fontsize=14, fontweight='bold', color='#4B3083')
plt.xticks(años)
plt.yticks(range(0, 16, 5))
plt.ylim(0, 15)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

# Mostrar la gráfica
plt.show()