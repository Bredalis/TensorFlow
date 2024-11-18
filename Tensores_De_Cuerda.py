
import tensorflow as tf

tensor_strings = tf.constant(["Hello World", "Hi", "TensorFlow"])
print("Tensor de cadenas:\n", tensor_strings)

# Dividir cada cadena por espacios
split_strings = tf.strings.split(tensor_strings, sep = " ")
print("\nTensor dividido por espacios:\n", split_strings)

# Convertir un tensor de texto a enteros
numeric_text = tf.constant("1 10 100")
print("\nTexto como tensor:\n", numeric_text)

# Convertir el texto en números
split_numbers = tf.strings.split(numeric_text, sep = " ")
converted_numbers = tf.strings.to_number(split_numbers)
print("\nTexto convertido a números:\n", converted_numbers)