
# Libreria

import tensorflow as tf

lista_irregular = [[0, 1, 2, 3], [4, 5], [6, 7, 8], [9]]
print(f"Lista irregular: \n{lista_irregular}")

tensor_irregular = tf.ragged.constant(lista_irregular)
print(f"\nTensor irregular: \n{tensor_irregular}")

print(f"Tamaño: {tensor_irregular.shape}")