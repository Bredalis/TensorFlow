
import tensorflow as tf

tensor_1d = tf.constant([1, 2, 3])

# Mostrar información del tensor
print(f"Tensor 1d: {tensor_1d}")
print(f"Tipo de datos: {tensor_1d.dtype}")
print(f"Dimension: {tensor_1d.ndim}")
print(f"Tamaño del tensor: {tensor_1d.shape}")
print("Total de elementos:", tf.size(tensor_1d).numpy())