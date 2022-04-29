# /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/28 17:46
# @Author  : Shaohd
# @FileName: main.py


import tornado.web
import os
from utils import photo
from loguru import logger


class IndexHandler(tornado.web.RequestHandler):
    """
     Home page for user,photo feeds
    """
    logger.info(f"IndexHandler")

    def get(self, *args, **kwargs):
        self.render('index.html')  # 打开index.html网页


class ExploreHandler(tornado.web.RequestHandler):
    """
    Explore page,photo of other users
    """

    def get(self, *args, **kwargs):
        logger.info(f"ExploreHandler")
        os.chdir('static')  # 用于改变当前工作目录到指定的路径
        image_urls = photo.get_images("uploads/thumbs")
        os.chdir("..")
        self.render('explore.html', image_urls=image_urls)


class PostHandler(tornado.web.RequestHandler):
    """
    Single photo page and maybe
    """

    def get(self, post_id):
        logger.info(f"PostHandler:{post_id}")
        self.render('post.html', post_id=post_id)


class UploadHandler(tornado.web.RequestHandler):
    logger.info(f"UploadHandler")

    def get(self, *args, **kwargs):
        self.render('upload.html')

    def post(self, *args, **kwargs):
        file_imgs = self.request.files.get('newImg', None)  # 获取上传文件数据，返回文件列表

        for file_img in file_imgs:
            # filename:文件的实际名字，body:文件的数据实体；content_type:文件的类型
            save_to = f"static/uploads/{file_img['filename']}"
            with open(save_to, 'wb') as f:
                f.write(file_img['body'])
            photo.make_thumb(save_to)

        self.redirect('/explore')