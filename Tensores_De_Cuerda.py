
# Libreria

import tensorflow as tf

# Tensores de cuerda

tensor_strings = tf.constant(["Hello World", "Hi", "TensorFlow"])

print("Tensor de cuerda: \n", tensor_strings)
print("\nTensor separado por espacios: \n", 
	tf.strings.split(tensor_strings, sep = " "))

# Pasar de tensor string a int

texto = tf.constant("1 10 100")
print("\n", texto)

print(tf.strings.to_number(tf.strings.split(texto, " ")))