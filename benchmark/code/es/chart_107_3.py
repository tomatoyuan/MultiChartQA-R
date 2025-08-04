import matplotlib.pyplot as plt
import numpy as np

# Deficiencias
deficiencias = ["Bajo costo - rendimiento del paquete", "Llamadas de ventas excesivas", "Servicio posventa deficiente",
                "Baja velocidad de red y limitación de ancho de banda", "Procedimientos comerciales complicados",
                "Altas tarifas de servicios con valor añadido", "Duración de llamada corta",
                "Cobertura de red irregular (señal débil o inestable en algunas áreas)", "Dificultad para cambiar de paquete"]
# Proporciones correspondientes (%)
proporciones = [44.75, 38.97, 34.58, 31.69, 27.30, 25.05, 20.66, 18.31, 9.31]

x = np.arange(len(deficiencias))  # Coordenadas del eje x

fig, ax = plt.subplots(figsize=(10, 6))
# Dibujar un gráfico de barras
barras = ax.bar(x, proporciones, color='orange')

# Agregar anotaciones numéricas
for i, proporcion in enumerate(proporciones):
    ax.text(i, proporcion + 1, f'{proporcion}', ha='center')

# Establecer las marcas y etiquetas del eje x, girar las etiquetas
ax.set_xticks(x)
ax.set_xticklabels(deficiencias, rotation=15, ha='right')
ax.set_ylabel('Proporción (%)')
ax.set_title('Deficiencias de los operadores de comunicaciones actuales percibidas por los usuarios chinos en 2025')

plt.tight_layout()
plt.show()