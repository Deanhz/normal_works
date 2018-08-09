#决策树

from math import log
import operator


def calcShannonEnt(dataSet):#计算数据集的香农熵
    numEntries=len(dataSet)
    labelCounts={} #统计各类的次数
    for featVec in dataSet:
        currentLabel=featVec[-1] #类
        labelCounts[currentLabel]=labelCounts.get(currentLabel,0)+1
    shannonEnt=0.0
    for key in labelCounts:
        prob=float(labelCounts[key])/numEntries
        shannonEnt-=prob*log(prob,2)
    return shannonEnt

def createDataSet():
    dataSet=[[1,1,'yes'],
             [1,1,'yes'],
             [1,0,'no'],
             [0,1,'no'],
             [0,1,'no']
             ]
    
    labels=['no surfacing','flippers']
    return dataSet,labels

def splitDataSet(dataSet,axis,value):#划分(抽取)数据集,三个参数:数据集，特征下标，特定特征值
    retDataSet=[]
    for featVec in dataSet:
        if featVec[axis]==value:
            reducedFeatVec=featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet


def chooseBestFeatureToSplit(dataSet):#根据信息增益,求最优的划分特征
    numFeatures=len(dataSet[0])-1 #特征数
    baseEntropy=calcShannonEnt(dataSet) #计算原始熵
    bestInfoGain=0.0
    bestFeature=-1 #最优特征下标
    for i in range(numFeatures):
        featList=[Vec[i] for Vec in dataSet] #第i个特征的list
        uniqueVals=set(featList) #无重复的第i个特征的集合
        newEntropy=0.0 #划分后的熵，也就是条件熵
        for value in uniqueVals:#计算条件熵
            subDataSet=splitDataSet(dataSet,i,value)
            prob=len(subDataSet)/float(len(dataSet))
            newEntropy+=prob*calcShannonEnt(subDataSet)
        infoGain=baseEntropy-newEntropy
        if(infoGain >bestInfoGain):
            bestInfoGain=infoGain
            bestFeature=i
    return bestFeature

def majorityCnt(classList):#求最多的类
    classCount={}
    for vote in classList:
        classCount[vote]=classCount.get(vote,0)+1
    sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)#返回字典的元组列表
    return sortedClassCount[0][0] #返回最多的类

def createTree(dataSet,labels):#labels是当前数据集dataSet的特征标签list
    classList=[vec[-1] for vec in dataSet] #类列表
    if classList.count(classList[0])==len(classList): #如果结点的类完全相同则停止划分，递归的出口
        return classList[0]
    if len(dataSet[0])==1: #如果遍历完所有的特征，则返回剩余结点中类出现最多的类别，递归的出口
        return majorityCnt(classList)
    bestFeat=chooseBestFeatureToSplit(dataSet)#最优特征的下标
    bestFeatLabel=labels[bestFeat] #最优特征
    myTree={bestFeatLabel:{}} #用嵌套的字典来表示树
    del(labels[bestFeat]) #删除该特征
    featValues=[vec[bestFeat] for vec in dataSet] #特征值list
    uniqueVals=set(featValues)#无重复的特征值set
    for value in uniqueVals:#遍历特征值
        subLabels=labels[:] #创建副本
        myTree[bestFeatLabel][value]=createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
    return myTree


def classify(inputTree,featLabels,testVec):#决策树,特征标签list,测试样本
    firstStr=list(inputTree.keys())[0] #第一个划分标签
    secondDict=inputTree[firstStr]
    featIndex=featLabels.index(firstStr)#第一个划分标签的下标
    for key in secondDict.keys():
        if testVec[featIndex]==key:#找到正确的分支
            if type(secondDict[key]).__name__=='dict':#当前值是字典类型，说明是内部结点，递归
                classLabel=classify(secondDict[key],featLabels,testVec)
            else:#如果是叶结点,当前值就是类别
                classLabel=secondDict[key]
    return classLabel

def storeTree(inputTree,filename):#利用pickle模块序列化对象
    import pickle
    fw=open(filename,'wb')#必须是wb,二进制
    pickle.dump(inputTree,fw)#把inputTree放入filename文件中保存
    fw.close()

def grabTree(filename):
    import pickle
    fr=open(filename,'rb')#必须是rb,二进制
    return pickle.load(fr)#取出filename中的对象












    

    






    
