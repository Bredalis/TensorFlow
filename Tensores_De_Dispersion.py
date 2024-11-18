
import tensorflow as tf

# Crear un tensor disperso
tensor_disperso = tf.sparse.SparseTensor(
    indices = [[0, 0], [1, 2]], 
    values = [1, 2],
    dense_shape = [3, 4]
)

# Mostrar el tensor disperso y convertirlo a denso
print("Tensor disperso:\n", tensor_disperso)
tensor_denso = tf.sparse.to_dense(tensor_disperso)
print("\nTensor convertido a denso:\n", tensor_denso)

# Convertir cadenas de texto a bytes y enteros
string_tensor = tf.constant("HOLA")
bytes_divididos = tf.strings.bytes_split(string_tensor)
bytes_enteros = tf.io.decode_raw(string_tensor, tf.uint8)

print("\nConversión de cadenas a bytes y enteros:")
print("Bytes divididos:", bytes_divididos)
print("Bytes como enteros:", bytes_enteros)