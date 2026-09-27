# ¿Qué son los Indices?
# Un indice es simplemente la posicion numerica que ocupa un elemento dentro de una 
# estructura ordenada (como una lista o un texto).

# En Python (y en la mayoria de los lenguajes de programacion), se empieza a contar desde el 0,
# no desde el 1.

# Indices positivos (de izquierda a derecha): Comienzan en 0 para el primer elemento.

# Indices negativos (de derecha a izquierda): Permiten contar desde el final hacia atras.
# El ultimo elemento es -1, el penultimo -2, etc.

# Ejemplo: 

puertos = [21, 22, 80, 443]
# Indices:   0   1   2    3
# Negativos:-4  -3  -2   -1

print(puertos[0])   # Imprime el primer puerto: 21
print(puertos[-1])  # Imprime el último puerto: 443

# ¿Que es el Slicing?

# El slicing es una tecnica que te permite extraer una porcion (un rango) de una lista o de un
# texto, en lugar de traer un solo elemento.

# Su sintaxis basica es: [inicio : fin]

# inicio: Es el indice donde empieza el corte (si se incluye).

# fin: Es el indice donde termina el corte (no se incluye; se detiene justo en el elemento anterior).

# Ejemplo:

puertos = [21, 22, 80, 443, 8080]

# Queremos desde el indice 1 hasta el 3
sub_lista = puertos[1:4] 
print(sub_lista)  # Resultado: [22, 80, 443] (extrajo los indices 1, 2 y 3, ignorando el 4 y el 0)
