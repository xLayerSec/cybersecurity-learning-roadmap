# Concepto: Sets

# Un set es una coleccion desordenada y unica de elementos. Se definen utilizando llaves {} 
# (igual que los diccionarios, pero sin las parejas de clave-valor).

# Tiene dos caracteristicas principales que los hacen sumamente utiles:

# No permiten duplicados: Si intentas añadir un elemento que ya existe en el set, Python lo ignora 
# automaticamente.

# Operaciones matematicas de conjuntos: Permiten hacer operaciones logicas muy
# potentes como uniones, intersecciones y diferencias de manera rapidisima.

# ¿Para que sirven en ciberseguridad o desarrollo?
# Son ideales cuando necesitas limpiar listas con IPs o puertos repetidos (por ejemplo, para
# obtener una lista unica de objetivos tras un escaneo masivo) o para comparar rapidamente que 
# elementos estan presentes en un registro y ausentes en otro.

# EJEMPLO SENCILLO

# Un set de puertos detectados (nota que repetimos el 80)

puertos_detectados = {80, 443, 80, 22, 443}

print(puertos_detectados)
# Resultado automático (elimina duplicados y el orden puede variar): {80, 22, 443}

# EJEMPLO PRACTICO

fuente_a = {"192.168.1.10", "192.168.1.50", "10.0.0.5"}
fuente_b = {"192.168.1.50", "172.16.0.2", "10.0.0.5"}

# Encontramos la interseccion (IPs comunes)
ips_comunes = fuente_a.intersection(fuente_b)
print(ips_comunes)  # Resultado: {'192.168.1.50', '10.0.0.5'}

# EJERCICIO

# Crea un set llamado logs_error que contenga los siguientes códigos de error
# repetidos: 404, 500, 404, 403, 500.

# Imprime el set para comprobar como Python elimina los duplicados automaticamente.

# Añade el código 502 utilizando el metodo .add().

logs_error = {404, 500, 404, 403, 500}

print(logs_error)

logs_error.add(502)

print(logs_error)
