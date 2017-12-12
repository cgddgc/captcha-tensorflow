"""
网络结构
"""
import tensorflow as tf
import numpy as np
from cfg import IMAGE_HEIGHT, IMAGE_WIDTH, CHAR_SET_LEN, MAX_CAPTCHA

X = tf.placeholder(tf.float32, [None, IMAGE_HEIGHT * IMAGE_WIDTH])
Y = tf.placeholder(tf.float32, [None, MAX_CAPTCHA * CHAR_SET_LEN])
keep_prob = tf.placeholder(tf.float32)  # dropout


def crack_captcha_cnn(w_alpha=0.01, b_alpha=0.1):
    """
    定义CNN
    cnn在图像大小是2的倍数时性能最高, 如果你用的图像大小不是2的倍数，可以在图像边缘补无用像素。
    np.pad(image,((2,3),(2,2)), 'constant', constant_values=(255,))  # 在图像上补2行，下补3行，左补2行，右补2行
    """

    x = tf.reshape(X, shape=[-1, IMAGE_HEIGHT, IMAGE_WIDTH, 1])

    #w_c1_alpha = np.sqrt(2.0/(IMAGE_HEIGHT*IMAGE_WIDTH)) #
    #w_c2_alpha = np.sqrt(2.0/(3*3*32))
    #w_c3_alpha = np.sqrt(2.0/(3*3*64))
    #w_d1_alpha = np.sqrt(2.0/(8*32*64))
    #out_alpha = np.sqrt(2.0/1024)

    # 3 conv layer
    w_c1 = tf.Variable(w_alpha * tf.random_normal([3, 3, 1, 32]))
    b_c1 = tf.Variable(b_alpha * tf.random_normal([32]))
    conv11 = tf.nn.relu(tf.nn.bias_add(tf.nn.conv2d(x, w_c1, strides=[1, 1, 1, 1], padding='SAME'), b_c1))
    #用3x3x1卷积核对图像进行卷积
    conv12 = tf.nn.max_pool(conv11, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
    #池化操作，图像宽高变为一半（向上取整）
    conv13 = tf.nn.dropout(conv12, keep_prob)
    #防止过拟合
    


    w_c2 = tf.Variable(w_alpha * tf.random_normal([3, 3, 32, 64]))
    b_c2 = tf.Variable(b_alpha * tf.random_normal([64]))
    conv21 = tf.nn.relu(tf.nn.bias_add(tf.nn.conv2d(conv13, w_c2, strides=[1, 1, 1, 1], padding='SAME'), b_c2))
    #用3x3x1卷积核对图像进行卷积
    conv22 = tf.nn.max_pool(conv21, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
    #池化操作，图像宽高变为一半（向上取整）
    conv23 = tf.nn.dropout(conv22, keep_prob)
    #防止过拟合
    


    w_c3 = tf.Variable(w_alpha * tf.random_normal([3, 3, 64, 64]))
    b_c3 = tf.Variable(b_alpha * tf.random_normal([64]))
    conv31 = tf.nn.relu(tf.nn.bias_add(tf.nn.conv2d(conv23, w_c3, strides=[1, 1, 1, 1], padding='SAME'), b_c3))
    #用3x3x1卷积核对图像进行卷积
    conv32 = tf.nn.max_pool(conv31, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
    #池化操作，图像宽高变为一半（向上取整）
    conv33 = tf.nn.dropout(conv32, keep_prob)
    #防止过拟合

    # 最后一层全连接
    w_d = tf.Variable(w_alpha * tf.random_normal([3*6*64, 1024]))
    b_d = tf.Variable(b_alpha * tf.random_normal([1024]))
    dense = tf.reshape(conv33, [-1, w_d.get_shape().as_list()[0]])
    dense = tf.nn.relu(tf.add(tf.matmul(dense, w_d), b_d))
    dense = tf.nn.dropout(dense, keep_prob)

    w_out = tf.Variable(w_alpha * tf.random_normal([1024, MAX_CAPTCHA * CHAR_SET_LEN]))
    b_out = tf.Variable(b_alpha * tf.random_normal([MAX_CAPTCHA * CHAR_SET_LEN]))
    out = tf.add(tf.matmul(dense, w_out), b_out)  # 36*4
    #out = tf.reshape(out, (CHAR_SET_LEN, MAX_CAPTCHA))  # 重新变成4,36的形状
    #out = tf.nn.softmax(out)
    #print(out)
    return out


