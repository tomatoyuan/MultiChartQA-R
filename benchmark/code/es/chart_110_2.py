import matplotlib.pyplot as plt
import numpy as np

# Escenarios de uso
escenarios = ["Escuchar antes de dormir", "Ir y volver del trabajo en transporte público", "Hacer tareas domésticas", "Hacer ejercicio o dar un paseo", "Cuidados personales por la mañana y la noche", 
             "Conducir", "Estudiar o trabajar", "Reuniones sociales", "Educación entre padres e hijos"]
# Proporciones correspondientes (%)
proporciones = [35.24, 31.91, 30.85, 28.99, 26.86, 24.07, 23.67, 22.61, 21.68]

x = np.arange(len(escenarios))  # Coordenadas del eje x

fig, ax = plt.subplots(figsize=(10, 6))
# Dibujar un gráfico de barras
barras = ax.bar(x, proporciones, color='orange')

# Agregar etiquetas numéricas
for i, proporcion in enumerate(proporciones):
    ax.text(i, proporcion + 1, f'{proporcion}', ha='center')

# Establecer las marcas y etiquetas del eje x, rotar las etiquetas
ax.set_xticks(x)
ax.set_xticklabels(escenarios, rotation=45, ha='right')
ax.set_ylabel('Proporción (%)')
ax.set_title('Escenarios de uso de aplicaciones de audiolibros por parte de usuarios chinos de audiolibros en 2025')

plt.tight_layout()
plt.show()