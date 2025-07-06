import time
from datetime import datetime
from fee import get_dynamic_prices
import logging


logging.basicConfig(
    filename="taximeter.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Taximeter:
    def __init__(self):
        self.move_time = 0
        self.stop_time = 0
        self.ride_active = True
        self.current_time = datetime.now().time()
        self.price_stop, self.price_move = get_dynamic_prices(self.current_time)
        self.state = None

    def measure_time(self, start_time, accumulated_time):
        return accumulated_time + (time.perf_counter() - start_time)


    def save_trip_log(self, move_time, stop_time, total):
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        line = f"{now} | Movimiento: {round(self.move_time, 2)}s | Parado: {round(self.stop_time, 2)}s | Total: {round(total, 2)}\n€"
        with open("historial.txt", "a", encoding="utf-8") as f:
            f.write(line)
        logging.info("Trayecto guardado en historial.txt")   


    def start_ride(self):
        

        print("Viaje iniciado")
        logging.info("Viaje iniciado")

   
 
        is_peak = self.price_stop > 0.02 or self.price_move > 0.05
        demand_status = "HORA PUNTA" if is_peak else "hora baja"

        print(f"Hora actual: {self.current_time.strftime('%H:%M')}")
        print(f"Estado de demanda: {demand_status}")
        print(f"Tarifas:")
        print(f"   - Parado: {self.price_stop:.2f}€/s")
        print(f"   - Movimiento: {self.price_move:.2f}€/s ")
    
        logging.info(f"Tarifas - Parado: €{self.price_stop:.2f}/s, Movimiento: €{self.price_move:.2f}/s")

        self.state = input('Cómo está el taxi? (p=parado, m=movimiento): ').lower()
    
        while self.ride_active:
            if self.state in ('m', 'p'):
                start_time = time.perf_counter()

            if self.state == "m":
                next_state = input("Para parar pulsa (p) y para finalizar trayecto (f): ").lower()
            elif self.state == "p":
                next_state = input("Para moverse pulsa (m) y para finalizar trayecto (f): ").lower()

            if next_state == 'f':
                if self.state == 'm':
                    self.move_time = self.measure_time(start_time, self.move_time)
                else:
                    self.stop_time = self.measure_time(start_time, self.stop_time)
                logging.info('Trayecto finalizado por el usuario')
                self.ride_active = False
                break

            elif next_state == 'p' and self.state == 'm':
                self.move_time = self.measure_time(start_time, self.move_time)
                logging.info('Cambio de estado: movimiento a parado')
                self.state = 'p'

            elif next_state == "m" and self.state == "p":
                self.stop_time = self.measure_time(start_time, self.stop_time)
                logging.info("Cambio de parado a movimiento")
                self.state = 'm'

            else:
                print("Entrada no válida. Usa 'p', 'm' o 'f'.")
                logging.warning(f"Entrada inicial inválida: {self.state}")
                self.state = input("Cómo está el taxi? (p=parado, m=movimiento): ").lower()

        self.end_ride()

    def end_ride(self):
        print("Trayecto finalizado")
        print(f"Tiempo en movimiento: {round(self.move_time, 2)}s")
        print(f"Tiempo parado: {round(self.stop_time, 2)}s")
    
        total = (self.move_time * self.price_move) + (self.stop_time * self.price_stop)
        print(f"Total: {round(total, 2)} €")

        logging.info(f"Trayecto finalizado - Movimiento: {round(self.move_time, 2)}s, Parado: {round(self.stop_time, 2)}s, Total: €{round(total, 2)}")

        self.save_trip_log(self.move_time, self.stop_time, total)