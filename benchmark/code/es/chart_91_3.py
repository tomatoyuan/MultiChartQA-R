import matplotlib.pyplot as plt

# Datos del gráfico circular exterior
tamaños_exteriores = [25, 17, 75]
etiquetas_exteriores = ['Participación en el mercado de las 10 empresas con mayores ingresos (%)', 'Participación en el mercado de las 5 empresas con mayores ingresos (%)', 'Participación en el mercado de otras empresas (%)']
colores_exteriores = ['#A4C639', '#87CEEB', '#D3D3D3']

# Datos del gráfico circular interior
tamaños_interiores = [25 + 17, 75]  # Las 10 principales (incluyendo las 5 principales), otras
etiquetas_interiores = ['', '']
colores_interiores = ['white', 'white']  # Círculo interior en blanco

# Crear un lienzo
fig, ax = plt.subplots(figsize=(6, 6))

# Dibujar el gráfico circular exterior
trozos_exteriores, textos_exteriores, textos_automaticos_exteriores = ax.pie(tamaños_exteriores, labels=etiquetas_exteriores, autopct='%1.1f%%',
                                                    colors=colores_exteriores, startangle=90,
                                                    textprops={'color': 'black'})
# Establecer el título
ax.set_title('Concentración del mercado de la industria de tazas y hervidores chinos en 2021', fontsize=14, fontweight='bold', y=1.05)

# Mantener el gráfico circular
ax.axis('equal')

plt.tight_layout()
plt.show()