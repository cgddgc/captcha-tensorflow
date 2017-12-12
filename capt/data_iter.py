"""
数据生成器
"""

import numpy as np
import os,random
from cfg import IMAGE_HEIGHT, IMAGE_WIDTH, CHAR_SET_LEN, MAX_CAPTCHA
from gen_captcha import wrap_gen_captcha_text_and_image
from utils import convert2gray, text2vec
from train_set import train_data

def get_next_batch(batch_size=128):
    """
    # 生成一个训练batch
    :param batch_size:
    :return:
    """
    imgpath="D:/gitrepos/captcha-tensorflow/vcode1/"
    batch_x = np.zeros([batch_size, IMAGE_HEIGHT * IMAGE_WIDTH])
    batch_y = np.zeros([batch_size, MAX_CAPTCHA * CHAR_SET_LEN])
    td=train_data()
    for i in range(batch_size):
        #text, image = wrap_gen_captcha_text_and_image()
        text, image = td.get_text_img(imgpath)
        image = convert2gray(image)

        batch_x[i, :] = image.flatten() / 255  # (image.flatten()-128)/128  mean为0
        batch_y[i, :] = text2vec(text)

    return batch_x, batch_y

def get_test_batch(batch_size=500):
    """
    # 生成一个训练batch
    :param batch_size:
    :return:
    """
    imgpath="D:/gitrepos/captcha-tensorflow/test/"
    batch_x = np.zeros([batch_size, IMAGE_HEIGHT * IMAGE_WIDTH])
    batch_y = np.zeros([batch_size, MAX_CAPTCHA * CHAR_SET_LEN])
    td=train_data()
    for i in range(batch_size):
        #text, image = wrap_gen_captcha_text_and_image()
        text, image = td.get_text_img(imgpath)
        image = convert2gray(image)

        batch_x[i, :] = image.flatten() / 255  # (image.flatten()-128)/128  mean为0
        batch_y[i, :] = text2vec(text)

    return batch_x, batch_y
#print(get_next_batch())