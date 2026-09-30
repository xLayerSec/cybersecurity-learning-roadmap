# Concepto: Entrada y salida de datos

# Salida de datos (print()): Ya lo conoces; sirve para mostrar informacion en la
# pantalla de la terminal.

# Entrada de datos (input()): Permite pausar el programa para que el usuario escriba algo 
# desde el teclado y presione Enter. Todo lo que el usuario escribe a traves de input() 
# se almacena en Python por defecto como una cadena de texto (str), 
# sin importar si escribiste un numero.

# EJEMPLO SENCILLO

# Solicitamos el nombre del analista por teclado
nombre = input("Ingresa tu nombre de usuario: ")

# Mostramos un saludo personalizado utilizando la entrada
print(f"Hola, {nombre}. Bienvenido al sistema.")

# EJEMPLO PRACTICO:

# Pedimos un puerto al usuario
puerto_ingresado = input("Introduce el puerto a escanear: ")

# Como input() devuelve un string, debemos convertirlo a entero (int) si queremos hacer operaciones numericas
puerto_num = int(puerto_ingresado)

if puerto_num == 80:
    print("Analizando trafico web estandar (HTTP)...")
else:
    print(f"Analizando puerto personalizado: {puerto_num}")
    
# EJERCICIO:

# Utiliza la función input() para pedirle al usuario que introduzca una dirección IP 
# (por ejemplo: "Introduce la IP objetivo: ") y guardala en una variable llamada ip_objetivo.

# imprime un mensaje que confirme el escaneo combinando el texto introducido con un f-string,


ip_objetivo = input("Introduce la IP objetivo: ")

if ip_objetivo == "":
    print("no se recibio ninguna IP")
    
else:
    print(f"IP: {ip_objetivo} recibida con exito")
