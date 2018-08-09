# k-近邻算法 p19
#距离应用欧氏距离,p=2
import operator
from numpy import *
import matplotlib.pyplot as plt
from os import listdir

def classfiy0(inX,dataSet,labels,k):
    #intX--要预测的输入向量
    #dataSet--训练样本集
    #labels--标签向量(每个样本对应的类别标签)
    dataSetSize=dataSet.shape[0] #样本矩阵的行数，也就是样本点数
    diffMat=tile(inX,(dataSetSize,1))-dataSet #计算intX向量和每个样本点的各个特征之差 
    sqDiffMat=diffMat**2 # 矩阵每个元素平方
    sqDistances=sqDiffMat.sum(axis=1)#计算每行元素的和，返回的一个一维数组(或向量)
    distances=sqDistances**0.5#每个元素开根号
    sortedDistIndicies=distances.argsort()#返回从小到大怕排序后的索引数组
    classCount={} #统计每个类别的样本个数
    for i in range(k):#取k个最近的样本点
        voteIlabel=labels[sortedDistIndicies[i]] #第i个样本的类别
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
    sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    #按classCount字典的每一项的第二个值(即按类别的样本数)进行从大到小排序

    return sortedClassCount[0][0] #返回样本数最多的类别

def createDataSet():
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1] ])
    labels=['A','A','B','B']
    return group,labels

def myReplace(str):
    str=str.replace('largeDoses','3')
    str=str.replace('smallDoses','2')
    str=str.replace('didntLike','1')
    return str
    

def file2matrix(filename):
    fr=open(filename)
    arrayOLines=fr.readlines() #返回list,文件每一行是一项
    numberOfLines=len(arrayOLines) #得到文件行数
    returnMat=zeros((numberOfLines,3))#创建m*n零矩阵
    classLabelVector=[]#类标记数组
    index=0
    for line in arrayOLines:
        line=line.strip()
        line=myReplace(line)#把类别用数字表示
        listFromLine=line.split('\t')#每行转化成list
        returnMat[index,:]=listFromLine[0:3]#前三项放入矩阵中
        classLabelVector.append(int(listFromLine[-1]))#最后一项转化为int型
        index+=1
    return returnMat,classLabelVector

def plotscatter():
    datingDataMat,datingLabels=file2matrix(r'ML\datingTestSet.txt')
    fig=plt.figure()
    ax1=fig.add_subplot(111)
    ax1.scatter(datingDataMat[:,1],datingDataMat[:,2],10*array(datingLabels),10*array(datingLabels))
    plt.show()
    
def autoNorm(dataSet):#数据归一化 newValue=(oldValue - min)/(max-min) 把特征值转化为0到1区间内的值
    minVals=dataSet.min(0) #返回一个数组，数组中每个数都是它所在列的最小值
    maxVals=dataSet.max(0) #返回一个数组，数组中每个数都是它所在列的最大值
    ranges=maxVals-minVals #作差后的数组
    normDataSet=zeros(shape(dataSet)) #零矩阵
    m=dataSet.shape[0] #行数
    normDataSet=dataSet-tile(minVals,(m,1)) # (oldValue - min)
    normDataSet=normDataSet/tile(ranges,(m,1)) #(oldValue - min)/(max-min)
    return normDataSet,ranges,minVals

def datingClassTest():#测试算法的正确性,求其分类错误率
    hoRatio=0.1 #去10%的样本作为测试数据集
    datingDataMat,datingLabels=file2matrix(r'datingTestSet.txt')
    normMat,ranges,minVals=autoNorm(datingDataMat)
    m=normMat.shape[0]
    numTest=int(hoRatio*m)#测试样本数
    errorCount=0.0 #错误分类的样本点
    for i in range(numTest):
        classifierResult=classfiy0(normMat[i,:],normMat[numTest:m,:],datingLabels[numTest:m],3)
        print('the classifier came back with:%d,the real answer is:%d'%(classifierResult,datingLabels[i]))
        if (classifierResult!=datingLabels[i]):
            errorCount+=1.0
    print('the total error rate is:%f'%(errorCount/float(numTest)))

def classifyPerson():#分类预测
    resultList=['not at all','in small doses','in large doses']
    percentTats=float(input('percentage of time spent playing video games? '))
    ffMiles=float(input('frequent flier miles earned per year? '))
    iceCream=float(input('liters of ice cream consumed per year? '))
    datingDataMat,datingLabels=file2matrix(r'datingTestSet.txt')
    normMat,ranges,minVals=autoNorm(datingDataMat)
    inArr=array([ffMiles,percentTats,iceCream])
    classifierResult=classfiy0((inArr-minVals)/ranges,normMat,datingLabels,3)
    print('You will probably like this person: ',resultList[classifierResult-1])


#以下是示例2.3 手写识别系统 所需函数

def img2vector(filename): #把数字矩阵(32*32) 转化成一个向量 (1*1024)
    returnVect=zeros((1,1024)) #初始化零向量(1*1024)
    fr=open(filename)
    for i in range(32): #每行
        lineStr=fr.readline() #读取一行
        for j in range(32): #每列
            returnVect[0,32*i+j]=int(lineStr[j]) #加入到向量中
    return returnVect

def handwritigClassTest():
    hwLabels=[]#保存分类数字
    trainingFileList=listdir(r'trainingDigits') #返回该目录下的文件名列表
    m=len(trainingFileList) #训练样本点数
    trainingMat=zeros((m,1024)) #初始化 训练数据矩阵(m*1024)
    for i in range(m):
        fileNameStr=trainingFileList[i]#第i个文件全名
        fileStr=fileNameStr.split('.')[0] #文件i个文件名
        classNumStr=int(fileStr.split('_')[0]) #分类数字
        hwLabels.append(classNumStr) #保存
        trainingMat[i,:]=img2vector(r'trainingDigits/%s'% fileNameStr)#放入训练数据矩阵中
    testFileList=listdir(r'testDigits')
    errorCount=0.0
    mTest=len(testFileList) #测试数据个数
    for i in range(mTest):
        fileNameStr=testFileList[i]
        fileStr=fileNameStr.split('.')[0]
        classNumStr=int(fileStr.split('_')[0]) #分类数字
        vectorUnderTest=img2vector(r'testDigits/%s'% fileNameStr) #测试向量
        classifierResult=classfiy0(vectorUnderTest,trainingMat,hwLabels,3)#调用分类算法
        print('the classifier came back with:%d,the real answer is:%d'%(classifierResult,classNumStr))
        if (classifierResult!=classNumStr):
            errorCount+=1.0
    print('the total number of errors is:%d'%errorCount)
    print('the total error rate is:%f'%(errorCount/float(mTest)))

handwritigClassTest()


    
    
    
