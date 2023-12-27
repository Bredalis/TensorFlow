
# Libreria

import tensorflow as tf

ceros = tf.Variable(tf.zeros([1, 2, 3]))
print(f'Variable de ceros: \n{ceros}')

a = tf.Variable(0.0)
b = a + 1

print(f'\n{a}')
print(b)

# Agregar valores a una variable
a = tf.Variable(0.0)
a.assign_add(1)

print(f'\nLeer el valor de la variable: \n{a.read_value()}')