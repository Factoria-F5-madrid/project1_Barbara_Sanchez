from taximeter import taxi

def welcome():
    print("Bienvenido al sistema de taxímetro digital")
    print("Este programa permite calcular automáticamente la tarifa de un trayecto en taxi según el tiempo transcurrido y el estado del vehículo:")
    print("-"*20)
welcome()    


def show_menu():
    print("1. Iniciar viaje")
    print("2. Finalizar viaje")
    print("3. Salir")
    print("-"*20)
    return input("Seleccione una opción: ")

def start_ride():
    print("Iniciando viaje")
    taxi()

def end_ride():
    print("Finalizando viaje")


    
def main():    
    while True:
        option = show_menu()
        if option == "1":
            start_ride()
        elif option == "2":
            end_ride()
        elif option == "3":
            print("Hasta pronto, gracias por usar el taxímetro")
            break
        else:
            print("Opción inválida. Intentalo de nuevo")


main()
