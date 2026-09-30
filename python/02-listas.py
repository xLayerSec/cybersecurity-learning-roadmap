# Concepto: Listas

# Una lista es una coleccion ordenada y mutable (modificable) de elementos. Se delimitan con
# corchetes [] y sus elementos se separan por comas. Pueden contener cualquier tipo de dato
# (incluso mezclar textos, numeros y booleanos).


# Ejemplo sencillo

# Una lista con nombres de herramientas de seguridad
herramientas = ["nmap", "wireshark", "burpsuite"]

# Una lista mixta (que contiene diferentes tipos de datos)
configuracion_objetivo = ["192.168.1.10", 80, True]


# Ejemplo practico

puertos_comunes = [21, 22, 80, 443, 8080]

# Podemos añadir un nuevo puerto a la lista usando el metodo .append()
puertos_comunes.append(3306)

print(puertos_comunes)
# Resultado: [21, 22, 80, 443, 8080, 3306]

# Ejercicio

# Crea una lista llamada ips_sospechosas que contenga al menos tres direcciones IP en formato de texto (str).
# Utiliza el método .append() para añadir una cuarta IP a esa lista.
# Imprime la lista completa resultante.

ips_sospechosas = ["192.168.100.1", "192.168.100.20", "192.168.100.100"]

ips_sospechosas.append("192.168.100.14")

print(ips_sospechosas)
