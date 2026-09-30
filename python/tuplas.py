# Concepto: Tuplas

# Una tupla es muy similar a una lista (una colecciOn ordenada de elementos), pero con una
# diferencia crucial: son inmutables. Esto significa que una vez que se crea una tupla, no se
# puede modificar (no puedes añadir, eliminar ni cambiar elementos).

# Se definen utilizando parentesis () en lugar de corchetes [].

#¿Para que sirven en la practica?
#Se utilizan para datos que nunca deben cambiar a lo largo de la ejecucion del programa, como 
# coordenadas geograficas, configuraciones fijas del sistema (por ejemplo, una dirección IP y 
# puerto por defecto que no deben alterarse por error), o para proteger datos contra 
# modificaciones accidentales.

# EJEMPLO SENCILLO:

# Una tupla con datos de configuracion estaticos
configuracion_red = ("192.168.1.1", 8080)

# Si intentamos modificar un valor, Python lanzara un error:
# configuracion_red[1] = 443  -> Error (TypeError)

# EJEMPLO PRACTICO:

# Códigos HTTP estandar autorizados para una comprobacion rapida

codigos_permitidos = (200, 301, 302, 403, 404)

# Podemos consultar sus elementos igual que en las listas usando indices

print(f"El primer codigo permitido es: {codigos_permitidos[0]}")

# EJERCICIO

# Crea una tupla llamada credenciales_por_defecto que contenga un usuario (texto) y
# una contraseña por defecto (texto).

# Intenta imprimir únicamente el usuario utilizando su indice.

#(Opcional para pensar): ¿Qué pasaría si intentas usar .append("nuevo_valor") en una 
# tupla? Piensalo o pruebalo mentalmente.

credenciales_por_defecto = ("admin", "passroot")

print(f"{credenciales_por_defecto[0]}")
