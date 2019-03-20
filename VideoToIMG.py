import cv2
import time
import os,glob

video_path = '/data2/maocaixia/data/video_data/video_data_3_floor/'
save_path = '/data2/maocaixia/data/video_data/imgs/'
files_video = os.listdir(video_path)
names = []
for file_v in files_video:
    tmp1,tmp2 = os.path.splitext(file_v)
    names.append(tmp1)
for video_name in names:
    video_name_path = video_path + video_name + '.flv'
    cam = cv2.VideoCapture(video_name_path)
    fgbg = cv2.createBackgroundSubtractorMOG2()
    thr = 10000
    frame_num = 0
    while 1:
        ret, frame = cam.read()
        frame_num += 1
        pos_msec = cam.get(cv2.CAP_PROP_POS_MSEC)

        if not ret:
            print('cant open video or video done')
            break

        fgmask = fgbg.apply(frame)
        res = cv2.medianBlur(fgmask, 5)
        pic = cv2.resize(res, (100,100), interpolation=cv2.INTER_NEAREST)
        sp = pic.shape
        sum_ = 0

        for i in range(sp[0]):
            for j in range(sp[1]):
                sum_ += pic[i,j]

        if sum_ > thr:
            video_dir = save_path+str(video_name)
            if not os.path.exists(video_dir):
                os.mkdir(video_dir)
            img_dir = video_dir+'/'+str(video_name)+'_'+str(frame_num)+'_'+str(int(pos_msec))+'.jpg'
            cv2.imwrite(img_dir, frame)
