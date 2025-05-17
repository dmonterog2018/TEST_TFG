
import random
print("PROGRAMA 3 NUMEROS ALEATORIOS")

def tres_numeros_aleatorios():
    return [random.randint(0, 100) for _ in range(3)]

print(tres_numeros_aleatorios())

