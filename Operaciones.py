
# Libreria

import tensorflow as tf

a = tf.constant([1, 2, 3])

# Encontrar el valor mas alto
print(f"Valor mas alto: {tf.reduce_max(a)}")

# Encontrar el index del valor mas alto
print(f"Index del valor mas alto: {tf.argmax(a)}")