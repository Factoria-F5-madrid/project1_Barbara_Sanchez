import os
import time

def taxi():
    print("Viaje iniciado")
    print("Escribe 'p' para PARADO, 'm' para MOVIMIENTO o 'f' para FINALIZAR el trayecto")

    total_cost = 0
    cost_stop = 0
    cost_move = 0

    price_stop = 0.02
    price_move = 0.05

    ride_active = True
    while ride_active:
        state = input("¿Estado del taxi? (p=parado, m=movimiento, f=finalizar): ").lower()
        if state == "p":
            print("Taxi parado. Tarifa: 0.02€/s.")
            while True:
                time.sleep(1)
                cost_stop += price_stop
                total_cost += price_stop
                print(f"Parado: {round(cost_stop, 2)}€, Total: {round(total_cost, 2)}€")

                choice = input("Enter = seguir parado, 'm' = moverse, 'f' = finalizar: ").lower()
                if choice == "m" or choice == "f":
                    state = choice
                    break

        elif state == "m":
            print("Taxi en movimiento. Tarifa: 0.05€/s.")
            while True:
                time.sleep(1)
                cost_move += price_move
                total_cost += price_move
                print(f"Movimiento: {round(cost_move, 2)}€, Total: {round(total_cost, 2)}€")

                choice = input("Enter = seguir, 'p' = parar, 'f' = finalizar: ").lower()
                if choice == "p" or choice == "f":
                    state = choice
                    break

        elif state == "f":
            ride_active = False
            print("Trayecto finalizado.")
            print(f"Tiempo parado: €{round(cost_stop, 2)}")
            print(f"Tiempo en movimiento: €{round(cost_move, 2)}")
            print(f"Total a pagar: €{round(total_cost, 2)}\n")

        else:
            print("Entrada no válida. Escribe 'p', 'm' o 'f'.")

       
taxi()    

            


