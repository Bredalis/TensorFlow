
import tensorflow as tf

ceros = tf.Variable(tf.zeros([1, 2, 3])).numpy()
print("Variable de ceros:\n", ceros)

a = tf.Variable(0.0)
b = a + 1

print(a.numpy())
print(b.numpy())

c = tf.Variable(0.0)
c.assign_add(2)

print("Leer el valor de una variable:\n", c.read_value().numpy())