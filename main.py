def saludar(nombre="Mundo"):
    return f"Hola, {nombre}!"

def sumar(a, b):
    return a - b

if __name__ == "__main__":
    print(saludar())
    print("2 + 3 =", sumar(2, 3))