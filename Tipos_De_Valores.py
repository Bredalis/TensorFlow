
# Libreria

import tensorflow as tf

tensor_1 = tf.constant([1.5, 2.5, 3.5])
print(f"Tensor con valor conocido: \n{tensor_1}")

tensor_2 = tf.constant([6, 3, 3], dtype = tf.int16)
print(f"\nTensor de 3 columnas: \n{tensor_2}")

tensor_matriz = tf.constant([["c", "c"], ["c", "c"]])
print(f"\nTensor Matriz 2x2: \n{tensor_matriz}")

ceros = tf.zeros([3])
print(f"\nTensor de ceros: \n{ceros}")

unos = tf.ones([2, 3], dtype = tf.int32)
print(f"\nTensor de unos: \n{unos}")

fill = tf.fill([2, 3, 9], 8)
print(f"\nTensor Fill: \n{fill}")

tensor_linspace = tf.linspace(5., 9., 5)
print(f"\nTensor Linspace: \n{tensor_linspace}")