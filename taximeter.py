import time
from datetime import datetime
from fee import get_dynamic_prices

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

def total_price(move_time, stop_time, price_move, price_stop):
    return (move_time * price_move) + (stop_time * price_stop)


def taxi():
    print("Viaje iniciado")

    current_time = datetime.now().time()
    price_stop, price_move = get_dynamic_prices(current_time) 

    
    is_peak = price_stop > 0.02 or price_move > 0.05
    demand_status = "HORA PUNTA" if is_peak else "hora baja"

    print(f"Hora actual: {current_time.strftime('%H:%M')}")
    print(f"Estado de demanda: {demand_status}")
    print(f"Tarifas aplicadas:")
    print(f"   - Parado: €{price_stop:.2f}/s")
    print(f"   - Movimiento: {price_move:.2f}€/s ")
    
   
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
    
    total = total_price(move_time, stop_time, price_move, price_stop)
    print(f"Total: {round(total, 2)} €")

