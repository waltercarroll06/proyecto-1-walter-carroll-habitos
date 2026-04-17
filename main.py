import random

nombre_usuario = input("¿Como es tu nombre?\n")
print(f"Hola {nombre_usuario} bienvenid@ a 'un paso mas' disfruta este proceso.\n")

meta_usuario = input("cual es tu meta principal: ")
print(f"Hola {nombre_usuario}, tu meta principal es: {meta_usuario}")

def habito(area):
   paso_1 = input("Ingrese el primera paso con el que quiere empezar: ")  
   tiempo_paso = int(input("ingrese tiempo de duracion del paso: "))
   habito_usuario = {
   "area": area,
   "paso": paso_1,
   "tiempo": tiempo_paso,
   "estado": "pendiente" 
   }
   habitos.append(habito_usuario)
   return f"hola {nombre_usuario} estamos en el area de {area} y tu paso sera: {paso_1} durante {tiempo_paso} minutos. Estado: pendiente"
   

def eliminar_habito():
   if len(habitos) == 0:
      print("no hay habitos registrados")
   else:
      for index, areas in enumerate(habitos ,1):
         print(f"{index}. area: {areas['area']}\npaso: {areas['paso']}\ntiempo: {areas['tiempo']}\nestado: {areas['estado']}\n")
      opcion_eliminar = int(input("Que habito desea eliminar: ")) 
      if opcion_eliminar > len(habitos) or opcion_eliminar < 1:
         print("habito no existe ") 
      else:
         del habitos [opcion_eliminar - 1] 
         return "habito eliminado correctamente"

def ver_habito_completados():
   if len(habitos) == 0:
      print("no hay habitos registrados")
   else:
      for i in habitos:
         if i["estado"] == "completado":
               print(f"area: {i['area']}")
               print(f"paso: {i['paso']}")
               print(f"tiempo: {i['tiempo']}")
               print(f"estado: {i['estado']}\n")
         else:      
               print("no hay habitos completados")      

def ver_habito_pendiente():
   if len(habitos) == 0:
      print("no hay habitos registrados")
   else:
      for i in habitos:
         if i["estado"] == "pendiente":
               print(f"area: {i['area']}")
               print(f"paso: {i['paso']}")
               print(f"tiempo: {i['tiempo']}")
               print(f"estado: {i['estado']}\n")
         else:
            print("no hay habitos pendientes")      

habitos=[]

opcion_menu = ""
while opcion_menu != "9":
   print("MENU\n"
   "1. Deporte\n" \
   "2. Intelecto\n" \
   "3. Alimentacion\n" \
   "4. Economico\n"
   "5. ver habitos\n"
   "6. eliminar habito\n"
   "7. ver habitos completados\n"
   "8. ver habitos pendintes\n"
   "9. salir")

   opcion_menu = input("area a trabajar: ")

   if  opcion_menu not in ["1","2","3","4","5","6","7","8","9"]:
      print("Opcion no valida")

   elif opcion_menu == "1":
      print(habito("deporte"))

   elif opcion_menu == "2":
      print(habito("intelecto"))

   elif opcion_menu == "3":
      print(habito("alimentacion"))

   elif opcion_menu == "4":
      print(habito("economico"))
   
   elif opcion_menu == "5":
      if len(habitos) == 0:
         print("no hay habitos")
      else:
         for index, areas in enumerate(habitos ,1):
            print(f"{index}. area: {areas['area']}\npaso: {areas['paso']}\ntiempo: {areas['tiempo']}\nestado: {areas['estado']}\n")
         opcion_usuario = input("deseas marcar como completado algun habito: ").lower()
         if opcion_usuario == "si":
               opcion_habito = int(input("ingresa el numero del habito que deseas marcar como completado: "))
               habitos[opcion_habito - 1]["estado"] = "completado"
               print("habito modificado")
         elif opcion_usuario == "no":
               pass 
         ver_habito = input("desea ver el proceso de algun habito : ")
         if ver_habito == "si":
            for i in habitos:
               print(f"{index}. area: {areas['area']}\npaso: {areas['paso']}\ntiempo: {areas['tiempo']}\nestado(cambiado): {areas['estado']}\n")
         elif ver_habito == "no":
            pass
            
   elif opcion_menu == "6":
      print(eliminar_habito())
   elif opcion_menu == "7":
      ver_habito_completados()
   elif opcion_menu == "8":
      ver_habito_pendiente()
   elif opcion_menu == "9":
      break

def frase():
   frases_motivadoras = (
    "Un paso pequeño también cuenta.",
    "La constancia vale más que la perfección.",
    "Hoy no tienes que hacerlo todo, solo avanzar.",
    "Cada paso que das también es progreso.",
    "Tu disciplina se construye poco a poco.",
    "No se trata de correr, sino de no detenerte.",
    "Avanzar lento sigue siendo avanzar.",
    "Lo importante no es hacerlo perfecto, sino hacerlo.",
    "Tu esfuerzo de hoy puede cambiar tu mañana.",
    "A veces un solo paso es suficiente por hoy."
)
   return random.choice(frases_motivadoras)

print(frase())   