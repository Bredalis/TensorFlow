
# Libreria

import tensorflow as tf

a = tf.constant([1, 2, 3])

# Informacion

print('Tipo de datos:', a.dtype)
print('\nDimension:', a.ndim)
print('Tamaño del tensor:', a.shape)
print('Total de elementos:', tf.size(a).numpy())