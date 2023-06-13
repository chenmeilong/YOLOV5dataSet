import os
import random
#此时训练数据集是0.8 测试数据集是0.1 验证数据集是 0.1
testval_percent = 0.2   #测试+验证数据集在所有数据集中占的比例    那么训练数据集就是1-testval_percent
testpercent = 0.5       #测试数据集在测试+验证数据集中占的比例
xmlfilepath = 'Annotations'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * testval_percent)
tr = int(tv * testpercent)
trainval = random.sample(list, tv)
test = random.sample(trainval, tr)

ftrainval = open('ImageSetstrainval.txt', 'w')
ftest = open('ImageSets/test.txt', 'w')
ftrain = open('ImageSets/train.txt', 'w')
fval = open('ImageSets/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in test:
            ftest.write(name)
        else:
            fval.write(name)
    else:
        ftrain.write(name)
ftrainval.close()
ftrain.close()
fval.close()
ftest.close()



