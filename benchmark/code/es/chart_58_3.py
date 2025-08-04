import matplotlib.pyplot as plt
import numpy as np

# Datos
semanas = ["Semana 1, Abril", "Semana 2, Abril", "Semana 3, Abril", "Semana 4, Abril", "Semana 5, Abril"]
datos_2024 = [3500.2, 3726.2, 3616.5, 3628.3, 3598.8]  # Datos simulados, se pueden reemplazar con valores reales
datos_2025 = [4039.3, 4230.8, 4409.0, 4232.3, 3966.2]  # Datos simulados, se pueden reemplazar con valores reales

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 5))

# Dibujar las líneas
ax.plot(semanas, datos_2025, color="#a5d65d", marker="o", label="Año 2025", linewidth=2)
ax.plot(semanas, datos_2024, color="#4bb7e6", marker="o", label="Año 2024", linewidth=2)

# Agregar etiquetas de datos
for x, y in zip(semanas, datos_2025):
    ax.text(x, y + 20, f'{y}', ha='center', va='bottom', fontsize=9)
for x, y in zip(semanas, datos_2024):
    ax.text(x, y + 20, f'{y}', ha='center', va='bottom', fontsize=9)

# Mejorar la configuración
ax.set_title("UserTracker - Comparación de tendencias de aplicaciones de rendimiento cultural desde el Día de las Momias hasta el Día del Trabajo en 2024 y 2025\nUnidad: Número de dispositivos de usuarios activos semanales (en unidades de diez mil)", fontsize=12, fontweight='bold')
ax.legend()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()