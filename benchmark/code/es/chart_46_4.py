import matplotlib.pyplot as plt
import numpy as np

# Organización de datos
categorias = ['Funciones Básicas', 'Funciones Avanzadas', 'Experiencia Multidimensional']
sub_categorias = {
    'Funciones Básicas': ['Comodidad de Asiento', 'Calidad y Seguridad', 'Durabilidad del Producto', 'Soporte de Funciones'],
    'Funciones Avanzadas': ['Facilidad de Operación', 'Ajustabilidad', 'Amigabilidad Ambiental'],
    'Experiencia Multidimensional': ['Interacción Inteligente', 'Valor Emocional y Función de Curación', 'Diseño Estético', 'Personalización']
}
valores = {
    'Funciones Básicas': [62, 56, 47, 43],
    'Funciones Avanzadas': [38, 33, 28],
    'Experiencia Multidimensional': [25, 23, 22, 17]
}

# Se utiliza para establecer la posición de cada grupo de barras
posiciones_x = {}
ancho_barra = 0.25
espaciado = 0.5  # Espaciado entre diferentes categorías principales

# Calcular dinámicamente la posición x de cada categoría principal
x_actual = 0
for cat in categorias:
    n_sub = len(sub_categorias[cat])
    posiciones_x[cat] = np.arange(x_actual, x_actual + n_sub)
    x_actual += n_sub + espaciado

# Crear una figura
fig, ax = plt.subplots(figsize=(14, 8))  # Aumentar la altura de la figura para acomodar las etiquetas

# Dibujar cada grupo de barras y agregar etiquetas de porcentaje
for i, cat in enumerate(categorias):
    barras = ax.bar(posiciones_x[cat], valores[cat], width=ancho_barra, label=cat)

    # Agregar etiquetas de porcentaje a cada barra
    for barra, valor in zip(barras, valores[cat]):
        ax.text(barra.get_x() + barra.get_width()/2, barra.get_height() + 0.8,
                f'{valor}%', ha='center', va='bottom', fontsize=9, fontweight='bold')

    # Agregar etiquetas de subcategoría para cada categoría principal (ajustar la posición)
    for j, pos in enumerate(posiciones_x[cat]):
        ax.text(pos, -3.5, sub_categorias[cat][j], ha='center', rotation=45, fontsize=9)

# Establecer las marcas del eje x (aquí solo necesitamos marcar la posición inicial de cada categoría principal)
ax.set_xticks([posiciones_x[cat][0] for cat in categorias])
ax.set_xticklabels(categorias)

# Agregar título, leyenda y etiquetas
ax.set_title('Demandas de los Consumidores para el Consumo de Asientos', fontsize=14)
ax.set_xlabel('Tipos de Demanda', fontsize=12)
ax.set_ylabel('Porcentaje (%)', fontsize=12)
ax.legend()

# Establecer el rango del eje y para que las etiquetas negativas y numéricas sean visibles
ax.set_ylim(bottom=-5, top=75)  # Ajustar el límite superior del eje y para asegurarse de que las etiquetas no estén fuera de rango

# Agregar líneas de cuadrícula para facilitar la lectura de los valores
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()