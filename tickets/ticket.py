import pickle   #guardar y cargar estructuras de datos en formato binario
import sys      #cerrar el programa
import os       #comandos del sistema, archivos, pantalla
import random   #generar números aleatorios

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear") #limpiara la pantalla no importa si esta en window o linux

def generar_numero_ticket(ticket): #generara ticket utilizando numero aleatorio
    while True:
        numero = random.randint(1000, 9999)
        if numero not in ticket: # si el numero no esta en uso
            return numero        #lo devolvera 

def cargar_tickets(nombre_archivo): #recibira el parametro(nombre_archivo) del cual queremos leer los tickets
    if os.path.isfile(nombre_archivo): #verifica si el archivo existe
        with open(nombre_archivo, "rb") as f: #(el archivo existe) 
            return pickle.load(f) #recupera los tickets guardados y los carga en memoria
    return {} #el archivo no existe: Retorna un diccionario vacío ({}) que indica que no hay tickets guardados todavía.

def guardar_tickets(nombre_archivo, ticket): #recibo 2 parametros el 1ro donde se guarda todo,2do el diccionario de tickets que queremos guardar
    with open(nombre_archivo, "wb") as f: #abre (o crea si no existe) el archivo con nombre nombre_archivo
        pickle.dump(ticket, f) 

def alta_ticket(ticket, nombre_archivo): 
    while True:   #permite al usuario cargar varios tickets seguidos sin volver al menú cada vez
        limpiar_pantalla()
        print("--- ALTA DE TICKET ---")
        nombre = input("Nombre: ")
        sector = input("Sector: ")
        asunto = input("Asunto: ")
        problema = input("Descripción del problema: ")

        numero_ticket = generar_numero_ticket(ticket) #se asegura que no esté repetido (no puede haber dos tickets con el mismo número)
        ticket[numero_ticket] = {  #agrega una entrada al diccionario ticket usando como clave el número generado (numero_ticket)
            "nombre": nombre, 
            "sector": sector,
            "asunto": asunto,
            "problema": problema
        }

        guardar_tickets(nombre_archivo, ticket)  #guarda todo el diccionario ticket en un archivo binario usando pickle.dump()

        print("\n Se genero el siguiente Ticket. Aquí están los detalles:\n")
        print(f"Número de Ticket : {numero_ticket}") 
        print(f"Nombre           : {nombre}")
        print(f"Sector           : {sector}")
        print(f"Asunto           : {asunto}")
        print(f"Descripción      : {problema}")
        print("\n Por favor, recuerde este número para futuras consultas.\n")

        otra = input("¿Desea crear otro ticket? (s/n): ").lower()   
        if otra != "s":   
            break

def leer_ticket(ticket):    
    while True:    
        limpiar_pantalla()
        print("--- LECTURA DE TICKET ---")
        try:     #codigo que puede fallar(si el usuario escribe letras, símbolos, o algo no convertible a numero ocurre error)
            numero = int(input("Ingrese el número de ticket: "))
        except ValueError:      #qué hacer si ocurre ese error 
            print(" Por favor ingrese un número válido.")
            input("Presione Enter para continuar...")#espera que el usuario presione Enter
            continue #vuelva directamente al inicio del while y le pide nuevamente el número

        if numero in ticket:    #verifica si el numero ingresado (numero) existe como clave en el diccionario ticket
            t = ticket[numero]   #accede al valor que está guardado en ticket[numero], que es otro diccionario
            print("\n Ticket encontrado:")
            print(f"Número de Ticket : {numero}")  
            print(f"Nombre           : {t['nombre']}")  
            print(f"Sector           : {t['sector']}")   
            print(f"Asunto           : {t['asunto']}")
            print(f"Descripción      : {t['problema']}")
        else:
            print(" No se encontró un ticket con ese número.")

        otra = input("\n¿Desea leer otro ticket? (s/n): ").lower()
        if otra != "s":
            break

def menu_principal():  
    nombre_archivo = "tickets.bin"  #contiene el nombre del archivo donde se van a guardar o leer los tickets 
    ticket = cargar_tickets(nombre_archivo)  #carga los tickets guardados o devuelve {} si no hay
    
    while True:   
        limpiar_pantalla()
        print("===SISTEMA DE TICKET ===")
        print("=== MENU PRINCIPAL ===")
        print("1 _ Alta Ticket")
        print("2 _ Leer Ticket") #ticket que guarde: 6161, 3153 y 7511
        print("3 _ Salir")
        opcion = input("Seleccione una opción: ")  

        if opcion == "1":
            alta_ticket(ticket, nombre_archivo) #llama a la funcion 'alta_ticket'(Le pasa el diccionario ticket y el archivo "tickets.bin" para guardar el nuevo ticket)
        elif opcion == "2":
            leer_ticket(ticket) #llama a la funcion 'leer_ticket'(Le pasa el diccionario ticket cargado desde el archivo)
        elif opcion == "3":
            confirmar = input("¿Está seguro que desea salir? (s/n): ").lower()  
            if confirmar == "s":
                print(" Programa finalizado.")
                sys.exit()  #cierra por completo el programa
        else:
            print(" Opción no válida.")
            input("Presione Enter para continuar...")

# Ejecutar el programa
menu_principal()

