
# Libreria

import tensorflow as tf

numero_aleatorio = tf.random.normal([10], dtype = tf.float64)
print(f"Numero aleatorio: \n{numero_aleatorio}")

# Transformacion de vector a matriz

vector = tf.constant([1., 2., 3., 4.])
matriz = tf.reshape(vector, [2, 2])

print(f"\nVector: \n{vector}")
print(f"\nMatriz: \n{matriz}")

# Extraccion de datos en rebanas

matriz_2 = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
slice_matriz = tf.slice(matriz_2, [1, 1], [2, 2])

print(f"\nMatriz 2: \n{matriz_2}")
print(f"\nMatriz Slice: \n{slice_matriz}")

# Vectores

v1 = tf.constant([1, 2])
v2 = tf.constant([3, 4])
v3 = tf.constant([5, 6])

print(f"\nVector 1: {v1}")
print(f"\nVector 2: {v2}")
print(f"\nVector 3: {v3}")

# Union de vectores

v4 = tf.stack([v1, v2, v3])
print(f"\nUnion de vectores: \n{v4}")