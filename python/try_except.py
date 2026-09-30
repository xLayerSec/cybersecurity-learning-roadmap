# Concepto: Manejo de errores y Excepciones (try / except)

# El manejo de excepciones con try y except es la tecnica defensiva para evitar esto. Le dice a Python:

# try (Intenta): "Ejecuta este bloque de codigo que podría ser peligroso".

# except (Excepto / Si falla): "Si ocurre un error especifico, no dejes que el programa
# se rompa; en su lugar, captura el error y ejecuta este plan de emergencia".

# ¿Por que es vital en desarrollo y ciberseguridad?
# Porque un script de analisis o automatizacion nunca debe detenerse por completo solo 
# porque un archivo no existe, una IP no responde o un usuario ingreso un dato mal. Debe manejar 
# el error con elegancia y continuar.

# EJEMPLO SENCILLO:

# Intentamos dividir un numero entre cero
try:
    resultado = 10 / 0
    print(resultado)
except ZeroDivisionError:
    print("¡Error! No se puede dividir entre cero.")
    
# EJEMPLO PRACTICO:

entrada_usuario = "abc"

try:
    # Intentamos convertir texto a numero entero
    puerto = int(entrada_usuario)
    print(f"Puerto configurado: {puerto}")
except ValueError:
    print("Error: Debes ingresar un numero valido, no letras.")
    
# EJERCICIO

# Crea una variable llamada puerto_texto = "no_es_un_puerto".

# Utiliza una estructura try / except.

# Dentro del try, intenta convertir puerto_texto en un numero entero usando
# int(puerto_texto) y guardalo en una variable.

# En el except, captura especificamente el error ValueError e imprime un mensaje de
# advertencia que diga: "Fallo en la conversion del puerto: formato invalido".

puerto_texto = "no_es_un_puerto"

try:
    el_puerto = int(puerto_texto)
    print("puerto abierto")
    
except ValueError:
    print("Fallo en la conversion del puerto: formato invalido")
    
