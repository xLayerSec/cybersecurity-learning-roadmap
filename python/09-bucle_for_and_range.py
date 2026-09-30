# Concepto: Bucles for y range()

# El bucle for sirve para repetir una tarea o recorrer cada uno de los elementos de una
# colección (como listas, tuplas o textos) de forma automatica, sin tener que escribir la misma
# linea una y otra vez.

# Cuando queremos repetir una acción un numero especifico de veces (por ejemplo, contar o 
# simular 5 intentos), lo combinamos con range():

# range(3) genera una secuencia de numeros del 0 al 2 (tres numeros en total).

#  EJEMPLO SENCILLO:

# Recorrer una lista de puertos automaticamente
puertos = [21, 22, 80, 443]

for puerto in puertos:
    print(f"Analizando puerto: {puerto}")
    
# EJEMPLO PRACTICO:

print("Iniciando escaneo rapido de ID internos...")

for i in range(3):
    print(f"Comprobando secuencia numero: {i}")
    
# EJERCICIO:

# Crea una lista llamada servicios que contenga tres textos: "FTP", "SSH", y "HTTP".

# Utiliza un bucle for para recorrer cada servicio de la lista.

# Dentro del bucle, imprime un mensaje por cada servicio que siga este formato exacto: 
# [+] Servicio detectado: <nombre_del_servicio>.

servicios = ["FTP", "SSH", "HTTP"]

for servicio in servicios:
    print(f"[+] Servicio detectado: {servicio}")
    
