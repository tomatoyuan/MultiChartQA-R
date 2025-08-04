import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# 1. Simular datos originales (fechas, tamaño de la población)
fechas = np.array(['1-10', '1-13', '1-16', '1-19', '1-22', '1-25', '1-28',
                  '1-31', '2-3', '2-6', '2-9', '2-12', '2-15', '2-18', '2-21'])

# Datos de estudiantes que se van a casa (picos el 1-19 y 1-25, mitad del pico el 1-22, 0 el 1-10 y 2-21)
estudiantes_van = np.array([0, 30, 60, 50, 30, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0])

# Datos de trabajadores migrantes que se van a casa (pico alrededor del 1-25)
trabajadores_migrantes_van = np.array([0, 0, 0, 30, 80, 85, 0, 0, 0, 0, 0, 0, 0, 0, 0])

# Datos de trabajadores de oficina que se van a casa (pico alrededor del 1-22)
trabajadores_oficina_van = np.array([0, 0, 0, 0, 70, 75, 0, 0, 0, 0, 0, 0, 0, 0, 0])

# Datos de regreso (distribución uniforme en febrero)
estudiantes_regresan = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 60, 70, 75, 70])
trabajadores_migrantes_regresan = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 60, 65, 64, 45, 0, 0])
trabajadores_oficina_regresan = np.array([0, 0, 0, 0, 0, 0, 0, 0, 75, 70, 0, 0, 0, 0, 0])

# 2. Crear un eje de tiempo uniformemente distribuido
x_uniforme = np.arange(len(fechas))  # Eje numérico uniformemente distribuido

# 3. Procesamiento de interpolación y suavizado
def suavizar_curva(y):
    x_nuevo = np.linspace(x_uniforme.min(), x_uniforme.max(), 300)
    spline = make_interp_spline(x_uniforme, y, k = 3)
    return x_nuevo, spline(x_nuevo)

# Proceso de suavizado
x_suave, estudiantes_van_suave = suavizar_curva(estudiantes_van)
_, trabajadores_migrantes_van_suave = suavizar_curva(trabajadores_migrantes_van)
_, trabajadores_oficina_van_suave = suavizar_curva(trabajadores_oficina_van)

_, estudiantes_regresan_suave = suavizar_curva(estudiantes_regresan)
_, trabajadores_migrantes_regresan_suave = suavizar_curva(trabajadores_migrantes_regresan)
_, trabajadores_oficina_regresan_suave = suavizar_curva(trabajadores_oficina_regresan)

# 4. Dibujar el gráfico de curvas
fig, ax = plt.subplots(figsize=(14, 7), facecolor='#f8f9fa')
ax.set_facecolor('#f8f9fa')

# Curva y relleno de la fase de ida
estudiantes_van_linea, = ax.plot(x_suave, estudiantes_van_suave, color='#A8D8EA', linewidth=2.5, label='Estudiantes (Yendo a Casa)')
ax.fill_between(x_suave, estudiantes_van_suave, color='#A8D8EA', alpha=0.3)  # Rellenar la curva de estudiantes que se van a casa

trabajadores_migrantes_van_linea, = ax.plot(x_suave, trabajadores_migrantes_van_suave, color='#AA96DA', linewidth=2.5, label='Trabajadores Migrantes (Yendo a Casa)')
ax.fill_between(x_suave, trabajadores_migrantes_van_suave, color='#AA96DA', alpha=0.3)  # Rellenar la curva de trabajadores migrantes que se van a casa

trabajadores_oficina_van_linea, = ax.plot(x_suave, trabajadores_oficina_van_suave, color='#FCBAD3', linewidth=2.5, label='Trabajadores de Oficina (Yendo a Casa)')
ax.fill_between(x_suave, trabajadores_oficina_van_suave, color='#FCBAD3', alpha=0.3)  # Rellenar la curva de trabajadores de oficina que se van a casa

# Curva y relleno de la fase de regreso
estudiantes_regresan_linea, = ax.plot(x_suave, estudiantes_regresan_suave, color='#CDEAC0', linewidth=2.5, label='Estudiantes (Regresando)')
ax.fill_between(x_suave, estudiantes_regresan_suave, color='#CDEAC0', alpha=0.3)  # Rellenar la curva de estudiantes que regresan

trabajadores_migrantes_regresan_linea, = ax.plot(x_suave, trabajadores_migrantes_regresan_suave, color='#FFDAC1', linewidth=2.5, label='Trabajadores Migrantes (Regresando)')
ax.fill_between(x_suave, trabajadores_migrantes_regresan_suave, color='#FFDAC1', alpha=0.3)  # Rellenar la curva de trabajadores migrantes que regresan

trabajadores_oficina_regresan_linea, = ax.plot(x_suave, trabajadores_oficina_regresan_suave, color='#FFB7B2', linewidth=2.5, label='Trabajadores de Oficina (Regresando)')
ax.fill_between(x_suave, trabajadores_oficina_regresan_suave, color='#FFB7B2', alpha=0.3)  # Rellenar la curva de trabajadores de oficina que regresan

# 5. Establecer las etiquetas de las marcas del eje x
plt.xticks(x_uniforme, fechas)
plt.xticks(rotation=30)

# 6. Agregar título, leyenda y decoración
ax.set_title('Tendencia de la Población Durante la Feria de Viajes de la Fiesta de Primavera 2017', fontsize=18, fontweight='bold', color='#333')
ax.set_xlabel('Fecha', fontsize=14, color='#555')
ax.set_ylabel('Tamaño de la Población', fontsize=14, color='#555')
ax.legend(loc='upper right', fontsize=11)

# 7. Agregar una línea divisoria (posición de la Fiesta de Primavera)
plt.axvline(x = 6.0, color='red', linestyle='--', alpha=0.5)
plt.text(5.6, max(estudiantes_van.max(), trabajadores_migrantes_van.max(), trabajadores_oficina_van.max()) * 0.95,
         'Fiesta de Primavera', fontsize=13, color='red')

# 8. Agregar líneas de cuadrícula
plt.grid(True, linestyle='--', alpha=0.6)

# 9. Ocultar los bordes superior y derecho
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 10. Mostrar el gráfico
plt.tight_layout()
plt.show()