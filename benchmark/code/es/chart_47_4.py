import matplotlib.pyplot as plt
import numpy as np

# Datos (ejemplo, deben ser reemplazados con datos reales)
etiquetas = ['MAT2022', 'MAT2023', 'MAT2024']
taobao = [60, 55, 45]  # Proporción de Taotian (ejemplo)
jingdong = [10, 10, 10]  # Proporción de JD (ejemplo)
douyin = [30, 35, 45]  # Proporción de Douyin (ejemplo)

x = np.arange(len(etiquetas))  # Posiciones del eje x
ancho = 0.35  # Ancho de las barras

fig, ax = plt.subplots()
# Dibujar gráficos de barras para cada canal, notar el parámetro bottom para el efecto de apilamiento
rects_taobao = ax.bar(x, taobao, ancho, label='Taotian', color='#E67E22')
rects_jingdong = ax.bar(x, jingdong, ancho, bottom=taobao, label='JD', color='#E74C3C')
rects_douyin = ax.bar(x, douyin, ancho, bottom=np.add(taobao, jingdong), label='Douyin', color='#6DD9E0')

# Anotar la tasa de crecimiento
ax.annotate('+28%', 
            xy=(2, 100),  # Ajustar la posición xy a la parte superior de la tercera barra
            xytext=(0, 10),  # Agregar un desplazamiento para colocar el texto encima de la barra
            textcoords="offset points",
            ha='center', 
            va='bottom',
            fontsize=12,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", linestyle="--", alpha=0.8))

# Agregar etiquetas de valor a cada barra
def agregar_etiquetas(rects, valores_inferiores=None):
    for i, rect in enumerate(rects):
        altura = rect.get_height()
        if valores_inferiores is not None:
            inferior = valores_inferiores[i]
        else:
            inferior = 0
        # Calcular la posición del texto (centro de la barra)
        posicion_y = inferior + altura / 2
        # Agregar etiqueta de valor
        ax.text(
            rect.get_x() + rect.get_width() / 2,  # Coordenada x: centro de la barra
            posicion_y,                          # Coordenada y: centro de la barra
            f'{altura}%',                        # Valor a mostrar
            ha='center', va='center',            # Centrado horizontal y verticalmente
            color='white', fontweight='bold',    # Texto blanco, en negrita
            fontsize=9                           # Tamaño de fuente
        )

# Agregar etiquetas para cada canal
agregar_etiquetas(rects_taobao)
agregar_etiquetas(rects_jingdong, taobao)
agregar_etiquetas(rects_douyin, np.add(taobao, jingdong))

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(etiquetas)
# Establecer el rango del eje y
ax.set_ylim(0, 110)  # Aumentar el límite superior del eje y para evitar que el texto se oculte
# Agregar marcas de porcentaje al eje y
ax.set_yticks(np.arange(0, 101, 20))
ax.set_yticklabels([f'{i}%' for i in range(0, 101, 20)])
# Agregar leyenda y título
ax.legend()
ax.set_title('Proporción y Tasa de Crecimiento de Canales Online Core en el Negocio de Cuidado de la Piel')

plt.tight_layout()  # Optimizar el diseño
plt.show()