# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import shutil
import os 

new_path_root = 'D:/DATA/SingleScreenTracking/data/'
path_ = 'D:/DATA/Three_Floor_Labeled/'
xmls = 'xmls/'
imgs = 'imgs/'

filelists = os.listdir(new_path_root)

for f in filelists:
    new_dir = new_path_root + f
    new_dir_1 = new_dir + '/' + 'Annotations/'
    new_dir_2 = new_dir + '/' + 'PNGImages/'
    print(f)
    #if not os.path.exists(new_dir_1):
    #    os.makedirs(new_dir_1)
    #if not os.path.exists(new_dir_2):
    #    os.makedirs(new_dir_2)
    #path_1 = path_ + xmls + f
    #path_2 = path_ + imgs + f
    #shutil.copytree(path_1, new_dir_1)
    #shutil.copytree(path_2, new_dir_2)
    img_files = os.listdir(new_dir_2)
    for img_f in img_files:
        img_pre, img_next = os.path.splitext(img_f)
        img_name = img_pre.split('_')
        img_frame = img_name[1]
        old_path = new_dir_2 + img_f
        new_path = new_dir_2 + img_frame + '.jpg'
        os.rename(old_path, new_path)
        
    xml_files = os.listdir(new_dir_1)
    for xml_f in xml_files:
        xml_pre, xml_next = os.path.splitext(xml_f)
        xml_name = xml_pre.split('_')
        xml_frame = xml_name[1]
        old_path = new_dir_1 + xml_f
        new_path = new_dir_1 + xml_frame + '.xml'
        os.rename(old_path, new_path)
    
    
