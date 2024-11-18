
import tensorflow as tf

# Tipos de tensores
tensor_strings = tf.constant(
	["Hola", "TensorFlow", "String"], dtype = tf.string)

tensor_floats = tf.constant([3.14, 2.718, 1.0], dtype = tf.float32)
tensor_integers = tf.constant([1, 2, 3, 4], dtype = tf.int32)
tensor_booleans = tf.constant([True, False, True], dtype = tf.bool)

print(f"Tensor de strings: {tensor_strings}")
print(f"Tensor de floats: {tensor_floats}")
print(f"Tensor de enteros: {tensor_integers}")
print(f"Tensor de booleanos: {tensor_booleans}")