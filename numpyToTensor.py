import tensorflow as tf
import numpy as np

i=np.arange(0,5)
print(i)
j=tf.convert_to_tensor(i,dtype=None)
print(j)