import matplotlib.pyplot as plt
import numpy as np

# Organización de datos
# Datos de duración promedio del sueño diario (fin de semana, días laborables)
etiquetas_duracion_sueno = ["Menos de 6 horas", "De 6 a 7 horas", "De 7 a 8 horas", "De 8 a 9 horas", "De 9 a 10 horas", "Más de 10 horas"]
sueno_fin_semana = [2.2, 12.2, 29.0, 35.3, 17.6, 3.7]
sueno_dia_laborable = [6.7, 20.4, 40.0, 16.6, 10.5, 5.8]

# Datos de hora de acostarse (fin de semana, días laborables)
etiquetas_hora_sueno = ["Antes de las 22:00", "Entre 22:00 y 23:00", "Entre 23:00 y 0:00", "Entre 0:00 y 1:00", "Entre 1:00 y 2:00", "Después de las 2:00"]
hora_sueno_fin_semana = [5.2, 23.0, 33.1, 22.1, 12.5, 4.1]
hora_sueno_dia_laborable = [7.9, 31.2, 34.4, 13.5, 7.8, 5.2]

x = np.arange(len(etiquetas_duracion_sueno))  # Eje x para la duración del sueño
x2 = np.arange(len(etiquetas_hora_sueno))     # Eje x para la hora de acostarse

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Gráfico [Fin de semana - Duración promedio del sueño diario]
axes[0, 0].bar(x, sueno_fin_semana, color='orange', label='Fin de semana')
axes[0, 0].set_xticks(x)
axes[0, 0].set_xticklabels(etiquetas_duracion_sueno, rotation=15, ha='right')
axes[0, 0].set_ylabel('Porcentaje (%)')
axes[0, 0].set_title('Duración promedio del sueño diario de los residentes chinos (Fin de semana)')
for i, val in enumerate(sueno_fin_semana):
    axes[0, 0].text(i, val + 1, f'{val}%', ha='center')

# Gráfico [Días laborables - Duración promedio del sueño diario]
axes[1, 0].bar(x, sueno_dia_laborable, color='gold', label='Días laborables')
axes[1, 0].set_xticks(x)
axes[1, 0].set_xticklabels(etiquetas_duracion_sueno, rotation=15, ha='right')
axes[1, 0].set_ylabel('Porcentaje (%)')
axes[1, 0].set_title('Duración promedio del sueño diario de los residentes chinos (Días laborables)')
for i, val in enumerate(sueno_dia_laborable):
    axes[1, 0].text(i, val + 1, f'{val}%', ha='center')

# Gráfico [Fin de semana - Hora de acostarse]
axes[0, 1].bar(x2, hora_sueno_fin_semana, color='orange', label='Fin de semana')
axes[0, 1].set_xticks(x2)
axes[0, 1].set_xticklabels(etiquetas_hora_sueno, rotation=15, ha='right')
axes[0, 1].set_ylabel('Porcentaje (%)')
axes[0, 1].set_title('Hora de acostarse de los residentes chinos (Fin de semana)')
for i, val in enumerate(hora_sueno_fin_semana):
    axes[0, 1].text(i, val + 1, f'{val}%', ha='center')

# Gráfico [Días laborables - Hora de acostarse]
axes[1, 1].bar(x2, hora_sueno_dia_laborable, color='gold', label='Días laborables')
axes[1, 1].set_xticks(x2)
axes[1, 1].set_xticklabels(etiquetas_hora_sueno, rotation=15, ha='right')
axes[1, 1].set_ylabel('Porcentaje (%)')
axes[1, 1].set_title('Hora de acostarse de los residentes chinos (Días laborables)')
for i, val in enumerate(hora_sueno_dia_laborable):
    axes[1, 1].text(i, val + 1, f'{val}%', ha='center')

plt.tight_layout()
plt.show()