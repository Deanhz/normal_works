from numpy import *
import matplotlib
import matplotlib.pyplot as plt

def loadDataSet(fileName,delim='\t'): #可以直接使用numpy自带的loadtxt函数
    fr=open(fileName)
    stringArr=[line.strip().split(delim) for line in fr.readlines()]
    datArr=[list(map(float,line)) for line in stringArr]
    return mat(datArr)

def pca(dataMat,topNfeat=99999):#参数：样本矩阵;要转化到的维数
    meanVals=mean(dataMat,axis=0) #求均值
    meanRemoved=dataMat-meanVals  #减均值
    covMat=cov(meanRemoved,rowvar=0) #求协方差矩阵
    eigVals,eigVects=linalg.eig(mat(covMat)) #求协方差矩阵的特征值和特征向量
    eigValInd=argsort(eigVals) #对特征值排序，返回下标
    eigValInd=eigValInd[:-(topNfeat+1):-1] #从大到小取前topNfeat个对应的下标
    redEigVects=eigVects[:,eigValInd] #取前topNfeat个特征向量
    lowDDataMat=meanRemoved*redEigVects #新的向量空间下的坐标，也就是在特征向量下的投影坐标
    reconMat=lowDDataMat*redEigVects.T+meanVals #把新向量空间的下的坐标转化到原始坐标系中(仅为了可视化)
    return lowDDataMat,reconMat #返回新向量空间下的坐标，和其在原始坐标系下的坐标
##############################
#说明：testSetPCA的样本是二维的，topNfeat>=2时，不能转换到更高维,求出的特征向量最多只有两个，
#此时lowDDataMat仍然是二维的样本集，此时对应的reconMat坐标和dataMat对应的坐标是完全一致的；
#此时整个变换过程相当于，把原始的x、y旋转了一下，变换成新的x、y轴，
#最后的reconMat相当于又把坐标轴旋转回来了。
#############################

def plot(dataMat,reconMat):#绘图
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.scatter(dataMat[:,0].T.A[0],dataMat[:,1].T.A[0],marker='^',s=50)#原始数据集
    ax.scatter(reconMat[:,0].T.A[0],reconMat[:,1].T.A[0],marker='o',s=20,c='red')#新向量空间下坐标在原始空间的坐标
    plt.show()

def replaceNanWithMean():#把数据中的缺失值(NaN)用均值替换
    datMat=loadDataSet('secom.data',' ')
    numFeat=shape(datMat)[1]
    for i in range(numFeat):
        meanVal=mean(datMat[nonzero(~isnan(datMat[:,i]))[0],i])
        datMat[nonzero(isnan(datMat[:,i]))[0],i]=meanVal
    return datMat
def PCA_secom():#PCA分析，分析一下大约有多少最重要的主成分
    datMat=replaceNanWithMean()#缺失值替换
    meanVals=mean(datMat,axis=0) #求均值
    meanRemoved=datMat-meanVals #减去均值
    covMat=cov(meanRemoved,rowvar=0) #求协方差矩阵
    eigVals,eigVects=linalg.eig(mat(covMat)) #求协方差矩阵的特征值和特征向量
    eigValInd=argsort(eigVals) #对所有特征值进行排序，返回下标
    eigValInd=eigValInd[::-1] #reverse一下，从大到小的下标
    sortedEigVals=eigVals[eigValInd] #排序后的特征值
    total=sum(sortedEigVals) #特征值的总和
    varPercentage=sortedEigVals/total*100 #每个特征值(主成份)的贡献率(占的比率)，越大说明这个主成分越重要

    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.plot(range(1,21),varPercentage[:20],marker='^')#画出前20个主成分的贡献率
    plt.xlabel('Principal Component Number')
    plt.ylabel('Percentage of Variance')
    plt.show()#通过分析，从大到小，第6个主成分以后的主成份贡献率接近为0，所以可以把这个590维的数据降到6维；从而把590个特征简化成6个特征，大概实现了100:1的压缩


def test1():
    dataArr=loadDataSet(r'd:/python34/ML/testSetPCA.txt')
    lowDDataMat,reconMat=pca(dataArr,1)#如果参数>=2,仍然是2维坐标，只不过是新的坐标轴而已，还原到
    plot(dataArr,reconMat)             #原始坐标系中，可以发现与原始数据集完全重合。

def test2():
    PCA_secom()#主成分分析，数据源是secom.data
    #通过以上分析，可以选择参数为6，把数据集降到6维
    datMat=replaceNanWithMean()#缺失值替换
    lowDDataMat,reconMat=pca(datMat,6)
    print(lowDDataMat[0:20,:])#输出降维后的数据集前20个样本
    

if __name__=='__main__':
    test2()
    
