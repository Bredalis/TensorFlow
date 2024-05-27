
# Libreria

import tensorflow as tf

tensor_0 = tf.constant(4) 
print(f"Tensor de rango 0 (Escalar): \n{tensor_0}")

tensor_1 = tf.constant([1, 2, 3, 4])  
print(f"\nTensor de rango 1 (Vector): \n{tensor_1}")

tensor_2 = tf.constant([[1, 2, 3], [4, 5, 6]])
print(f"\nTensor de rango 2 (Matriz): \n{tensor_2}") 

tensor_3 = tf.constant([[[1], [2]], [[3], [4]]])
print(f"\nTensor de rango 3 (Cubo): \n{tensor_3}")
print(f"\nTensor de rango 4: \n{tf.zeros([3, 2, 4, 5])}")