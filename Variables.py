
import tensorflow as tf

tensor_zeros = tf.Variable(tf.zeros([1, 2, 3])).numpy()
print("Tensor de ceros:\n", tensor_zeros)

# Operaciones con una variable escalar
scalar_a = tf.Variable(0.0)  # Inicializa una variable escalar con valor 0.0
scalar_b = scalar_a + 1  # Operación directa (no modifica scalar_a)

print("\nValor inicial de 'scalar_a':", scalar_a.numpy())
print("Resultado de 'scalar_a + 1':", scalar_b.numpy())

# Modificación en una variable escalar
scalar_c = tf.Variable(0.0)  # Inicializa otra variable escalar con valor 0.0
scalar_c.assign_add(2)  # Incrementa su valor en 2

valor_actualizado = scalar_c.read_value().numpy()
print("\nValor actualizado de 'scalar_c' (después de sumar 2):", valor_actualizado)