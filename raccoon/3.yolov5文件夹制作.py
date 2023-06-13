import os
import numpy as np
import shutil
#目前将验证数据集和测试数据集合在了一起
dir_data=os.getcwd()
os.chdir(dir_data)  #切换工作目录
# print(os.listdir())

#删除文件夹内的所有文件
def del_files(dir_path):
    if os.path.isfile(dir_path):
        try:
            os.remove(dir_path) # 这个可以删除单个文件，不能删除文件夹
        except BaseException as e:
            print(e)
    elif os.path.isdir(dir_path):
        file_lis = os.listdir(dir_path)
        for file_name in file_lis:
            tf = os.path.join(dir_path, file_name)
            del_files(tf)
    # print('ok')
del_files('yolo5_data')



FILE_image_PATH='yolo5_data/images'
if not os.path.exists(FILE_image_PATH):
    os.makedirs(FILE_image_PATH)

if not os.path.exists(FILE_image_PATH+'/train'):
    os.makedirs(FILE_image_PATH+'/train')

if not os.path.exists(FILE_image_PATH+'/test'):
    os.makedirs(FILE_image_PATH+'/test')

FILE_label_PATH='yolo5_data/labels'
if not os.path.exists(FILE_label_PATH):
    os.makedirs(FILE_label_PATH)
if not os.path.exists(FILE_label_PATH+'/train'):
    os.makedirs(FILE_label_PATH+'/train')
if not os.path.exists(FILE_label_PATH+'/test'):
    os.makedirs(FILE_label_PATH+'/test')


#训练
f = open("train.txt",'r',encoding="utf-8")
for index,line in enumerate(f.readlines()):                    #引入序号，判断更改    将txt文件写出来
    img_name = line.strip().split('/')[-1]
    #转存图片和文件
    source_path='labels/'+img_name[:-4]+'.txt'
    targer_path=FILE_label_PATH+'/train'
    shutil.copy(source_path,targer_path)

    source_path='JPEGImages/'+img_name
    targer_path=FILE_image_PATH+'/train'
    shutil.copy(source_path,targer_path)


#测试1
f = open("test.txt",'r',encoding="utf-8")
for index,line in enumerate(f.readlines()):                    #引入序号，判断更改    将txt文件写出来
    img_name = line.strip().split('/')[-1]
    #转存图片和文件
    source_path='labels/'+img_name[:-4]+'.txt'
    targer_path=FILE_label_PATH+'/test'
    shutil.copy(source_path,targer_path)

    source_path='JPEGImages/'+img_name
    targer_path=FILE_image_PATH+'/test'
    shutil.copy(source_path,targer_path)

#测试2
f = open("val.txt",'r',encoding="utf-8")
for index,line in enumerate(f.readlines()):                    #引入序号，判断更改    将txt文件写出来
    img_name = line.strip().split('/')[-1]
    #转存图片和文件
    source_path='labels/'+img_name[:-4]+'.txt'
    targer_path=FILE_label_PATH+'/test'
    shutil.copy(source_path,targer_path)

    source_path='JPEGImages/'+img_name
    targer_path=FILE_image_PATH+'/test'
    shutil.copy(source_path,targer_path)
