# Concepto: Diccionarios

# Un diccionario es una estructura de datos que almacena informaciOn en parejas de clave-valor 
# (key-value), muy similar a un diccionario de la vida real donde buscas una palabra (clave) para 
# encontrar su definición (valor).

# Se definen utilizando llaves {}. Las claves deben ser Unicas e inmutables (generalmente textos
# o numeros), y los valores pueden ser de cualquier tipo de dato (incluso listas u otros 
# diccionarios).

# ¿Por que son tan importantes?
# Porque nos permiten estructurar datos complejos con significado propio, en lugar de depender
# unicamente de la posición numerica como en las listas. Son ideales para almacenar 
# configuraciones, perfiles de usuario o registros de eventos. 

# EJEMPLO SENCILLO:

# Un diccionario con informacion de una cuenta de usuario

usuario = {
    "nombre": "admin",
    "id": 101,
    "activo": True
}

# Para acceder a un valor, llamamos a su clave entre corchetes
print(usuario["nombre"])  # Resultado: admin


# EJEMPLO PRACTICO:

servicio_detectado = {
    "puerto": 22,
    "servicio": "SSH",
    "version": "OpenSSH 8.2p1",
    "vulnerable": False
}

# Podemos actualizar un valor existente o añadir uno nuevo fácilmente
servicio_detectado["vulnerable"] = True  # Modificamos un valor
servicio_detectado["protocolo"] = "TCP"  # Añadimos una nueva clave-valor

print(servicio_detectado)

# EJERCICIO

# Crea un diccionario llamado objetivo_red que contenga las siguientes tres claves y sus respectivos valores:

# "ip": "192.168.1.100" (texto)

# "puerto_principal": 80 (entero)

# "estado": True (booleano)

# Imprime únicamente el valor de la clave "ip" utilizando el diccionario.
# Añade una nueva clave llamada "sistema_operativo" con el valor "Linux" al diccionario existente.

objetivo_red = {
    "ip": "192.168.1.100",
    "puerto_principal": 80,
    "estado": True
}

print(objetivo_red["ip"])

objetivo_red["sistema_operativo"] = "Linux"

print(objetivo_red)
