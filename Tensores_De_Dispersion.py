
# Libreria

import tensorflow as tf

# Estructura del tensor
tensor_disperso = tf.sparse.SparseTensor(
    indices = [[0, 0], [1, 2]], values = [1, 2], dense_shape = [3, 4])

print(f"Tensor de dispersion: \n{tensor_disperso}")
print("\n", tf.sparse.to_dense(tensor_disperso))

# Convirtiendo de strings a bytes
bytes_strings = tf.strings.bytes_split(tf.constant("HOLA"))
bytes_ints = tf.io.decode_raw(tf.constant("HOLA"), tf.uint8)

print("\nStrings - Bytes\n")
print(bytes_strings)
print(bytes_ints)