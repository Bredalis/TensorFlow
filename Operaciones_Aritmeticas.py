
# Libreria

import tensorflow as tf

# Vectores

v_1 = tf.constant([1, 2])
v_2 = tf.constant([3, 4])

# Operaciones

suma = tf.add(v_1, v_2)
resta = tf.subtract(v_1, v_2)
multiplicacion = tf.multiply(v_1, v_2)
division = tf.divide(v_1, v_2)

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicacion: {multiplicacion}")
print(f"Division: {division}")

print("\nSuma sin funcion:", v_1 + v_2)
print("Multiplicacion sin funcion:", v_1 * v_2)