# Concepto: Operadores Logicos

# Ahora que sabemos tomar decisiones con if, ¿que pasa si necesitamos evaluar mas de una 
# condicion al mismo tiempo? Para eso existen los operadores logicos:

# and (Y): Devuelve True solo si ambas condiciones son verdaderas. Si una sola
# falla, todo es falso.

# or (O): Devuelve True si al menos una de las condiciones es verdadera.

# not (NO): Invierte el valor booleano (si es True lo vuelve False, y viceversa).

# ¿Para que sirven en ciberseguridad?
# Son indispensables para crear reglas de filtrado o deteccion complejas. Por ejemplo: una alerta
# solo debe saltar si la IP es desconocida Y el puerto es el 22 (SSH).

# EJEMPLO SENCILLO

# Operador and
usuario_valido = True
contraseña_correcta = True

if usuario_valido and contraseña_correcta:
    print("Acceso concedido.")
else:
    print("Acceso denegado.")
    
# EJEMPLO PRACTICO

puerto_destino = 21
es_ip_interna = False

# Queremos detectar si el puerto es critico (21) O la IP NO es interna
if puerto_destino == 21 or not es_ip_interna:
    print("¡Alerta! Trafico analizado con atencion especial.")    
    

# EJERCICIO

# Crea dos variables: usuario = "admin" y intentos_fallidos = 4.

# Utiliza una estructura condicional if con el operador and que evalue si:

# El usuario es igual a "admin" Y los intentos fallidos son mayores a 3.

# Si ambas condiciones se cumplen, imprime un mensaje de alerta de seguridad. Si no, 
# imprime que el estado es normal.

usuario = "admin"
intentos_fallidos = 4

if usuario == "admin" and intentos_fallidos >= 3:
    print("alerta de intrusos")
else:
    print("Estado: normal")
