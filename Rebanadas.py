
import tensorflow as tf
import numpy as np

# Tensor

t_1 = tf.constant([0, 1, 2, 3, 4, 5, 6, 7])

print("Rebanada\n", tf.slice(t_1, begin = [1], size = [3]))
print(t_1[1:4])
print(t_1[-3:])

# Tensor bidimensional

t_2 = tf.constant([
	[0, 1, 2, 3, 4],
	[5, 6, 7, 8, 9],
	[10, 11, 12, 13, 14],
	[15, 16, 17, 18, 19]
])

print(t_2[:-1, 1:3])

# Tensor alfanumerico

tensor_alfanumerico = tf.constant(list("abcdefghijklmnopqrstuvwxyz"))
print(tf.gather(tensor_alfanumerico, indices = [1, 17, 4, 3, 0, 11, 8, 18]))