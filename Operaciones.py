
# Libreria

import tensorflow as tf

a = tf.constant([1, 2, 3])

print(f"Valor mas alto: {tf.reduce_max(a)}")
print(f"Index del valor mas alto: {tf.argmax(a)}")