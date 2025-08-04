import matplotlib.pyplot as plt
import numpy as np

# Datos
ingresos_totales = 15
derechos_medios = 10
patrocinadores = {
    "Ping An Insurance": 1.815,
    "Nike": 1,
    "Ford": 0.4,
    "JD.com": 0.35,
    "Carlsberg": 0.2,
    "DHL": 0.2,
    "Red Bull": 0.2
}
socios = {
    "Shell": 0.2,
    "TAG Heuer": 0.4
}

# Calcular otros ingresos
otros_ingresos = ingresos_totales - derechos_medios - sum(patrocinadores.values()) - sum(socios.values())

# Crear figura
plt.figure(figsize=(12, 10))

# Preparar datos para el gráfico de barras
categorias = ["Derechos de Medios", "Patrocinadores", "Socios Oficiales", "Otros"]
valores = [derechos_medios, sum(patrocinadores.values()), sum(socios.values()), otros_ingresos]
colores = ['#4e79a7', '#f28e2b', '#e15759', '#76b7b2']

# Graficar el gráfico de barras principal - ingresos por categoría
plt.subplot(2, 1, 1)
barras = plt.bar(categorias, valores, color=colores)
plt.title('Distribución de Ingresos de la Compañía de la Superliga China (por Categoría)')
plt.ylabel('Monto (CNY 100 millones)')

# Agregar etiquetas de valor en las barras
for barra in barras:
    altura = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2., altura,
             f'{altura:.2f} CNY ({altura/ingresos_totales*100:.1f}%)',
             ha='center', va='bottom')

# Graficar el gráfico de barras detallado para patrocinadores y socios
plt.subplot(2, 1, 2)

# Combinar datos de patrocinadores y socios
nombres_patrocinadores = list(patrocinadores.keys())
valores_patrocinadores = list(patrocinadores.values())
nombres_socios = list(socios.keys())
valores_socios = list(socios.values())

# Establecer posiciones de las barras
x_patrocinadores = np.arange(len(nombres_patrocinadores))
x_socios = np.arange(len(nombres_socios)) + len(nombres_patrocinadores) + 1

# Graficar barras de patrocinadores
plt.bar(x_patrocinadores, valores_patrocinadores, width=0.6, label='Patrocinadores', color='#59a14f')
# Graficar barras de socios
plt.bar(x_socios, valores_socios, width=0.6, label='Socios', color='#af7aa1')

# Establecer etiquetas y marcas del eje x
plt.xticks(list(x_patrocinadores) + list(x_socios), nombres_patrocinadores + nombres_socios, rotation=45, ha='right')
plt.title('Ingresos Detallados de Patrocinadores y Socios')
plt.ylabel('Monto (CNY 100 millones)')
plt.legend()

# Agregar etiquetas de valor en las barras
for i, v in enumerate(valores_patrocinadores):
    plt.text(x_patrocinadores[i], v + 0.02, f'{v:.2f}', ha='center')
for i, v in enumerate(valores_socios):
    plt.text(x_socios[i], v + 0.02, f'{v:.2f}', ha='center')

plt.tight_layout()
plt.show()