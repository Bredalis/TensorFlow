
import tensorflow as tf

numero_aleatorio = tf.random.normal([10], dtype = tf.float64)
print(f"Número aleatorio:\n{numero_aleatorio}")

# Transformación de vector a matriz
vector = tf.constant([1., 2., 3., 4.])
matriz = tf.reshape(vector, [2, 2])

print(f"\nVector:\n{vector}")
print(f"\nMatriz:\n{matriz}")

# Extracción de datos en rebanas
matriz_2 = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
slice_matriz = tf.slice(matriz_2, [1, 1], [2, 2])

print(f"\nMatriz 2:\n{matriz_2}")
print(f"\nMatriz Slice:\n{slice_matriz}")

# Vectores
vector_1 = tf.constant([1, 2])
vector_2 = tf.constant([3, 4])
vector_3 = tf.constant([5, 6])

print(f"\nVector 1: {vector_1}")
print(f"Vector 2: {vector_2}")
print(f"Vector 3: {vector_3}")

# Unión de vectores
vector_4 = tf.stack([vector_1, vector_2, vector_3])
print(f"\nUnión de vectores:\n{vector_4}")