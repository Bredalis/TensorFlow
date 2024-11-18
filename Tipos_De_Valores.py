
import tensorflow as tf

# Tensores
tensor_1 = tf.constant([1.5, 2.5, 3.5])
tensor_2 = tf.constant([6, 3, 3], dtype = tf.int16)
tensor_matriz = tf.constant([["c", "c"], ["c", "c"]])
tensor_zeros = tf.zeros([3])
tensor_ones = tf.ones([2, 3], dtype = tf.int32)
tensor_fill = tf.fill([2, 3, 9], 8)
tensor_linspace = tf.linspace(5., 9., 5)

# Mostrar tensores
print(f"Tensor con valor conocido:\n{tensor_1}")
print(f"\nTensor de 3 columnas:\n{tensor_2}")
print(f"\nTensor matriz 2x2:\n{tensor_matriz}")
print(f"\nTensor de ceros:\n{tensor_zeros}")
print(f"\nTensor de unos:\n{tensor_ones}")
print(f"\nTensor fill:\n{tensor_fill}")
print(f"\nTensor linspace:\n{tensor_linspace}")