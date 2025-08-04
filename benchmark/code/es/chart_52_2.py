import matplotlib.pyplot as plt

# Definición de datos
etiquetas = ["Perseguir la innovación académica", "Participar activamente en proyectos de investigación científica y acumular experiencia académica", "Ser capaz de producir resultados de investigación personales de forma independiente", "No tomar la iniciativa, solo hacerlo cuando la escuela lo requiera"]
tamaños = [33.8, 31.0, 27.3, 7.8]  # Datos simulados aproximadamente, se pueden ajustar según la situación real
# Configuración de colores, lo más cercano posible a la imagen original
colores = ["greenyellow", "green", "limegreen", "lightgray"]

# Crear un gráfico circular
fig, ax = plt.subplots(figsize=(8, 6))
porciones, textos, textos_automaticos = ax.pie(tamaños, labels=etiquetas, autopct='%1.1f%%', startangle=140, colors=colores,
                                  textprops={'fontsize': 12}, wedgeprops={'linewidth': 1, 'edgecolor': 'white'})

# Mejorar el color del texto de la anotación
for texto_automatico in textos_automaticos:
    texto_automatico.set_color('white')
    texto_automatico.set_weight('bold')

# Establecer el título
ax.set_title("Requisitos personales de los estudiantes universitarios en aspectos académicos", fontsize=16, fontweight='bold', y=1.05)

# Ajustar la posición de la leyenda (opcional, se puede ajustar si es necesario)
ax.legend(loc='upper right', bbox_to_anchor=(2.5, 0.8), fontsize=12)

# Ajustar el diseño
plt.tight_layout()

plt.show()