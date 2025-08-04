import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# 数据
etiquetas = ["Crecimiento de cabello anti-caída",
             "Eliminación de grasa y relajación",
             "Hidratación", "Limpieza profunda",
             "Resaltado de color de cabello",
             "Mejora de la fibra capilar",
             "Fuerza y prevención de rotura de cabello",
             "Mejora del folículo piloso",
             "Eliminación de caspa e itching"]
columnas = ["Generación 05", "Generación 00", "Generación 95", "Generación 90", "Generación 85", "Antes de los 80"]
datos = [
    [96, 120, 105, 114, 95, 49],
    [101, 130, 82, 100, 96, 121],
    [160, 88, 119, 90, 58, 123],
    [104, 95, 72, 96, 120, 124],
    [121, 93, 109, 67, 122, 87],
    [78, 43, 117, 113, 147, 116],
    [45, 74, 132, 106, 85, 100],
    [95, 78, 107, 132, 60, 85],
    [85, 93, 105, 96, 115, 98]
]

# Crear DataFrame
df = pd.DataFrame(datos, index=etiquetas, columns=columnas)

# Establecer valores por debajo de 100 como blanco
df_enmascarado = df.copy()
df_enmascarado[df < 100] = np.nan

# Elegir la paleta de colores
cmap = sns.light_palette("deeppink", as_cmap=True)

# Dibujar el mapa de calor
plt.figure(figsize=(10, 6))
sns.heatmap(df_enmascarado, annot=df, fmt="d", cmap=cmap, linewidths=0.5, linecolor='grey', cbar=True,
            mask=df < 100, annot_kws={"size": 10}, square=False)

# Establecer el título y el estilo
plt.title("Encuesta de necesidades de salud del cuero cabelludo de mujeres de diferentes generaciones (TGI>100)", fontsize=14)
plt.xticks(rotation=0)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()