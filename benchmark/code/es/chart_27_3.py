import matplotlib.pyplot as plt
import numpy as np

# Nombres de las telenovelas
etiquetas = ["Procuración del Estado", "Poder Absoluto", "Soy el Maestro de las Altibajos", "Cadre del Estado"]
# Datos del índice de búsqueda
valores = [526.24, 183.28, 128.79, 111.05]
# Se utiliza para posicionar cada termómetro en el eje x
posiciones_x = np.arange(len(etiquetas))  

# Crear un lienzo y subgráficos
fig, ejes = plt.subplots(1, len(etiquetas), figsize=(12, 5), sharey=True)

# La escala máxima del termómetro (se puede ajustar según los datos, se establece en 600 aquí para facilitar la visualización)
max_temp = 600  
for i in range(len(etiquetas)):
    ax = ejes[i]
    # Dibujar el marco exterior del termómetro (simulado por un rectángulo, aquí se simplifica, también se pueden usar líneas verticales y formas personalizadas más complejas)
    # Primero dibujar el "tubo de vidrio" del termómetro, usando un fondo de relleno blanco para la simulación
    ax.bar(0, max_temp, width=0.5, color='white', edgecolor='black')
    # Dibujar la parte roja del "mercurio", con la altura igual al valor de los datos correspondientes
    ax.bar(0, valores[i], width=0.5, color='red')
    # Establecer el rango del eje y
    ax.set_ylim(0, max_temp)
    # Ocultar las marcas del eje x
    ax.set_xticks([])  
    # Agregar el nombre de la telenovela como título
    ax.set_title(etiquetas[i], y=-0.2)  
    # Mostrar el valor porcentual encima del termómetro
    ax.text(0, valores[i] + 10, f"{valores[i]}", ha='center')  

# Título general
fig.suptitle("Comparación de los índices de búsqueda de las telenovelas populares después del estreno de En nombre del Pueblo", fontsize=16, y=1.05)
# Ajustar el diseño
plt.tight_layout()
# Mostrar el gráfico
plt.show()