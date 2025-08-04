import matplotlib.pyplot as plt
import numpy as np

# Nombres de las categorías
categorias = ["Hidrogel de silicona", "Hidrogel", "Lentes de gas permeable rígidos", "Material mixto", "No lo sé"]
# Datos de proporción de cada categoría correspondientes a diferentes tipos de lentes de contacto
datos = np.array([
    [20, 20, 16],
    [18, 18, 12],
    [12, 10, 12],
    [6, 6, 6],
    [8, 8, 4]
])

# Calcular el valor total de cada categoría
valores_totales = datos.sum(axis=1)

# Ordenar según el valor total (en orden descendente)
indices_ordenados = np.argsort(valores_totales)[::-1]

# Reordenar categorías y datos
categorias = [categorias[i] for i in indices_ordenados]
datos = datos[indices_ordenados]

# Transponer los datos para que cada columna corresponda a un tipo de lente de contacto
datos = datos.T

# Etiquetas y colores correspondientes para diferentes tipos de lentes de contacto
etiquetas = ["Lentes de contacto transparentes", "Lentes de contacto coloreados", "Lentes de contacto rígidos"]
colores = ["#4CAF50", "#FF9800", "#F44336"]  

# Crear un gráfico
fig, ax = plt.subplots(figsize=(10, 6))  # Aumentar el ancho adecuadamente para acomodar las etiquetas

# Dibujar un gráfico de barras apiladas
parte_inferior = np.zeros(len(categorias))
for i in range(len(etiquetas)):
    barras = ax.barh(categorias, datos[i], left=parte_inferior, color=colores[i], label=etiquetas[i])
    
    # Agregar etiquetas de datos a cada barra
    for barra, valor in zip(barras, datos[i]):
        if valor > 0:  # Mostrar solo valores no nulos
            ax.text(
                barra.get_x() + barra.get_width()/2,  # Posición x: centro de la barra
                barra.get_y() + barra.get_height()/2, # Posición y: centro de la barra
                f"{valor}%",                      # Mostrar el valor y el signo de porcentaje
                ha='center', va='center',         # Centrado horizontal y verticalmente
                color='white', fontweight='bold', # Texto blanco, en negrita
                fontsize=9                        # Tamaño de fuente
            )
    
    parte_inferior += datos[i]

# Agregar texto de anotación (ajustar la posición para evitar cubrir las etiquetas)
texto_anotacion = "El hidrogel de silicona es principalmente para usuarios intensivos\nque usan lentes de contacto de 8 a 12 horas\n(TGI>100)"
ax.text(0.7, 0.85, texto_anotacion, transform=ax.transAxes,
        bbox=dict(facecolor='orange', alpha=0.8), fontsize=10)

# Establecer atributos del gráfico
ax.yaxis.set_label_position("right")
ax.set_ylabel("Tipos de lentes de contacto", fontsize=12)
ax.set_xlabel("Proporción (%)", fontsize=12)
ax.set_title("Distribución por tipo de usuarios de diferentes materiales de lentes de contacto", fontsize=14, pad=15)
ax.legend(loc='center right')  # Ajustar la posición de la leyenda
plt.tight_layout()
plt.show()