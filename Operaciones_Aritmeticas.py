
import tensorflow as tf

# Tensores
tensor_1 = tf.constant([1, 2])
tensor_2 = tf.constant([3, 4])

print(f"Tensor 1: {tensor_1}")
print(f"Tensor 2: {tensor_2}")

# Operaciones
print(f"\nSuma: {tf.add(tensor_1, tensor_2)}")
print(f"Resta: {tf.subtract(tensor_1, tensor_2)}")
print(f"Multiplicación: {tf.multiply(tensor_1, tensor_2)}")
print(f"División: {tf.divide(tensor_1, tensor_2)}")

print(f"\nSuma sin función: {tensor_1 + tensor_2}")
print(f"Multiplicación sin función: {tensor_1 * tensor_2}")