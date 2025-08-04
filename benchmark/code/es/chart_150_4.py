import matplotlib.pyplot as plt
import numpy as np

# Organización de datos (en orden de métricas y niveles de satisfacción: Muy Satisfecho, Bastante Satisfecho, Promedio, Bastante Insatisfecho, Muy Insatisfecho)
metricas = [
    "Conveniencia del servicio", "Limpieza", "Experiencia de servicio", 
    "Coherencia con la información promocional", "Razonabilidad de precios", "Seguridad", "Actividades promocionales"
]
# Proporción (%) de cada nivel de satisfacción bajo cada métrica
datos = np.array([
    [57, 34, 7, 2, 0],   # Conveniencia del servicio
    [50, 41, 7, 2, 0],   # Limpieza
    [50, 40, 10, 0, 0],  # Experiencia de servicio
    [49, 40, 8, 3, 0],   # Coherencia con la información promocional
    [44, 44, 10, 4, 0],  # Razonabilidad de precios
    [51, 37, 10, 3, 0],  # Seguridad
    [49, 38, 11, 2, 0]   # Actividades promocionales
])
# Esquema de colores para cada nivel de satisfacción (similar a la figura original)
colores = ["#f8cecc", "#f4a460", "#ff8c00", "#cd5c5c", "#8b0000"]
# Etiquetas para los niveles de satisfacción
etiquetas = ["Muy Satisfecho", "Bastante Satisfecho", "Promedio", "Bastante Insatisfecho", "Muy Insatisfecho"]

x = np.arange(len(metricas))  # Coordenadas del eje x (una posición para cada métrica)
ancho_barra = 0.8  # Ancho de las barras para hacer los segmentos más compactos

fig, ax = plt.subplots(figsize=(12, 8))

# Dibujar el gráfico de barras apiladas segmentado
base = np.zeros(len(metricas))  # Posición de inicio para apilar
for i in range(5):
    ax.bar(
        x, 
        datos[:, i], 
        width=ancho_barra, 
        color=colores[i], 
        bottom=base, 
        label=etiquetas[i] if i == 0 else ""  # Mostrar la leyenda solo para el primer nivel para evitar repeticiones
    )
    base += datos[:, i]  # Actualizar la posición de inicio para el próximo segmento

ax.set_title('Encuesta 2023 sobre la satisfacción de los usuarios de servicios locales chinos en la experiencia de servicio en tienda', fontsize=14)
ax.set_ylabel('Proporción (%)')
ax.set_xticks(x)
ax.set_xticklabels(metricas, rotation=45, ha='right')
ax.legend(title='Nivel de satisfacción', loc='upper right')

# Agregar anotaciones numéricas (anotar solo "Muy Satisfecho" y "Bastante Satisfecho" como la figura original solo muestra estas dos partes; se puede expandir el bucle si se necesitan anotar todas)
for i in range(len(metricas)):
    # Anotar el valor de "Muy Satisfecho"
    ax.text(x[i], datos[i, 0]/2, f'{datos[i, 0]}%', ha='center', va='center', color='black')
    # Anotar el valor de "Bastante Satisfecho"
    ax.text(x[i], datos[i, 0] + datos[i, 1]/2, f'{datos[i, 1]}%', ha='center', va='center', color='black')
    # Si se necesitan anotar "Promedio", "Bastante Insatisfecho", "Muy Insatisfecho", se puede continuar agregando:
    # ax.text(x[i], datos[i, 0]+datos[i, 1]+datos[i, 2]/2, f'{datos[i, 2]}%', ...) 

plt.tight_layout()
plt.show()