import matplotlib.pyplot as plt
import numpy as np

# Fechas (eje x, convertidas a números para la representación gráfica, se mostrarán las fechas originales)
dates = np.arange(1, 29, 2)
date_labels = ['1 feb', '3 feb', '5 feb', '7 feb', '9 feb', '11 feb', '13 feb', '15 feb', '17 feb', '19 feb', '21 feb', '23 feb', '25 feb', '27 feb']

# Atención de búsqueda de varios tipos de leche en polvo (eje y)
children_milk = [1000, 1200, 1300, 1500, 1400, 1450, 1420, 1430, 1400, 4000, 1300, 1200, 1100, 1000]
pregnant_milk = [15000, 20000, 25000, 30000, 28000, 28500, 29000, 29500, 28000, 25000, 30000, 25000, 40000, 18000]
infant_milk = [2000, 2200, 2300, 2400, 2350, 2400, 2420, 2430, 2400, 2500, 2300, 2200, 2100, 2000]
student_milk = [2500, 2600, 2700, 2800, 2750, 2800, 2820, 2830, 2800, 2900, 2700, 2600, 2500, 2400]

# Creación de la gráfica
plt.figure(figsize=(14, 8))

# Dibujar gráficas de líneas
children_line, = plt.plot(dates, children_milk, color='orange', label='Leche en polvo para niños', linewidth=2)
infant_line, = plt.plot(dates, infant_milk, color='blue', label='Leche en polvo para bebés', linewidth=2)
pregnant_line, = plt.plot(dates, pregnant_milk, color='pink', label='Leche en polvo para mujeres embarazadas', linewidth=2)
student_line, = plt.plot(dates, student_milk, color='lightblue', label='Leche en polvo para estudiantes', linewidth=2)

# Establecer las marcas y etiquetas del eje x
plt.xticks(dates, date_labels, rotation=45)

# Establecer el título y las etiquetas de los ejes
plt.title('Tendencias de atención de búsqueda por categoría en febrero', fontsize=16)
plt.xlabel('Fecha', fontsize=12)
plt.ylabel('Atención de búsqueda', fontsize=12)

# Añadir líneas de cuadrícula
plt.grid(True, linestyle='--', alpha=0.7)

# Añadir anotaciones inteligentes a los puntos de datos para evitar superposiciones
def add_smart_annotations(x, y, color, label, is_pregnant=False):
    """Añadir anotaciones inteligentes a los puntos de datos para evitar superposiciones"""
    # Recopilar todas las posiciones de las anotaciones colocadas
    placed_annotations = []

    for i, (date, value) in enumerate(zip(x, y)):
        # Formatear el valor con separadores de miles
        value_str = f"{value:,}"

        # Desplazamiento base
        base_offset = 15

        # Establecer un desplazamiento base mayor para la leche en polvo de mujeres embarazadas
        if is_pregnant:
            base_offset = 30

        # Comprobar si se superpone con las anotaciones existentes
        overlaps = True
        attempts = 0
        max_attempts = 8
        offset = base_offset

        while overlaps and attempts < max_attempts:
            # Probar diferentes ángulos y distancias para colocar la anotación
            angle = (attempts % 4) * 90  # 0, 90, 180, 270 grados
            distance = base_offset + (attempts // 4) * 10  # Aumentar la distancia cada dos intentos

            # Calcular el desplazamiento
            if angle == 0:  # Derecha
                xytext = (distance, 0)
                ha = 'left'
                va = 'center'
            elif angle == 90:  # Arriba
                xytext = (0, distance)
                ha = 'center'
                va = 'bottom'
            elif angle == 180:  # Izquierda
                xytext = (-distance, 0)
                ha = 'right'
                va = 'center'
            else:  # Abajo
                xytext = (0, -distance)
                ha = 'center'
                va = 'top'

            # Comprobar la superposición
            overlaps = False
            for (x_annot, y_annot) in placed_annotations:
                # Calcular la distancia
                dist = np.sqrt((date - x_annot)**2 + (value - y_annot)**2)
                # Considerar que hay superposición si la distancia es demasiado corta
                if dist < 30:  # El umbral se puede ajustar
                    overlaps = True
                    break

            if not overlaps:
                # No hay superposición, registrar esta posición
                placed_annotations.append((date + xytext[0]/10, value + xytext[1]/10))
                break

            attempts += 1

        # Si no se puede encontrar una posición sin superposición después de varios intentos, usar la posición predeterminada
        if overlaps:
            xytext = (0, base_offset)
            ha = 'center'
            va = 'bottom'

        # Añadir anotación
        plt.annotate(value_str,
                     (date, value),
                     textcoords="offset points",
                     xytext=xytext,
                     ha=ha,
                     va=va,
                     fontsize=8,
                     color=color,
                     bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=color, alpha=0.8))


# Añadir anotaciones inteligentes para varios tipos de leche en polvo
add_smart_annotations(dates, children_milk, 'orange', 'Leche en polvo para niños')
add_smart_annotations(dates, infant_milk, 'blue', 'Leche en polvo para bebés')
add_smart_annotations(dates, pregnant_milk, 'pink', 'Leche en polvo para mujeres embarazadas', True)
add_smart_annotations(dates, student_milk, 'lightblue', 'Leche en polvo para estudiantes')

# Añadir leyenda
plt.legend(fontsize=10, loc='upper left')

# Añadir descripción de la fuente de datos
plt.figtext(0.1, 0.01, 'Fuente de datos: Datos ficticios solo para demostración', ha="left", fontsize=9, bbox={"facecolor": "white", "alpha": 0.5, "pad": 5})

# Optimizar el diseño
plt.tight_layout()

# Mostrar la gráfica
plt.show()