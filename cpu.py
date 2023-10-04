# Ejemplo para demostrar uso excesivo de cpu

def operacion_intensiva():
    result = 0
    for _ in range(10**7):
        result += 1
    return result

while True:
    operacion_intensiva()