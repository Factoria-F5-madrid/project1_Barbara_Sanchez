from taximeter import Taximeter


def welcome():
    print("Bienvenido al sistema de taxímetro digital")
    print("Este programa permite calcular automáticamente la tarifa de un trayecto en taxi según el tiempo transcurrido y el estado del vehículo:")
  
   

def show_menu():
    print("-" * 20)
    print("1. Iniciar un nuevo trayecto")
    print("2. Salir")
    print("-" * 20)
    return input("Selecciona una opción: ")

    
def main():


    
    welcome()

    while True:
        option = show_menu()

        if option == "1":
            taxi = Taximeter()
            taxi.start_ride()
        elif option == "2":
            print("Hasta pronto. Gracias por usar el taxímetro digital.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
   
    
main()
