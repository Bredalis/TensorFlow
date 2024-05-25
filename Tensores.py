
# Libreria

import tensorflow as tf

# Tensor de strings
tensor_strings = tf.constant(
	["Hola", "TensorFlow", "String"], dtype = tf.string)

print(f"Tensor de strings: \n{tensor_strings}")

# Tensor de floats
tensor_floats = tf.constant([3.14, 2.718, 1.0], dtype = tf.float32)
print(f"\nTensor de floats: \n{tensor_floats}")

# Tensor de enteros
tensor_integers = tf.constant([1, 2, 3, 4], dtype = tf.int32)
print(f"\nTensor de enteros: \n{tensor_integers}")

# Tensor de booleanos
tensor_booleans = tf.constant([True, False, True], dtype = tf.bool)
print(f"\nTensor de booleanos: \n{tensor_booleans}")	 