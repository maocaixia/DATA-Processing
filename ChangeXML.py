# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:53:10 2019

@author: maocaixia
"""

#coding:utf-8
from PIL import Image
import os.path
import glob
import xml.etree.ElementTree as ET
import xml.dom.minidom

filedir = 'D:/DATA/SingleScreenTracking/data/'
#imgsdir = "E:\\object-detection-Game-2018-5-31\\imgs"
#outdir = "E:\\object-detection-Game-2018-5-31\\imgs"
for file_ in os.listdir(filedir):
    print(file_)
    xmldir = filedir + file_ + '/Annotations/'
    for xmlfile in os.listdir(xmldir):
        xmlname = os.path.splitext(xmlfile)[0]
        dom = xml.dom.minidom.parse(os.path.join(xmldir, xmlfile))
        root = dom.documentElement
        # 获取标签对filename之间的值并赋予新值i
        root.getElementsByTagName('filename')[0].firstChild.data = xmlname + '.jpg'
        # 将修改后的xml文件保存
        # xml文件修改前后的路径
        old_xmldir = os.path.join(xmldir, xmlfile)
        #new_xmldir = os.path.join(xmldir, str(i)+'.xml')
        # 打开并写入
        with open(old_xmldir, 'w') as fh:
            dom.writexml(fh)
        #os.rename(old_xmldir, new_xmldir)
        #for pngfile in os.listdir(imgsdir):
        #pngname = os.path.splitext(pngfile)[0]
        #if pngname == xmlname:
        # 修改图片文件名
        # 图片文件名修改前后的路径
        #olddir = os.path.join(os.path.abspath(imgsdir), pngname + ".png")
        #newdir = os.path.join(os.path.abspath(imgsdir), str(i)+".png")
        #os.rename(olddir, newdir)
        #print(xmlfile, '----->', str(i) + '.png')
        # 修改filename结点属性
        # 读取xml文件


