
# Libreria

import tensorflow as tf

# Tensor de rango 0 o escalar
tensor_0 = tf.constant(4) 
print(f"Tensor de rango 0 (Escalar): \n{tensor_0}")

# Tensor de rango 1 o vector
tensor_1 = tf.constant([1, 2, 3, 4])  
print(f"\nTensor de rango 1 (Vector): \n{tensor_1}")

# Tensor de rango 2 o matriz
tensor_2 = tf.constant([[1, 2, 3], [4, 5, 6]])
print(f"\nTensor de rango 2 (Matriz): \n{tensor_2}") 

# Tensor de rango 3 o cubo
tensor_3 = tf.constant([[[1], [2]], [[3], [4]]])
print(f"\nTensor de rango 3 (Cubo): \n{tensor_3}")

# Tensor de rango 4
print(f"\nTensor de rango 4: \n{tf.zeros([3, 2, 4, 5])}")