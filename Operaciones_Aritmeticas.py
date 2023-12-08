
# Libreria

import tensorflow as tf

# Vectores

v1 = tf.constant([1, 2])
v2 = tf.constant([3, 4])

# Operaciones

suma = tf.add(v1, v2)
resta = tf.subtract(v1, v2)
multiplicacion = tf.multiply(v1, v2)
division = tf.divide(v1, v2)

print(f"Suma: {suma}")
print(f"\nResta: {resta}")
print(f"\nMultiplicacion: {multiplicacion}")
print(f"\nDivision: {division}")

print("\nSuma sin funcion:", v1 + v2, "\n")
print("Multiplicacion sin funcion:", v1 * v2, "\n")