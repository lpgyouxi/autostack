#!/usr/bin/env python
# coding:utf-8


class mysql(object):
    """
        提供对mysql数据操作的一些方法
    """
    def __init__(self, dbname, tablename):
        """
        :param dbname: 数据库名
        :param tablename:  表名
        :return:
        """
        pass

    def insert(self, data):
        """
        将数据插入到数据库
        :param data: 需要插入的数据
        :return: 已插入的数据条数
        """
        pass

    def update(self, data):
        """
        :param data: 更新数据以及条件
        :return:
        """
        pass

    def delete(self, condition):
        """
        :param condition: 删除的条件
        :return:
        """
        pass

    def select(self, condition):
        """
        :param condition: 查询条件
        :return:
        """
        pass

    def query(self, sql):
        """
        :param sql: 原始sql
        :return:
        """
        pass


class redis(object):
    def __init__(self):
        pass

    def get(self, condition):
        pass

    def set(self, data):
        pass

