import random
import threading

cuenta_1 = 1000
cuenta_2 = 1000
total_en_ambas_cuentas = 2000

def mover_monto_c1_a_c2():
    global cuenta_1, cuenta_2

    cantidad = random.randint(0, 10)

    cuenta_1 -= cantidad
    cuenta_2 += cantidad

    checar_total()


def mover_monto_c2_a_c1():
    global cuenta_1, cuenta_2

    cantidad = random.randint(0, 10)

    cuenta_2 -= cantidad
    cuenta_1 += cantidad

    checar_total()


def checar_total():
    global cuenta_1, cuenta_2

    total = cuenta_1 + cuenta_2

    if total != total_en_ambas_cuentas:
        print(F'--------- Cantidad Invalida {total}')


def ejecutar(funcion):
    while True:
        funcion()


t1 = threading.Thread(target=ejecutar, args=(mover_monto_c1_a_c2, ))
t2 = threading.Thread(target=ejecutar, args=(mover_monto_c2_a_c1, ))

t1.start()
t2.start()