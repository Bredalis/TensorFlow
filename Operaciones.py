
import tensorflow as tf

tensor_1d = tf.constant([1, 2, 3])

print(f"Tensor 1d: {tensor_1d}")
print(f"Valor más alto: {tf.reduce_max(tensor_1d)}")
print(f"Index del valor más alto: {tf.argmax(tensor_1d)}")