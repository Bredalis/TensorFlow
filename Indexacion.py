
import tensorflow as tf

# Indexacion

a = tf.constant([1, 2, 3, 12, 5, 14, 22, 28])

print("Primero:", a[0])
print("Segundo:", a[1])
print("Ultimo:", a[-1])

print("\nTodos:", a[:].numpy())
print("Antes de la posicion 4:", a[:4].numpy())
print("De la posicion 4 al final:", a[4:].numpy())
print("De 2 antes de 7:", a[2:7].numpy())
print("Todos los otros articulos:", a[::2].numpy())
print("Reversa:", a[::-1].numpy())

# Obtener filas y columnas de los tensores (matrices)

b = tf.constant([[1, 2], [3, 4]])

print("\n", b[1, 1])

print(f"\nSegunda fila: {b[1, :].numpy()}")
print(f"Segunda columna: {b[:, 1].numpy()}")
print(f"Ultima fila: {b[-1, :].numpy()}")
print(f"Primer articulo de la ultima columna: {b[-1, 0].numpy()}")
print(f"Saltando la primera fila: {b[1:, :].numpy()}")