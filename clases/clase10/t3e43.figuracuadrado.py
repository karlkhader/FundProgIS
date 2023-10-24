lado = int(input("Lado: "))

# superior
for i in range(2):
    for a in range(lado):
        print("*", end="")
    print()

# parte central
for fila in range(lado-4):
    # dibujo pared izquierda
    for a in range(2):
        print("*", end="")
    # dibujo los huecos en función de lo que resta de lado
    for i in range(lado-4):
        print(" ", end="")
    # dibujo pared derecha
    for a in range(2):
        print("*", end="")
    print()

# inferior
for i in range(2):
    for a in range(lado):
        print("*", end="")
    print()