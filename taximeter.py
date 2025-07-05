import time
from datetime import datetime
from fee import get_dynamic_prices
import logging

logging.basicConfig(
    filename="taximeter.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def move():
    return time.perf_counter()

def measure_time(start_time, accumulated_time):
    end_time = time.perf_counter()
    return accumulated_time + (end_time - start_time)

def total_price(move_time, stop_time, price_move, price_stop):
    return (move_time * price_move) + (stop_time * price_stop)

def save_trip_log(move_time, stop_time, total):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    line = f"{now} | Movimiento: {round(move_time, 2)}s | Parado: {round(stop_time, 2)}s | Total: €{round(total, 2)}\n"
    with open("historial.txt", "a", encoding="utf-8") as f:
        f.write(line)
    logging.info("Trayecto guardado en historial.txt")   


def taxi():
    print("Viaje iniciado")
    logging.info("Viaje iniciado")

    current_time = datetime.now().time()
    price_stop, price_move = get_dynamic_prices(current_time) 

    
    is_peak = price_stop > 0.02 or price_move > 0.05
    demand_status = "HORA PUNTA" if is_peak else "hora baja"

    print(f"Hora actual: {current_time.strftime('%H:%M')}")
    print(f"Estado de demanda: {demand_status}")
    print(f"Tarifas:")
    print(f"   - Parado: €{price_stop:.2f}/s")
    print(f"   - Movimiento: {price_move:.2f}€/s ")
    
    logging.info(f"Tarifas - Parado: €{price_stop:.2f}/s, Movimiento: €{price_move:.2f}/s")


    move_time = 0
    stop_time = 0
    ride_active = True

    state = input('Cómo está el taxi? (p=parado, m=movimiento): ').lower()
    
    while ride_active:
        if state in ('m', 'p'):
            start_time = time.perf_counter()

            if state == "m":
                next_state = input("Para parar pulsa (p) y para finalizar trayecto (f)?: ").lower()
            elif state == "p":
                next_state = input("Para moverse pulsa (m) y para finalizar trayecto (f)?: ").lower()

            if next_state == 'f':
                if state == 'm':
                    move_time = measure_time(start_time, move_time)
                else:
                    stop_time = measure_time(start_time, stop_time)
                logging.info('Trayecto finalizado por el usuario')
                ride_active = False

            elif next_state == 'p' and state == 'm':
                move_time = measure_time(start_time, move_time)
                logging.info('Cambio de estado: movimiento a parado')
                state = 'p'

            elif next_state == "m" and state == "p":
                stop_time = measure_time(start_time, stop_time)
                logging.info("Cambio de parado a movimiento")
                state = 'm'

            else:
                print("Entrada no válida o sin cambio de estado.")
                logging.warning(f"Entrada sin efecto o inválida: {next_state}")

        else:
            print("Entrada no válida. Usa 'p', 'm' o 'f'.")
            logging.warning(f"Entrada inicial inválida: {state}")
            state = input("Cómo está el taxi? (p=parado, m=movimiento): ").lower()

   
    print("Trayecto finalizado")
    print(f"Tiempo en movimiento: {round(move_time, 2)}s")
    print(f"Tiempo parado: {round(stop_time, 2)}s")
    
    total = total_price(move_time, stop_time, price_move, price_stop)
    print(f"Total: {round(total, 2)} €")

    logging.info(f"Trayecto finalizado - Movimiento: {round(move_time, 2)}s, Parado: {round(stop_time, 2)}s, Total: €{round(total, 2)}")

    save_trip_log(move_time, stop_time, total)