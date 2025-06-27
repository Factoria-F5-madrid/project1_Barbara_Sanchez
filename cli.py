def show_menu():
    print("Bienvenido al sistema de taxímetro digital")
    print("Este programa permite calcular automáticamente la tarifa de un trayecto en taxi según el tiempo transcurrido y el estado del vehículo:")
    print("1. Iniciar viaje")
    print("2. Finalizar viaje")
    print("3. Mostrar información del viaje")
    print("4. Salir")
    return input("Seleccione una opción: ")

def start_ride():
    print("Iniciando viaje")

def end_ride():
    print("Finalizando viaje")

def show_ride_info():
    print("Mostrando información del viaje")

    
def main():    
    while True:
        option = show_menu()
        if option == "1":
            start_ride()
        elif option == "2":
            end_ride()
        elif option == "3":
            show_ride_info()
        elif option == "4":
            print("Saliendo del programa")
            break
        else:
            print("Opción inválida")



