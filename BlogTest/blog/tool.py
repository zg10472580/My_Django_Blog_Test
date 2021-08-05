# -*- coding: utf-8 -*-
# Time     :  2021/8/3 9:32
# Author   :  老飞机
# File     :  tool.py
# Software :  PyCharm
from django.shortcuts import render

def tool_index(request):
    return render(request, 'tool/index.html')