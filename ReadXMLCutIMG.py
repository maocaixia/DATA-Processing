#from __future__ import division
import os
from PIL import Image
import xml.dom.minidom
import numpy as np

ImgPath = 'D:/DATA/data_3_floor_Background_Model/imgs/'
AnnoPath = 'D:/DATA/data_3_floor_Background_Model/xmls/'
savepath = 'D:/DATA/HumanBody'

#if not os.path.exists(ProcessedPath):
#	os.makedirs(ProcessedPath)

fileslist = os.listdir(ImgPath)
for file_ in fileslist:
    file_path = ImgPath + file_
    imagelist = os.listdir(file_path)
    print('Load new file:', file_)
    count = 0 
    for image in imagelist:
        if count % 5 != 0:
            count += 1
            continue
        count += 1
        print('Load new image:', image)
        image_pre, ext = os.path.splitext(image)
        imgfile = file_path + '/' + image 
        xmlfile = AnnoPath + file_ + '/' + image_pre + '.xml'
    
        DomTree = xml.dom.minidom.parse(xmlfile)
        annotation = DomTree.documentElement
    
        filenamelist = annotation.getElementsByTagName('filename') 
        filename = filenamelist[0].childNodes[0].data
        objectlist = annotation.getElementsByTagName('object')
    
        i = 1
        for objects in objectlist:
            # print objects
            
            namelist = objects.getElementsByTagName('name')
            # print 'namelist:',namelist
            objectname = namelist[0].childNodes[0].data
    
            bndbox = objects.getElementsByTagName('bndbox')
            cropboxes = []
            for box in bndbox:
                x1_list = box.getElementsByTagName('xmin')
                x1 = int(float(x1_list[0].childNodes[0].data))
                y1_list = box.getElementsByTagName('ymin')
                y1 = int(float(y1_list[0].childNodes[0].data))
                x2_list = box.getElementsByTagName('xmax')
                x2 = int(float(x2_list[0].childNodes[0].data))
                y2_list = box.getElementsByTagName('ymax')
                y2 = int(float(y2_list[0].childNodes[0].data))
                w = x2 - x1
                h = y2 - y1
    
                img = Image.open(imgfile)
                width,height = img.size
    
                region = img.crop((x1,y1,x2,y2))
                region.save(savepath + '/' + image_pre + '_' + str(i) + '.jpg')
                i += 1

                
                
                
