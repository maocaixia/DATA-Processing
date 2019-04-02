# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:02:07 2019

@author: maocaixia
"""
import os
import xml.dom.minidom

dirs = 'D:/DATA/CrossScreen/'

for ddir in os.listdir(dirs):
    path_ = dirs + ddir + '/UniformLabel/'
    save_path = 'D:/DATA/CrossScreen/'+ddir+'/gt.txt'
    t_w = open(save_path, 'w')
    for xml_name in os.listdir(path_):
        print(ddir,' --> ',xml_name)
        xml_dir = path_ + xml_name
        t1,t2 = os.path.splitext(xml_name)[0].split('_')
        t_w.write(t1+',')
        dom = xml.dom.minidom.parse(xml_dir)
        root = dom.documentElement
        filenamelist = root.getElementsByTagName('filename')
        objectlist = root.getElementsByTagName('object')
        objectIDlist = root.getElementsByTagName('objectID')
        object_num = len(objectIDlist)
        index = int(object_num / 2)
        t_w.write(str(objectIDlist[index].childNodes[0].data)+',')
        bndbox = objectlist[0].getElementsByTagName('bndbox')
        for box in bndbox:
            x1_list = box.getElementsByTagName('xmin')
            x1 = int(float(x1_list[0].childNodes[0].data))
            y1_list = box.getElementsByTagName('ymin')
            y1 = int(float(y1_list[0].childNodes[0].data))
            x2_list = box.getElementsByTagName('xmax')
            x2 = int(float(x2_list[0].childNodes[0].data))
            y2_list = box.getElementsByTagName('ymax')
            y2 = int(float(y2_list[0].childNodes[0].data))
            t_w.write(str(x1)+','+str(y1)+','+str(x2)+','+str(y2)+',')
        t_w.write('1,-1,-1,-1\n')
        
    t_w.close()
            
            
