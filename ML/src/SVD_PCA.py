from numpy import *

def loadExData2():
    return[[0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 5],
           [0, 0, 0, 3, 0, 4, 0, 0, 0, 0, 3],
           [0, 0, 0, 0, 4, 0, 0, 1, 0, 4, 0],
           [3, 3, 4, 0, 0, 0, 0, 2, 2, 0, 0],
           [5, 4, 5, 0, 0, 0, 0, 5, 5, 0, 0],
           [0, 0, 0, 0, 5, 0, 1, 0, 0, 5, 0],
           [4, 3, 4, 0, 0, 0, 0, 5, 5, 0, 1],
           [0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 4],
           [0, 0, 0, 2, 0, 2, 5, 0, 0, 1, 2],
           [0, 0, 0, 0, 5, 0, 0, 0, 0, 4, 0],
           [1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0]]

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
    return lowDDataMat

def svd(dataMat,topNfeat=6):
    meanVals=mean(dataMat,axis=0)
    meanRemoved=dataMat-meanVals
    U,sigma,VT=linalg.svd(meanRemoved)
    EigVects=VT[:topNfeat,:].T
    lowDDataMat=meanRemoved*EigVects
    return lowDDataMat
def svd2(dataMat,topNfeat):
    dataMat2=dataMat.T
    meanVals=mean(dataMat2,axis=0)
    meanRemoved=dataMat2-meanVals
    U,sigma,VT=linalg.svd(meanRemoved)
    EigVects=VT[:topNfeat,:].T
    lowDDataMat=meanRemoved*EigVects
    lowDDataMat2=lowDDataMat.T
    return lowDDataMat2
def svd3(dataMat,topNfeat):
    meanVals=mean(dataMat,axis=0)
    meanRemoved=dataMat-meanVals
    U,sigma,VT=linalg.svd(meanRemoved)
    EigVects=U[:,:topNfeat].T
    lowDDataMat=EigVects*meanRemoved
    return lowDDataMat
    

def test():
    dataArr=loadtxt(r'd:/python34/ML/testSetPCA.txt')
    data1=pca(mat(dataArr))
    data2=svd(mat(dataArr))
    print(data1[0:10,:])
    print(data2[0:10,:])
def test2():
    dataArr=loadExData2()
    lowDData1=svd2(mat(dataArr),4)
    print(lowDData1)
    lowDData2=svd3(mat(dataArr),4)
    print(lowDData2)
def test3():
    dataArr=loadExData2()
    myData=mat(dataArr)
    U,sigma,VT=linalg.svd(myData)
    data1=U[:,:4].T*myData
    print(VT[:4,:].T)
    
    

if __name__=='__main__':
    test3()
    
