**本文设计的代码与素材均在[这里](https://github.com/chenmeilong/YOLOV5dataSet)，如果对您有帮助，欢迎start**
## 1.打标签
执行labelImg.exe，制作xml数据集
![e401f52d-2597-452c-b655-784464a6d7c9.png](http://img.cmlt.fun/article/e401f52d-2597-452c-b655-784464a6d7c9.png)

## 2.构建VOC2007目录
将标注好的xml文件放在Annotations目标中
将图片放在JPEGImages中
![451064a5-6f2e-4045-8509-185662c4693d.png](http://img.cmlt.fun/article/451064a5-6f2e-4045-8509-185662c4693d.png)

## 3.用python依次执行1,2,3，后面会提供1,2,3程序
注意：执行1.数据集划分.py之前需要修改数据集划分的比例（可以不修改）
![fcbef480-c838-47f8-a38f-b60b6a5d69a7.png](http://img.cmlt.fun/article/fcbef480-c838-47f8-a38f-b60b6a5d69a7.png)
注意：执行2.voc_label.py之前需要修改类别（必须修改）
![107a9352-b264-4057-b2e9-e45007d6bf3f.png](http://img.cmlt.fun/article/107a9352-b264-4057-b2e9-e45007d6bf3f.png)
依次执行1,2,3py文件，会生成一堆其他文件和这个yolo5_data
![07a6e332-e9ca-42cd-bf01-be80f4eafa58.png](http://img.cmlt.fun/article/07a6e332-e9ca-42cd-bf01-be80f4eafa58.png)
将生成的uolo5_data拷贝到yolo项目

## 4.在YOLO5项目的data目录中新建自己的yaml文件
写入下面内容nc为分类数量，name是标签名字
![6546de5d-1be3-41a8-9cec-d59f93b7b5e7.png](http://img.cmlt.fun/article/6546de5d-1be3-41a8-9cec-d59f93b7b5e7.png)

## 5.修改train.py文件
1处需要打开到对应的文件models/yolo5s.yaml文件，修改为分类数量
![7d1274be-b5f7-4641-b5de-59d4dc13fe4e.png](http://img.cmlt.fun/article/7d1274be-b5f7-4641-b5de-59d4dc13fe4e.png)
2处需要改为前面新建的yaml的名字
![26cb34f7-c1d5-4093-802c-d533aca09620.png](http://img.cmlt.fun/article/26cb34f7-c1d5-4093-802c-d533aca09620.png)
## 6.开始训练执行train.py
若是第一次配置 
1%执行train.py文件就可以开始训练自己的数据集
99%的可能出现错误，比如：显存不足，模型权重版本不正确，电脑环境没配置好。要根据报错信息具体分析。
***
**如果你觉得本文对你有所帮助，别忘记给我点个start，有任何疑问和想法，欢迎在评论区与我交流。**
