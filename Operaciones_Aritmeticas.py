
# Libreria

import tensorflow as tf

# Vectores

v_1 = tf.constant([1, 2])
v_2 = tf.constant([3, 4])

# Operaciones

print(f"Suma: {tf.add(v_1, v_2)}")
print(f"Resta: {tf.subtract(v_1, v_2)}")
print(f"Multiplicacion: {tf.multiply(v_1, v_2)}")
print(f"Division: {tf.divide(v_1, v_2)}")

print("\nSuma sin funcion:", v_1 + v_2)
print("Multiplicacion sin funcion:", v_1 * v_2)