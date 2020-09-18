#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :__init__.py
# @Time      :2020/9/18 2:43 下午
# @Author    :Kangke

import os
import sys

# 获得本文件父文件的绝对路径
curPath = os.path.abspath(os.path.dirname(__file__))
# 根文件的绝对路径
rootPath = os.path.split(curPath)[0]
# 根文件的父文件加入系统路径
sys.path.append(os.path.split(rootPath)[0])