
import tensorflow as tf

tensor_1d = tf.constant([0, 1, 2, 3, 4, 5, 6, 7])

# Rebanadas del tensor 1d
slice_explicit = tf.slice(tensor_1d, begin = [1], size = [3])
slice_slicing_operator = tensor_1d[1:4]
slice_negative_index = tensor_1d[-3:]  # Últimos tres elementos

print("Tensor 1d:", tensor_1d)
print("\nRebanada explícita:", slice_explicit)
print("Rebanada con operador de índice:", slice_slicing_operator)
print("Últimos tres elementos:", slice_negative_index)

tensor_2d = tf.constant([
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19]
])

# Rebanada del tensor 2d 
# (todas menos la última fila, y columnas 1 a 3)
slice_2d = tensor_2d[:-1, 1:3]

print("\nTensor 2d (bidimensional):", tensor_2d)
print("\nRebanada bidimensional (sin última fila, columnas 1 a 3):\n", slice_2d)

# Tensor alfanumérico
tensor_alphabet = tf.constant(list("abcdefghijklmnopqrstuvwxyz"))
selected_letters = tf.gather(tensor_alphabet, indices = [1, 17, 4, 3, 0])
print("\nLetras seleccionadas del tensor alfabético:\n", selected_letters)