import matplotlib.pyplot as plt

# Datos
marcas = [
    "Noche UEFA Euro de NEC",
    "Noche de ebullición UEFA Euro de Xiaomi",
    "Noche UEFA Euro de Samsung",
    "Noche UEFA Euro de los un millón de propietarios de Tiguan",
    "Noche UEFA Euro de la nueva era de Junyue",
    "Noche juvenil super de descubrir buenos productos de Meizu",
    "Noche insomne del carnaval de mil personas UEFA Euro de Hisense",
    "Noche UEFA Euro de Didi Taxi",
    "Noche refrescante de la caravana de Chang'an Suzuki",
    "Noche UEFA Euro de la Embajada Bovard"
]
calificaciones = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Crear un lienzo y un sub - gráfico
fig, ax = plt.subplots(figsize=(10, 6))  # figsize puede ajustar el tamaño del gráfico

# Dibujar un gráfico de barras horizontales
ax.barh(marcas[::-1], calificaciones[::-1], color='royalblue')

# Establecer el título y las etiquetas de los ejes
ax.set_title('Calificaciones estrelladas de las actividades de marketing fuera de\n línea de las marcas compitiendo por la "Noche UEFA Euro"', fontsize=14, fontweight='bold')
ax.set_xlabel('Calificación estrellada', fontsize=12)
ax.set_ylabel('Actividades de la marca', fontsize=12)

# Establecer las marcas del eje x (de 0 a 10 según las calificaciones estrelladas)
ax.set_xticks(range(0, 11))

# Mostrar el gráfico
plt.tight_layout()  # Ajustar el diseño para evitar la superposición de etiquetas
plt.show()