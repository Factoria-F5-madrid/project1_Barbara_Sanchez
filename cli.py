from taximeter import taxi

def welcome():
    print("Bienvenido al sistema de taxímetro digital")
    print("Este programa permite calcular automáticamente la tarifa de un trayecto en taxi según el tiempo transcurrido y el estado del vehículo:")
    print("-"*20)
welcome()    


def show_menu(ride_active):
    if not ride_active:
        print("1. Iniciar viaje")
        print("2. Salir")
    else:
        print("1.Finalizar viaje")
        print("2.Salir")
    print("-"*20)
    return input("Selecciona una opción: ")

def start_ride():
    print("Iniciando viaje")
    taxi()

def end_ride():
    print("Finalizando viaje")


    
def main():
    
    ride_active = False 

    while True:
        option = show_menu(ride_active)

        if not ride_active:
            if option == "1":
                start_ride()
                ride_active = True
            elif option == "2":
                print("Finalizando el viaje antes de salir")
                end_ride()
                ride_active = False
                print("Hasta pronto, gracias por usar el taxímetro")
                break
            else:
                print("Opción inválida. Inténtalo de nuevo")
        else:
            if option == "1":
                end_ride()
                ride_active = False
            elif option == "2":
                print("Hasta pronto, gracias por usar el taxímetro")
                break
            else:
                print("Opción inválida. Inténtalo de nuevo")
   
    
main()
