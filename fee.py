# fee.py
from datetime import datetime, time

def get_dynamic_prices(current_time=None):
   
    if current_time is None:
        current_time = datetime.now().time()

  
    morning_peak = time(7, 0) <= current_time <= time(10, 0)
    afternoon_peak = time(17, 0) <= current_time <= time(19, 0)

    if morning_peak or afternoon_peak:
        price_stop = 0.03  
        price_move = 0.07
    else:
        price_stop = 0.02
        price_move = 0.05

    return price_stop, price_move
