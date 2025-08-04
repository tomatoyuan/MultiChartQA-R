import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime

# Puntos de datos clave originales
fechas = [
    datetime.datetime(2024, 8, 16),
    datetime.datetime(2024, 8, 30),
    datetime.datetime(2024, 9, 15),
    datetime.datetime(2024, 9, 25),  # Punto de aumento
    datetime.datetime(2024, 10, 15),
    datetime.datetime(2024, 11, 4),
    datetime.datetime(2024, 11, 24),
    datetime.datetime(2024, 12, 11)
]

indice_ai = [0, -5, -3, 23, 20, 36, 35, 42.3]
indice_sh = [0, 1, -2, 17, 18, 12, 16, 19.3]

# Convertir fechas a valores numéricos
x = mdates.date2num(fechas)

# Generar puntos de fecha más densos (datos diarios)
fecha_inicio = fechas[0]
fecha_fin = fechas[-1]
delta = fecha_fin - fecha_inicio
todas_fechas = [fecha_inicio + datetime.timedelta(days=i) for i in range(delta.days + 1)]
todos_x = mdates.date2num(todas_fechas)

# Función de generación de volatilidad del mercado (volatilidad uniforme en toda la curva)
def generar_volatilidad_mercado(x, y, todos_x, volatilidad=0.03, persistencia=0.7):
    """
    Generar datos del mercado con volatilidad uniforme en toda la curva
    
    Parámetros:
    x: coordenadas x de los puntos de datos originales
    y: coordenadas y de los puntos de datos originales
    todos_x: todas las coordenadas x donde se deben generar datos
    volatilidad: Coeficiente de intensidad de la volatilidad
    persistencia: Persistencia de la dirección de la volatilidad (entre 0 y 1)
    """
    # Realizar interpolación spline cúbica en los datos originales para obtener la curva base
    from scipy.interpolate import make_interp_spline
    spl = make_interp_spline(x, y, k=3)
    curva_base = spl(todos_x)
    
    # Calcular la amplitud de la volatilidad diaria (como porcentaje de la curva base)
    volatilidad_diaria = np.abs(curva_base) * volatilidad
    
    # Generar ruido aleatorio de volatilidad con persistencia de dirección
    n_puntos = len(todos_x)
    ruido = np.zeros(n_puntos)
    direccion = 1  # Dirección inicial
    
    for i in range(1, n_puntos):
        # Cambiar la dirección con una probabilidad de (1 - persistencia)
        if np.random.random() > persistencia:
            direccion = -direccion
        
        # Generar el valor de volatilidad en este punto (utilizando la distribución de Laplace para aumentar los valores extremos)
        ruido[i] = np.random.laplace(0, volatilidad_diaria[i]) * direccion
    
    # Acumular la volatilidad para formar un paseo aleatorio
    ruido_acumulado = np.cumsum(ruido)
    
    # Asegurarse de que los puntos finales coincidan con los datos originales
    # Calcular el desplazamiento necesario para ajustar de modo que el último punto vuelva al valor original
    desplazamiento = y[-1] - (curva_base[-1] + ruido_acumulado[-1])
    ruido_ajustado = ruido_acumulado + desplazamiento * np.linspace(0, 1, n_puntos)
    
    # Curva final de volatilidad = curva base + volatilidad ajustada
    curva_final = curva_base + ruido_ajustado
    
    return curva_final

# Generar datos con volatilidad uniforme en toda la curva
ai_volatil = generar_volatilidad_mercado(x, indice_ai, todos_x, volatilidad=0.04, persistencia=0.6)
sh_volatil = generar_volatilidad_mercado(x, indice_sh, todos_x, volatilidad=0.025, persistencia=0.7)

# Crear el gráfico
fig, ax = plt.subplots(figsize=(16, 9))

# Trazar las curvas de volatilidad
line_ai, = ax.plot(todos_x, ai_volatil, label='Índice AI Glass (886085)', 
                   color='#32CD32', linewidth=1.6, alpha=0.9)
line_sh, = ax.plot(todos_x, sh_volatil, label='Índice Compositivo de Shanghái (000001)', 
                   color='#1E90FF', linewidth=1.6, alpha=0.9, linestyle='--')

# Etiquetar los cambios de precio finales
ax.text(todos_x[-1], ai_volatil[-1], f'{ai_volatil[-1]:.1f}%', ha='left', va='bottom', 
        color='#32CD32', fontweight='bold', fontsize=12, bbox=dict(facecolor='white', alpha=0.7))
ax.text(todos_x[-1], sh_volatil[-1], f'{sh_volatil[-1]:.1f}%', ha='left', va='bottom', 
        color='#1E90FF', fontweight='bold', fontsize=12, bbox=dict(facecolor='white', alpha=0.7))

# Establecer el eje x en formato de fecha y controlar la densidad de visualización
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))  # Mostrar una fecha por semana
plt.xticks(rotation=45, fontsize=10)

# Establecer el título y la leyenda
ax.set_title('Comparación de los cambios acumulados de precio entre el Índice AI Glass y el Índice Compositivo de Shanghái\n(2024/8/16 - 2024/12/11)', 
             fontsize=17, pad=15, fontweight='bold')
ax.legend(loc='upper left', frameon=True, framealpha=0.9, fontsize=12)

# Establecer el eje y en formato de porcentaje
ax.set_ylabel('Cambio acumulado de precio (%)', fontsize=13)
ax.set_ylim(-30, 70)  # Ampliar aún más el rango del eje y para acomodar una mayor volatilidad

# Mostrar la cuadrícula
ax.grid(True, linestyle='--', alpha=0.6, which='both')

# Resaltar la línea vertical para la fecha clave
ax.axvline(x[3], color='gray', linestyle='-.', alpha=0.5)  # 2024/9/25

# Agregar colores de fondo para distinguir diferentes períodos de tiempo
for i in range(len(x)-1):
    if i == 3:  # El área después del punto de aumento
        ax.axvspan(x[i], x[i+1], color='lightgreen', alpha=0.1)
    else:
        ax.axvspan(x[i], x[i+1], color='white' if i%2==0 else 'lightgray', alpha=0.1)

# Embelezar el borde del gráfico
for spine in ax.spines.values():
    spine.set_color('gray')
    spine.set_linewidth(1)

# Agregar una nota sobre la volatilidad
ax.text(0.02, 0.02, 'Nota: La volatilidad se aplica uniformemente en toda la curva, coherente con las características de volatilidad continua del mercado', 
        transform=ax.transAxes, fontsize=10, color='gray')

# Ajustar el diseño
plt.tight_layout()
plt.show()