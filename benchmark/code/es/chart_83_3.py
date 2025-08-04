import matplotlib.pyplot as plt

# -------------------- Definición de Datos --------------------
etiquetas = ['1 - 500,000 yuan (unidades)', '500,001 - 999,999 yuan (unidades)', '1,000,000 yuan y más (unidades)']
tamaños = [95, 3, 2]  # Proporción
valores_absolutos = [950, 30, 20]  # Cantidades reales asumidas (opcional)

# Nuevo esquema de colores (mejora la legibilidad y la estética)
colores = ['#ff6f91', '#845ec2', '#88ccf1']

# -------------------- Crear el lienzo --------------------
fig, ax = plt.subplots(figsize=(7, 6))

# -------------------- Dibujar el gráfico de donut (Gráfico circular + agujero central) --------------------
porciones, textos, textos_automaticos = ax.pie(
    tamaños,
    labels=etiquetas,
    autopct='%1.1f%%',
    startangle=140,
    colors=colores,
    wedgeprops=dict(width=0.6, edgecolor='white')  # Forma de donut + Borde blanco
)

# -------------------- Ajustar el estilo del texto --------------------
for i, texto_automatico in enumerate(textos_automaticos):
    texto_automatico.set_color('white')
    texto_automatico.set_fontweight('bold')
    texto_automatico.set_fontsize(10)

# -------------------- Agregar anotación central --------------------
total = sum(valores_absolutos)
ax.text(
    0, 0,
    f"Total\n{total} unidades",
    ha='center', va='center',
    fontsize=12,
    fontweight='bold',
    color="#424242"
)

# -------------------- Agregar título --------------------
ax.set_title(
    "Distribución de unidades de equipos por valor superior a 10,000 yuan en hospitales de rehabilitación chinos en 2020 (Gráfico de donut)",
    fontsize=14,
    fontweight='bold',
    pad=20
)

# -------------------- Optimizar el diseño y mostrar --------------------
plt.tight_layout()
plt.show()