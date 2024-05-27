
# Libreria

import tensorflow as tf

tensor_strings = tf.constant(
	["Hola", "TensorFlow", "String"], dtype = tf.string)

tensor_floats = tf.constant([3.14, 2.718, 1.0], dtype = tf.float32)
tensor_integers = tf.constant([1, 2, 3, 4], dtype = tf.int32)
tensor_booleans = tf.constant([True, False, True], dtype = tf.bool)

print(f"Tensor de strings: \n{tensor_strings}")
print(f"\nTensor de floats: \n{tensor_floats}")
print(f"\nTensor de enteros: \n{tensor_integers}")
print(f"\nTensor de booleanos: \n{tensor_booleans}")	 