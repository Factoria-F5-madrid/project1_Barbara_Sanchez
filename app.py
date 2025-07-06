import streamlit as st
from datetime import datetime
import time
from fee import get_dynamic_prices


st.set_page_config(page_title="Taxímetro Digital", page_icon="🚖", layout="centered")


if 'trayecto_iniciado' not in st.session_state:
    st.session_state['trayecto_iniciado'] = False
if 'estado_taxi' not in st.session_state:
    st.session_state['estado_taxi'] = 'Parado'
if 'start_time' not in st.session_state:
    st.session_state['start_time'] = None
if 'move_time' not in st.session_state:
    st.session_state['move_time'] = 0
if 'stop_time' not in st.session_state:
    st.session_state['stop_time'] = 0
if 'has_moved' not in st.session_state:
    st.session_state['has_moved'] = False


st.title("🚖 Taxímetro Digital")
st.markdown("## Bienvenido al sistema de taxímetro digital")
st.markdown("Esta aplicación te permite calcular automáticamente la tarifa de un trayecto en taxi según el tiempo transcurrido y el estado del vehículo.")


current_time = datetime.now().time()
price_stop, price_move = get_dynamic_prices(current_time)


is_peak = price_stop > 0.02 or price_move > 0.05
demand_status = "HORA PUNTA" if is_peak else "hora baja"


st.header("Control del Trayecto")
col1, col2 = st.columns(2)
with col1:
    iniciar = st.button("Iniciar trayecto", disabled=st.session_state['trayecto_iniciado'])
    if iniciar:
        st.session_state['trayecto_iniciado'] = True
        st.session_state['start_time'] = None  # No iniciar el tiempo hasta que se mueva
        st.session_state['move_time'] = 0
        st.session_state['stop_time'] = 0
        st.session_state['estado_taxi'] = 'Parado'
        st.session_state['has_moved'] = False

with col2:
    finalizar = st.button("Finalizar trayecto", disabled=not st.session_state['trayecto_iniciado'])
    if finalizar:
        st.session_state['trayecto_iniciado'] = False
        if st.session_state['start_time'] is not None:
            elapsed_time = time.time() - st.session_state['start_time']
            if st.session_state['estado_taxi'] == 'En movimiento':
                st.session_state['move_time'] += elapsed_time
            elif st.session_state['has_moved']:
                st.session_state['stop_time'] += elapsed_time
        total_cost = (st.session_state['move_time'] * price_move) + (st.session_state['stop_time'] * price_stop)
        st.write("Trayecto finalizado.")
        st.write(f"Tiempo total en movimiento: {int(st.session_state['move_time'])}s")
        st.write(f"Tiempo total parado: {int(st.session_state['stop_time'])}s")
        st.write(f"Costo total: {round(total_cost, 2)}€")


if st.session_state['trayecto_iniciado']:
    st.header("Tarifas")
    st.write(f"Estado de demanda: {demand_status}")
    st.write(f"- Parado: {price_stop}€/s")
    st.write(f"- Movimiento: {price_move}€/s")


if st.session_state['trayecto_iniciado']:
    st.header("Estado del Taxi")
    estado = st.radio("Selecciona el estado del taxi:", ('Parado', 'En movimiento'), index=0 if st.session_state['estado_taxi'] == 'Parado' else 1)
    if estado != st.session_state['estado_taxi']:
        if st.session_state['start_time'] is not None:
            elapsed_time = time.time() - st.session_state['start_time']
            if st.session_state['estado_taxi'] == 'En movimiento':
                st.session_state['move_time'] += elapsed_time
                st.session_state['has_moved'] = True
            elif st.session_state['has_moved']:
                st.session_state['stop_time'] += elapsed_time
        st.session_state['estado_taxi'] = estado
        st.session_state['start_time'] = time.time() if estado == 'En movimiento' or st.session_state['has_moved'] else None

    
    tiempo_container = st.empty()
    while st.session_state['trayecto_iniciado']:
        current_time = time.time()
        if st.session_state['estado_taxi'] == 'En movimiento' and st.session_state['start_time'] is not None:
            move_time = st.session_state['move_time'] + (current_time - st.session_state['start_time'])
            stop_time = st.session_state['stop_time']
        elif st.session_state['has_moved'] and st.session_state['start_time'] is not None:
            move_time = st.session_state['move_time']
            stop_time = st.session_state['stop_time'] + (current_time - st.session_state['start_time'])
        else:
            move_time = st.session_state['move_time']
            stop_time = st.session_state['stop_time']

       
        total_cost = (move_time * price_move) + (stop_time * price_stop)

        
        tiempo_container.markdown(f"### Tiempo y Precio\n- Tiempo en movimiento: {int(move_time)}s\n- Tiempo parado: {int(stop_time)}s\n- Precio acumulado: {round(total_cost, 2)}€")

        time.sleep(1)
