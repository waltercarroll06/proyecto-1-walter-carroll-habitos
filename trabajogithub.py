# nombre usuario

nombre_usuario = input("ingresa tu nombre: ")
# meta usuario

meta_usuario = input("ingresa tu meta: ")

#mensaje de bienvenida

print(f"¡Bienvenid@ {nombre_usuario} a Control de Hábitos! Un paso pequeño cada día puede cambiar tu vida.\n")


# variables globales

habitos = []


# funciones 

def mostrar_menu():
    print("===== CONTROL DE HÁBITOS =====\n")
    print("selecciona una opción:\n")
    print("1. Ver hábitos\n")
    print("2. Agregar hábito\n")
    print("3. Completar hábito\n")
    print("4. Eliminar hábito\n")
    print("5. Ver progreso\n")
    print("6. salir\n")
    opcion_valida = True
    while opcion_valida:
        try:
            opcion_usuario = int(input("ingresa una opcion: "))
            if opcion_usuario >= 1 and opcion_usuario <= 6:
                opcion_valida = False
                return opcion_usuario
            else:
                print("ERROR, ingrese nuevamente una opcion")
        except ValueError:
            print("ingrese solo un numero")        

def ver_habitos():
    if len(habitos) == 0:
        print("no hay habitos registrados")
    else:
        for index, habito in enumerate(habitos, +1):
            print(f"{index}. {habito}")

def agregar_habito():
    habito_correcto = True
    while habito_correcto:
        nombre_habito = input("ingresa el nombre del habito: ").strip()
        if nombre_habito.isdigit():
            print("nombre no puede contener numeros")
        else:
            try:       
                duracion_habito = int(input("duracion del habito: "))  
                print("habito guardado")  
                habito_correcto = False
                break
            except ValueError:
                print("solo se puede numeros")
    if not habito_correcto:
        habito = {
            "nombre": nombre_habito,
            "duracion": duracion_habito,
            "estado" : "pendiente"
        }

        habitos.append(habito)

def completar_habito():
    habito_completado = True
    while habito_completado:
            if len(habitos) == 0:
                print("no hay habitos registrados")
                habito_completado = False
            else:
                for index , h in enumerate(habitos, +1):
                    print(f"{index}. {h}")
                try:
                    numero_habito = int(input("ingresa el numero del habito que desea marcar como comnpleto: "))
                    if numero_habito <= len(habitos) and numero_habito >= 1:
                        habitos[numero_habito-1]["estado"]  = "completado"
                        print("habito completado")
                        habito_completado = False
                    else:
                        print("habito no encontrado....")    
                except ValueError:
                    print("error ingresa el numero del habtio que quieres cambiar o si deseas salir presione 0")
                    n = int(input(""))     
                    if n == 0:
                        habito_completado = False   

def eliminar_habito():
    habito_eliminar = True
    while habito_eliminar:
            if len(habitos) == 0:
                print("no hay habitos registrados")
                habito_eliminar = False
            else:
                for index , h in enumerate(habitos, +1):
                    print(f"{index}. {h}")
                try:
                    numero_habito = int(input("ingresa el numero del habito que desea eliminaro: "))
                    if numero_habito <= len(habitos) and numero_habito >= 1:
                        habitos.pop(numero_habito-1)
                    else:
                        print("habito no encontrado") 
                except ValueError:
                    print("error ingresa el numero del habtio que quieres cambiar o si deseas salir presione 0")
                    n = int(input(""))     
                    if n == 0:
                        habito_eliminar = False   

def ver_progreso():
    habitos_completados = len([h for h in habitos if h["estado"] == "completado"])
    habitos_pendiente =  len([h for h in habitos if h["estado"] == "pendiente"])
    print(f"tienes un total de {habitos_completados} habitos completados y \n")
    print(f"tienes un total de {habitos_pendiente} habitos pendientes")


# menu

while True:
    opcion = mostrar_menu()
    if opcion == 1:
        ver_habitos()
    elif opcion == 2:
        agregar_habito()
    elif opcion == 3:
        completar_habito()
    elif opcion == 4:
        eliminar_habito()
    elif opcion == 5:
        ver_progreso()
    elif opcion == 6:
        print("Gracias por usar Control de Hábitos.")
        break
    else:
        print("Opción no válida. Intenta otra vez.")
