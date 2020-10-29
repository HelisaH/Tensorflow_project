# TODO: Add imports.
import tensorflow as tf

tf.reset_default_graph()

test_constant = tf.constant(10.0, dtype=tf.float32)
add_one_operation = test_constant + 1