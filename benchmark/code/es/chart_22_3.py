import matplotlib.pyplot as plt
import numpy as np

# Datos de los patrocinadores
patrocinadores = {
    "Ping An Insurance": 1.815,
    "Nike": 1,
    "Ford": 0.4,
    "JD.com": 0.35,
    "Carlsberg": 0.2,
    "DHL": 0.2,
    "Red Bull": 0.2
}

# Crear un lienzo
plt.figure(figsize=(12, 8))

# Gráfico de barras de los montos de patrocinio
nombres_patrocinadores = list(patrocinadores.keys())
valores_patrocinadores = list(patrocinadores.values())
barras = plt.bar(nombres_patrocinadores, valores_patrocinadores, color='#66b3ff')
plt.title('Monto de Patrocinio de los Patrocinadores')
plt.xlabel('Patrocinador')
plt.ylabel('Monto (Miles de millones)')
plt.xticks(rotation=45)

# Agregar etiquetas numéricas
for barra in barras:
    altura = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2., altura,
             f'{altura:.3f}',
             ha='center', va='bottom')

plt.tight_layout()
plt.show()