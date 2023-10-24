sa = int(input("Semialtura: "))

# Parte superior
# Defino variables contadores para los asteriscos y espacios
ast: int = 1
espacios: int = sa-1
# Recorro la parte superior hasta la mitad incluida
for linea in range(sa):
    # Imprimo los espacios
    for i in range(espacios):
        print(" ", end='')
    # Imprimo los asteriscos
    for i in range(ast):
        print('*', end='')
    print()
    # Varío los contadores para la siguiente iteración
    ast += 2
    espacios -= 1

# Parte inferior
ast -= 4 # Modifico el contador de asteriscos restando los 2 que sumé al final y los 2 asteriscos menos que deben haber
espacios = 1 # Al comienzo solo hay un espacio
for linea in range(sa-1, 0, -1):
    for i in range(espacios):
        print(" ", end='')
    for i in range(ast):
        print('*', end='')
    print()
    ast -= 2
    espacios += 1