# Concepto: Scope

# Variables Locales: Son las que se crean dentro de una funcion (como los parametros o las
# variables internas). Solo existen mientras la funcion se esta ejecutando; una vez que la
# funcion termina, desaparecen de la memoria. No puedes usarlas fuera de esa funcion.

# Variables Globales: Son las que se declaran fuera de cualquier funcion 
# (en el "cuerpo principal" del script). Se pueden consultar desde cualquier parte del programa
# (aunque modificarlas desde dentro de una funcion requiere reglas especiales que veremos mas adelante).

# EJEMPLO SENCILLO:

# Variable global
modo_seguro = True

def mostrar_modo():
    # Variable local (solo vive aquí dentro)
    mensaje_interno = "Modo activo"
    print(mensaje_interno)
    print(modo_seguro)  # Podemos leer una variable global sin problema

mostrar_modo()

# Si intentamos hacer esto afuera, dara error:
# print(mensaje_interno) -> NameError: name 'mensaje_interno' is not defined

# EJEMPLO PRACTICO:

# 1. Aqui creamos el parametro (puertos_abiertos es como una "etiqueta vacia" que espera recibir datos)
def calcular_riesgo(puertos_abiertos):
    riesgo = len(puertos_abiertos) * 10
    return riesgo

# 2. Creamos la variable con los datos reales en el programa principal
puertos = [22, 80, 443]

# 3. EL MOMENTO CLAVE: Aqui es donde llamamos a la funcion y le PASAMOS el argumento (mis_puertos)
nivel_calculado = calcular_riesgo(puertos) 

print(f"Puntuación de riesgo: {nivel_calculado}")


# EJERCICIO

def registrar_IP():
    ip_interna = "192.168.1.5"
    print(ip_interna)

registrar_IP()
print(ip_interna)  # <-- ¿Que crees que pasara en esta ultima linea?


# Sin ejecutarlo todavía, ¿que crees que ocurrira cuando el programa llegue a la ultima linea
# (print(ip_interna))?

# R= nos dara un error

# ¿Por que crees que Python reacciona de esa manera basandote en lo que acabamos de explicar
# sobre variables locales?

# R= por que ip_interna es una variable local entonces al ejecutarla dice que no esta definida esa variable 
