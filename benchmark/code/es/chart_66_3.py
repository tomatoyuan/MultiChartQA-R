import matplotlib.pyplot as plt
import numpy as np

# Categorías de datos
tipos_de_usuarios = ["Usuarios de pomada", "No usuarios de pomada"]
# Etiquetas de grupos de edad
etiquetas_edad = ["Nacidos después de 1995", "Nacidos después de 1990", "Nacidos después de 1985", "Nacidos antes de 1985"]
# Corregir la estructura de datos: cada sub - lista representa la distribución de un tipo de usuario en los grupos de edad
datos = [
    [36.5, 32.5, 18.9, 12.2],  # Usuarios de pomada
    [33.1, 29.0, 21.6, 16.4]   # No usuarios de pomada
]
# Configuración de colores
colores = ["#A4C639", "#8DB328", "#7EA11E", "#668718"]

# Crear un lienzo y un sub - gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras apiladas
x = np.arange(len(tipos_de_usuarios))
ancho_barra = 0.6

# Dibujar barras apiladas para cada tipo de usuario por separado
for i, datos_usuario in enumerate(datos):
    base = 0
    for j, valor in enumerate(datos_usuario):
        ax.bar(
            x[i], valor, ancho_barra, bottom=base, 
            color=colores[j], label=etiquetas_edad[j] if i == 0 else "",  # Agregar leyenda solo en el primer dibujo
            edgecolor="white"
        )
        # Agregar etiquetas de datos en el centro de las barras
        ax.text(
            x[i], base + valor/2, f"{valor}%",
            ha='center', va='center', color='white', fontweight='bold'
        )
        base += valor

# Configurar los ejes y el título
ax.set_xticks(x)
ax.set_xticklabels(tipos_de_usuarios, fontsize=12)
ax.set_ylabel('Porcentaje (%)', fontsize=12)
ax.set_title('Distribución de edad de dueños de mascotas (por tipo de usuario)', fontsize=16, pad=15)

# Configurar el rango del eje y
ax.set_ylim(0, 100)

# Agregar una leyenda (eliminar duplicados)
handles, labels = ax.get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys(), loc='upper right', bbox_to_anchor=(1.2, 1))

# Hacer que el gráfico sea más atractivo
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.show()