#1. Concepto: Variables y Tipos de Datos Básicos

# Una variable es un valor que almacenamos en en la memoria RAM
# de nuestro dispositivo para usarlo mas tarde 

#TIPOS DE DATOS BASICOS

# int (Enteros): Numeros sin decimales (ej. 42, -7).

# float (Decimales): Numeros con punto flotante (ej. 3.14, 0.001).

# str (Cadenas de texto): Texto delimitado por comillas simples o dobles (ej. "Hola, mundo", 'admin').

# bool (Booleanos): Valores de veracidad, solo pueden ser True o False.

# EJERCICIO

# Crea un pequeño script donde declares tres variables:

# Una variable para almacenar el nombre de una herramienta de red (tipo str).
# Una variable para la cantidad de puertos escaneados (tipo int).
# Una variable booleana que indique si el escaneo finalizó con éxito (True o False).

# Luego, imprime un mensaje en pantalla que combine las tres variables utilizando la función print().

tool = "ReconLayer"
puertos_escaneados = 10
puertos_escaneados = puertos_escaneados / 2
escaneo_exitoso = True

print(f"{tool} {puertos_escaneados} {escaneo_exitoso}")
