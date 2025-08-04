import matplotlib.pyplot as plt
import pandas as pd

# Preparación de datos
etiquetas = ['Somatización', 'Síntomas obsesivos\n'
                             ' - compulsivos',
             'Sensibilidad en relaciones\n'
             ' interpersonales', 'Depresión', 'Ansiedad', 'Hostilidad',
             'Fobia', 'Paranoia', 'Psicosis', 'Otros \n(problemas de sueño, etc.)']
obvio = [8.1, 19.2, 17.9, 24.6, 16.7, 14.3, 8.9, 13.2, 11.2, 14.5]
leve = [29.9, 41.9, 39.6, 40.3, 37.5, 33.1, 27.3, 34.6, 36.6, 38.6]
saludable = [62.0, 38.9, 42.5, 35.1, 45.8, 52.6, 63.7, 52.2, 52.1, 46.9]

df = pd.DataFrame({
    'Obvio': obvio,
    'Leve': leve,
    'Saludable': saludable
}, index=etiquetas)

# Dibujo del gráfico
fig, ax = plt.subplots(figsize=(10, 8))
df[::-1].plot(kind='barh', stacked=True, color=['#FFCB2F', '#7D65AD', '#99DEEB'], ax=ax)

# Añadir etiquetas
for i, (obs, mid, hea) in enumerate(zip(obvio[::-1], leve[::-1], saludable[::-1])):
    ax.text(obs / 2, i, f'{obs}%', va='center', ha='center', color='black', fontsize=8)
    ax.text(obs + mid / 2, i, f'{mid}%', va='center', ha='center', color='white', fontsize=8)
    ax.text(obs + mid + hea / 2, i, f'{hea}%', va='center', ha='center', color='black', fontsize=8)

# Ajuste de estilo
ax.set_title('Distribución de los resultados de la auto - evaluación de salud \n'
             'mental en usuarios de evaluación psicológica', fontsize=14)
ax.set_xlabel('Porcentaje')
ax.set_xlim(0, 100)
ax.legend(loc='upper center', ncol=3, bbox_to_anchor=(0.5, -0.08))
plt.tight_layout()
plt.show()