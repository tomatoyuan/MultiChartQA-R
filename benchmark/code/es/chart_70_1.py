import matplotlib.pyplot as plt
import numpy as np

# Direcciones técnicas
direcciones_tecnicas = ["Inteligencia Artificial", "Big Data", "Pruebas", "Operación/Soporte Técnico", "Desarrollo Backend", "Desarrollo Frontend", "Desarrollo Móvil"]
# Datos de porcentaje correspondientes
datos = np.array([87.7, 44.2, 38.5, 38.0, 35.1, 22.2, 21.1])

# Tamaño de las burbujas (simular el área percibida con el cuadrado de los datos)
tamanos = datos ** 2.2  # Ajusta el exponente para optimizar la percepción visual
colores = plt.cm.plasma(datos / max(datos))  # Utilizar el mapa de colores plasma para mejorar el sentido del diseño

# Crear un lienzo
fig, ax = plt.subplots(figsize=(10, 6))

# Configuración de los ejes
x = np.arange(len(direcciones_tecnicas))

# Dibujar un gráfico de burbujas
scatter = ax.scatter(x, [1]*len(x), s=tamanos, c=colores, alpha=0.8, edgecolors='white', linewidths=1.5)

# Agregar anotaciones numéricas
for i in range(len(direcciones_tecnicas)):
    ax.text(x[i], 1.02, f"{datos[i]}%", ha='center', va='bottom', fontsize=10, fontweight='bold')

# Establecer las etiquetas del eje x como direcciones técnicas
ax.set_xticks(x)
ax.set_xticklabels(direcciones_tecnicas, rotation=15, ha="right", fontsize=11)
ax.set_yticks([])

# Agregar un título
ax.set_title("Cambio interanual en la demanda de contratación para las principales direcciones técnicas de Internet en la primavera de 2022", fontsize=14, fontweight="bold", pad=20)

# Eliminar el borde
for spine in ["top", "right", "left", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()