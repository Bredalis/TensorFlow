
import tensorflow as tf

tensor_1d = tf.constant([1, 2, 3, 12, 5, 14, 22, 28])

print("Primero:", tensor_1d[0])
print("Segundo:", tensor_1d[1])
print("Último:", tensor_1d[-1])

# Manipulación del tensor 1d
print("\nTodos:", tensor_1d[:].numpy())
print("Antes de la posición 4:", tensor_1d[:4].numpy())
print("De la posición 4 al final:", tensor_1d[4:].numpy())
print("De 2 antes de 7:", tensor_1d[2:7].numpy())
print("Todos los otros artículos:", tensor_1d[::2].numpy())
print("Reversa:", tensor_1d[::-1].numpy())

tensor_2d = tf.constant([[1, 2], [3, 4]])

# Manipulación del tensor 2d
print(tensor_2d[1, 1])
print(f"\nSegunda fila: {tensor_2d[1, :].numpy()}")
print(f"Segunda columna: {tensor_2d[:, 1].numpy()}")
print(f"Última fila: {tensor_2d[-1, :].numpy()}")
print(f"Primer artículo de la última columna: {tensor_2d[-1, 0].numpy()}")
print(f"Saltando la primera fila: {tensor_2d[1:, :].numpy()}")