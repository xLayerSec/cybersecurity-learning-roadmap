# Concepto: Operadores y Condicionales

# Operadores de comparacion: Nos permiten comparar valores y devuelven un booleano
# (True o False):

# == (Igual a)

# != (Diferente de)

# > (Mayor que), < (Menor que)

# >= (Mayor o igual), <= (Menor o igual)


# Condicionales (if / elif / else): Permiten que el flujo del programa cambie segun si una condicion es
# verdadera o falsa.

# if: Si se cumple la condicion, ejecuta su bloque.

# elif : Si la condicion anterior no se cumplio, prueba esta nueva condicion.

# else: Si ninguna de las anteriores se cumplio, ejecuta este bloque por defecto.

#EJEMPLO SENCILLO

intentos_fallidos = 4

if intentos_fallidos > 3:
    print("¡Alerta! Demasiados intentos fallidos.")
else:
    print("Acceso permitido.")
    
    
# EJEMPLO PRACTICO

codigo_estado = 403

if codigo_estado == 200:
    print("Recurso accesible.")
elif codigo_estado == 403 or codigo_estado == 401:
    print("Acceso prohibido o no autorizado.")
else:
    print(f"Estado desconocido: {codigo_estado}") 
    
# EJERCICIO

# Crea una variable llamada nivel_amenaza con un valor numerico entero (por ejemplo, 8).

# Utiliza una estructura condicional (if / elif / else):

# Si el nivel es mayor o igual a 8, imprime "Nivel critico: Activar contramedidas".

# Si esta entre 4 y 7 (puedes usar >= 4), imprime "Nivel moderado: Monitorear de cerca".

# Si es menor a 4, imprime "Nivel bajo: Sistema seguro".


nivel_amenaza = 2

if nivel_amenaza >= 8:
    print("Nivel critico: Activar contramedidas")
elif nivel_amenaza >= 4:
    print("Nivel moderado: monitorear de cerca")
else:
    print("Nivel bajo: sitema seguro")
