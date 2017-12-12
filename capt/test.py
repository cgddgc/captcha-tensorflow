#coding=utf-8
import tensorflow as tf

tensor = tf.zeros(shape=(2,2,3))

session = tf.InteractiveSession()
a = tf.Variable(tensor)
session.run(tf.initialize_all_variables())
print(session.run(a))