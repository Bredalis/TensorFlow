
import tensorflow as tf

a = tf.constant([[1, 2], [3, 4]])

print(f"Tamaño: {a.shape}")
print(f"Tamaño como lista: {a.shape.as_list()}")
print(f"Cambiar tamaño a 1 fila y 4 columnas: \n{tf.reshape(a, [1, 4])}")
print(f"Cambiar tamaño a un vector en reversa: \n{tf.reshape(a, [-1])}")