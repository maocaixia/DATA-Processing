# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 14:27:22 2019

@author: maocaixia
"""
import os
import xml.etree.ElementTree as ET
import xml.dom.minidom
from xml.dom import Node

dirs_ = 'D:/DATA/SingleScreenTracking/data/'
for dir_ in os.listdir(dirs_):
    xml_dir = dirs_ + dir_ + '/'
    label_ = 0
    dict_map = {}
    
    for xml_ in os.listdir(xml_dir+'SingleScreenLabel/'):
        xml_name = xml_dir + 'SingleScreenLabel/' +xml_
        xml_1, xml_2 = os.path.splitext(xml_)[0].split('_')
        print(dir_,xml_,xml_1,xml_2)
        
        dom = xml.dom.minidom.parse(xml_name)
        root = dom.documentElement
        filenamelist = root.getElementsByTagName('filename')
        objectlist = root.getElementsByTagName('object')
        
        objectidlist = root.getElementsByTagName('objectID')
        object_num = len(objectidlist)
        if object_num % 2:
            i = object_num/2 + 1
        else:
            i = object_num/2
        
        while i < object_num:
            index = int(i)
            i += 2
            ori_d_1 = objectidlist[index].childNodes[0].data #
            ori_d_2 = objectidlist[index+1].childNodes[0].data #
            dict_index_1 = xml_1 + '_' + ori_d_1
            dict_index_2 = xml_2 + '_' + ori_d_2
            
            if str(dict_index_1) in dict_map or str(dict_index_2) in dict_map:
                if dict_index_1 in dict_map:
                    new_label = dict_map[str(dict_index_1)]
                    dict_map[str(dict_index_2)] = new_label
                else:
                    new_label = dict_map[str(dict_index_2)]
                    dict_map[str(dict_index_1)] = new_label
            else:
                new_label = str(label_)
                label_ = label_ + 1
                dict_map[str(dict_index_1)] = new_label
                dict_map[str(dict_index_2)] = new_label
                
            objectidlist[index].childNodes[0].data = new_label
            objectidlist[index+1].childNodes[0].data = new_label
            
        save_path = xml_dir + 'UniformLabel/'
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        save_name = save_path + xml_
        with open(save_name, 'w') as fh:
                dom.writexml(fh)


#with open(xml_dir + 'res.txt', 'w') as ow:
#    for key in dict_map:
#        ow.write(key + ' ' + dict_map[key] + '\n')
    
#    maplist = root.getElementsByTagName('map')
#    #map_objectlist = maplist.getElementsByTagName('filename')
#    print(maplist[0].childNodes[0].data)
#    mapl = maplist[0]
#    print(mapl.getAttribute("filename"))
    #print('objectid: ', objectidlist[3].childNodes[0].data)
    #print('filename: ', filenamelist[2].childNodes[0].data)
    #filenamelist[2].childNodes[0].data = '6666.jpg'
    
    
#    listInfos = []
#    for child in root.childNodes:
#        if child.nodeType == Node.ELEMENT_NODE:
#            dictAttr = {}
#            for key in child.attributes.keys():
#                attr = child.attributes[key]
#                dictAttr[attr.name] = attr.value
#            listInfos.append({child.nodeName: dictAttr})
#    for index, each in enumerate(listInfos):
#        print('----', index + 1, '----', each)
    
    
#    for objectid in objectidlist:
#        print('objectid: ', objectid.childNodes[0].data)
#        
#    for i in range(4):
#        objectidlist[i].childNodes[0].data = i
#    
#    print('After Changing: ')
#    for objectid in objectidlist:
#        print('objectid: ', objectid.childNodes[0].data)
        
#    bndbox = objectlist[1].getElementsByTagName('bndbox')
#    for box in bndbox:
#        x1_list = box.getElementsByTagName('xmin')
#        x1 = int(float(x1_list[0].childNodes[0].data))
#        y1_list = box.getElementsByTagName('ymin')
#        y1 = int(float(y1_list[0].childNodes[0].data))
#        x2_list = box.getElementsByTagName('xmax')
#        x2 = int(float(x2_list[0].childNodes[0].data))
#        y2_list = box.getElementsByTagName('ymax')
#        y2 = int(float(y2_list[0].childNodes[0].data))
#        #print(x1,y1,x2,y2)
#    
#    with open(xml_name, 'w') as fh:
#        dom.writexml(fh)
    
    
    
    
    
    
    
