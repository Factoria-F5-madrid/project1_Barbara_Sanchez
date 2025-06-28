import time

price_stop = 0.02
price_move = 0.05

def move():
    return time.perf_counter()

def stop(start_time, move_time):
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    move_time += elapsed_time
    return elapsed_time, move_time

def pause(start_time, stop_time):
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    stop_time += elapsed_time
    return elapsed_time, stop_time

def total_price(move_time, stop_time):
    return (move_time * price_move) + (stop_time * price_stop)

def taxi():
    print("Viaje iniciado")
   
    move_time = 0
    stop_time = 0
    ride_active = True

    state = input("¿Estado inicial del taxi? (p=parado, m=movimiento): ").lower()
    while ride_active:
        if state == "m":
            start_time = move()
            while True:
                cont = input("Presiona Enter para seguir en movimiento, 'p' para parar, 'f' para finalizar: ").lower()
                if cont == "":
                    continue
                elif cont == "p":
                    _, move_time = stop(start_time, move_time)
                    state = "p"
                    break
                elif cont == "f":
                    _, move_time = stop(start_time, move_time)
                    ride_active = False
                    break
        elif state == "p":
            start_time = move()
            while True:
                cont = input("Presiona Enter para seguir parado, 'm' para moverse, 'f' para finalizar: ").lower()
                if cont == "":
                    continue
                elif cont == "m":
                    _, stop_time = pause(start_time, stop_time)
                    state = "m"
                    break
                elif cont == "f":
                    _, stop_time = pause(start_time, stop_time)
                    ride_active = False
                    break
        else:
            print("Entrada no válida. Usa 'p', 'm' o 'f'.")
            state = input("¿Estado del taxi? (p=parado, m=movimiento): ").lower()

   
    print("Trayecto finalizado")
    print(f"Tiempo en movimiento: {round(move_time, 2)}s")
    print(f"Tiempo parado: {round(stop_time, 2)}s")
    print(f"Total: €{round(total_price(move_time, stop_time), 2)}")
