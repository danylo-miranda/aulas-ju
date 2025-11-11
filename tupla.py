# Definindo uma tupla
coordenadas = [10.5, 25.3]
print(f"Tupla original: {coordenadas}")

#tentativa de modificar um elemento dentro da tupla
try:
    coordenadas[0] = 5.0
except TypeError as e:
    print(f'Erro ao tentar modificar a tupla: {e}')

print(coordenadas)