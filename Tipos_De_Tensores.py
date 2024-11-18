
import tensorflow as tf

escalar = tf.constant(4) 
print(f"Tensor de rango 0 (Escalar): {escalar}")

vector = tf.constant([1, 2, 3, 4])  
print(f"Tensor de rango 1 (Vector): {vector}")

matriz = tf.constant([[1, 2, 3], [4, 5, 6]])
print(f"\nTensor de rango 2 (Matriz):\n{matriz}") 

cubo  = tf.constant([[[1], [2]], [[3], [4]]])
print(f"\nTensor de rango 3 (Cubo):\n{cubo }")
print(f"\nTensor de rango 4:\n{tf.zeros([3, 2, 4, 5])}")