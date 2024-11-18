
import tensorflow as tf

# Tensores
tensor_1d = tf.constant([[1, 2], [3, 4]])
tensor_modificado = tf.reshape(tensor_1d, [1, 4])
tensor_inverso = tf.reshape(tensor_1d, [-1])

# Información del tensor
print(f"Tensor 1d:\n{tensor_1d}")
print(f"\nTamaño del tensor: {tensor_1d.shape}")
print(f"Tamaño como lista: {tensor_1d.shape.as_list()}")
print(f"Cambiar tamaño a 1 fila y 4 columnas: {tensor_modificado}")
print(f"Cambiar tamaño a un tensor en reversa: {tensor_inverso}")