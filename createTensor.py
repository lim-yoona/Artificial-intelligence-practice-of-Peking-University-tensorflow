import tensorflow as tf

tensor1=tf.constant("hello world",dtype=None)
print(tensor1)
print(tensor1.dtype)
print(tensor1.shape)

tensor2=tf.constant([[2,3],[4,5]])
print(tensor2)
print(tensor2.dtype)
print(tensor2.shape)