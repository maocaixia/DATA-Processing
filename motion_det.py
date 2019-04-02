# -*-coding:utf-8 -*-
import cv2
import time
import os
import glob
#img save path
save_path = '/data2/maocaixia/data/video_data/imgs/'
video_path = '/data2/maocaixia/data/video_data/video_data_3_floor/'
files_video = os.listdir(video_path)
names = []
for file_v in files_video:
    tmp1,tmp2 = os.path.splitext(file_v)
    names.append(tmp1)
#camera = cv2.VideoCapture(0)
#if (camera.isOpened()):
#    print('Open')
#else:
#    print('Open Fails')
for video_name in names:
    video_name_path = video_path + video_name + '.flv'
    camera = cv2.VideoCapture(video_name_path)
#pos_msec = camera.get(cv2.CAP_PROP_POS_MSEC)
#print(pos_msec)
#size = (int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)),
#        int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)))
#print('size:'+repr(size))

#fps = 20
    pre_frame = None
    num = 0
    frame_num = 0
    while(1):
        #start = time.time()
        ret, frame = camera.read()
        frame_num += 1
        #gray_lwpCV = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        pos_msec = camera.get(cv2.CAP_PROP_POS_MSEC)
        #print(pos_msec)    

        if not ret:
            print('cant open video')
            break
        gray_lwpCV = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #end = time.time()
        #cv2.imshow("capture", frame)
        #seconds = end - start
        #if seconds < 1.0 / fps:
        #    time.sleep(1.0 / fps - seconds)
        gray_lwpCV = cv2.resize(gray_lwpCV, (500, 500))
        gray_lwpCV = cv2.GaussianBlur(gray_lwpCV, (21, 21), 0)

        if pre_frame is None:
            pre_frame = gray_lwpCV
        else:
            img_delta = cv2.absdiff(pre_frame, gray_lwpCV)
            thresh = cv2.threshold(img_delta, 25, 255, cv2.THRESH_BINARY)[1]
            thresh = cv2.dilate(thresh, None, iterations=2)
            image, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for c in contours:
                if cv2.contourArea(c) < 1000:
                    continue
                else:
                    #print(cv2.contourArea(c))
                    video_dir = save_path+str(video_name)
                    if not os.path.exists(video_dir):
                        os.mkdir(video_dir)
                    #num += 1
                    #print 'Saved images: %d\r' % (num),
                    #cv2.imwrite(save_path + str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))) + '.jpg', frame)
                    cv2.imwrite(video_dir+'/'+str(video_name)+'_'+str(frame_num)+'_'+str(int(pos_msec))+'.jpg', frame)
                    break
            pre_frame = gray_lwpCV

         #if cv2.waitKey(1) & 0xFF == ord('q'):
         #    break

    camera.release()
    #cv2.destroyAllWindows()
