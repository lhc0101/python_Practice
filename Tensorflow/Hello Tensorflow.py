import tensorflow as tf
hello = tf.constant("Hello TensorFlow")
#创建一个会话，上下文环境
sess = tf.Session()
#执行常量操作 hello 并打印到标准输出
print(sess.run(hello))