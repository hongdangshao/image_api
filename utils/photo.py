# /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/28 17:47
# @Author  : Shaohd
# @FileName: photo.py


import glob
import os
from PIL import Image


def get_images(path):
    # glob模块的主要方法就是glob,该方法返回所有匹配的文件路径列表（list）
    image_urls = glob.glob(path + '/*.jpg')
    return image_urls


# 生成缩略图
def make_thumb(path):
    h = 200
    im = Image.open(path)
    im.thumbnail((h, h))  # thumbnail函数接受一个元组作为参数，分别对应着缩略图的宽高，在缩略时，函数会保持图片的宽高比例。
    name = os.path.basename(path)
    filename, ext = os.path.splitext(name)
    # save to filename_200x200.jpg
    im.save(f"static/uploads/thumbs/{filename}_{h}x{h}{ext}")