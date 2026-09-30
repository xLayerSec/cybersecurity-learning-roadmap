# Concepto: Bucle while, break y continue

# Ya sabemos usar el bucle for para recorrer elementos que ya conocemos. Pero ¿que pasa
# cuando no sabemos cuantas veces se va a repetir algo, sino que dependemos de que ocurra
# una condicion? Para eso usamos el bucle while (mientras).

# while: Se repetira una y otra vez mientras la condicion especificada sea verdadera 
# (True). ¡Cuidado con crear bucles infinitos donde la condicion nunca cambie a False!

# break: Sirve para romper o salir de un bucle de manera abrupta antes de que termine
# por si solo.

# continue: Salta la iteracion actual y pasa inmediatamente a la siguiente repeticion del bucle.

# EJEMPLO SENCILLO:

# Un contador simple que simula reintentos de conexion
intentos = 0

while intentos < 3:
    print(f"Intentando conectar... (Intento {intentos + 1})")
    intentos = intentos + 1  # Es vital modificar la variable para que el bucle termine

print("Conexion finalizada.")

# EJEMPLO PRACTICO:

puertos_a_escanear = [21, 80, 443, 8080]

for puerto in puertos_a_escanear:
    if puerto == 80:
        print("Puerto 80 ignorado temporalmente.")
        continue  # Salta esta iteracion y pasa a la siguiente
        
    if puerto == 443:
        print("¡Puerto crítico 443 encontrado! Deteniendo escaneo.")
        break  # Rompe y sale completamente del bucle
        
    print(f"Analizando puerto {puerto}...")
    

# EJERCICIO:

# Crea una variable llamada intentos_fallidos con valor 0.

# Utiliza un bucle while que se mantenga ejecutandose mientras intentos_fallidos sea menor a 3.

# Dentro del bucle, imprime "Alerta: Fallo de autenticacion" y aumenta en 1 el valor de intentos_fallidos 
# en cada vuelta (para evitar un bucle infinito).

# Fuera del bucle, imprime "Bloqueo de seguridad activado".

intentos_fallidos = 0

while intentos_fallidos < 3:
    print("Alerta: Fallo de autenticacion")
    intentos_fallidos = intentos_fallidos + 1

print("bloque de seguridad activado")
