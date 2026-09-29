# Concepto: Funciones

# Una funcion es un bloque de codigo reutilizable que realiza una tarea especifica. Se define con
# la palabra clave def.

# Parametros: Son las variables "variables" que la funcion recibe como datos de entrada 
# (se definen entre los parentesis al crearla).

# Argumentos: Son los valores reales que le pasamos a la funcion cuando la llamamos.

# return: Permite que la funcion devuelva un resultado hacia afuera para que pueda ser
# utilizado por el resto del programa (si no lleva return, la función simplemente ejecuta su 
# tarea pero no entrega ningun valor final).

# EJEMPLO SENCILLO

# Definimos la funcion que saluda a un usuario
def saludar_analista(nombre):
    mensaje = f"Bienvenido al sistema, {nombre}"
    return mensaje  # Devolvemos el resultado

# Llamamos a la funcion pasando un argumento
resultado = saludar_analista("Carlos")
print(resultado)

# EJEMPLO PRACTICO:

def evaluar_puerto(puerto):
    if puerto == 21 or puerto == 22 or puerto == 80:
        return "Puerto critico detectado"
    else:
        return "Puerto estandar"

# Usamos la funcion multiples veces con distintos valores
print(evaluar_puerto(22))   # Resultado: Puerto critico detectado
print(evaluar_puerto(443))  # Resultado: Puerto estándar

# EJERCICIO:

# Define una funcion llamada verificar_intentos que reciba un parametro numerico 
# llamado intentos.

# Dentro de la funcion, haz que si intentos es mayor o igual a 3, devuelva el texto
# "Alerta de seguridad". De lo contrario, que devuelva "Estado normal".

# Fuera de la funcion, llama a tu funcion pasandole el numero 4 como argumento y guarda
# el resultado en una variable llamada estado_actual.

# Imprime la variable estado_actual.

def verificar_intentos(intentos):
    if intentos >= 3:
        return("Alerta de seguridad")
    else:
        return("Estado Normal")
        
estado_actual = verificar_intentos(1)

print(estado_actual)
