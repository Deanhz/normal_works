from numpy import *

def loadDataSet(fileName):#读数据
    dataMat=[]
    fr=open(fileName)
    for line in fr.readlines():
        curLine=line.strip().split('\t')
        fltLine=list(map(float,curLine))
        dataMat.append(fltLine)
    return dataMat

def distEclud(vecA,vecB):#计算向量的距离
    return sqrt(sum(power(vecA-vecB,2))) 

def randCent(dataSet,k):#随机生成簇质心集合
    m,n=shape(dataSet)
    centroids=mat(zeros((k,n)))#簇质心，k行n列的矩阵
    for j in range(n):
        minJ=min(dataSet[:,j])
        maxJ=max(dataSet[:,j])
        rangeJ=float(maxJ-minJ)
        centroids[:,j]=minJ+rangeJ*random.rand(k,1)
    return centroids

def kMeans(dataSet,k,distMeans=distEclud,createCent=randCent):#K-均值聚类算法
    m=shape(dataSet)[0]
    clusterAssment=mat(zeros((m,2)))#m行2列矩阵，第一列保存簇索引，第二列保存到簇质心的距离的平方
    centroids=createCent(dataSet,k)#生成最初的簇质心集合
    clusterChanged=True #标志是否发生改变
    while clusterChanged:
        clusterChanged=False
        for i in range(m):#遍历每个样本点
            minDist=inf #保存最小距离
            minIndex=-1 #最小距离对应的簇质心的索引
            for j in range(k):#遍历每个簇质心
                distJI=distMeans(centroids[j,:],dataSet[i,:]) #计算距离
                if distJI<minDist: 
                    minDist=distJI
                    minIndex=j
            if clusterAssment[i,0]!=minIndex:#如果原来保存的索引和本次不一样，则标志位=True
                clusterChanged=True
            clusterAssment[i,:]=minIndex,minDist**2 #更新
        #print(centroids)
        for cent in range(k):#更新每个质心
            ptsInClust=dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]#属于该簇的所有点
            centroids[cent,:]=mean(ptsInClust,axis=0)#该簇质心的值是属于该簇所有点的均值
    return centroids,clusterAssment #返回最终的簇质心集合，记录每个点分配的结果
#############################################################################################
#####二分K-均值聚类算法
#伪代码：
#     将所有点看成一个簇
#     当簇数目小于K时
#           对每一个簇：
#               计算总误差 
#               在给定的簇上面进行K-均值聚类(K=2)
#               计算将该簇一分为二后的总误差
#           选择使得误差最小的那个簇进行划分操作

def biKmeans(dataSet,k,distMeans=distEclud):#
    m=shape(dataSet)[0]
    clusterAssment=mat(zeros((m,2))) #保存每个样本的分配结果
    centroid0=mean(dataSet,axis=0).tolist()[0] #首先将所有点看作同一个簇，值是均值
    centList=[centroid0] #簇集合
    for j in range(m):#初始化分配结果矩阵。只需要赋值第二列，因为第一列已经全是0，正好是第一个簇的索引
        clusterAssment[j,1]=distMeans(mat(centroid0),dataSet[j,:])**2
    while (len(centList)<k):#当簇数目小于K时
        lowestSSE=inf
        for i in range(len(centList)):#遍历每一个簇，选择一个簇进行划分
            ptsInCurrCluster=dataSet[nonzero(clusterAssment[:,0].A==i)[0],:]#属于当前簇的样本集合
            centroidMat,splitClustAss=kMeans(ptsInCurrCluster,2,distMeans)#对当前簇样本进行划分
            sseSplit=sum(splitClustAss[:,1])#当前簇划分后的误差
            sseNotSplit=sum(clusterAssment[nonzero(clusterAssment[:,0].A!=i)[0],1])#其他簇的总误差
            if (sseSplit+sseNotSplit)<lowestSSE: #如果划分后的簇误差加上其他簇的误差小于 lowestSSE
                bestCentToSplit=i #最优划分簇的索引
                bestNewCents=centroidMat #划分后的簇集合
                bestClustAss=splitClustAss.copy() #当前簇的样本划分后的分配结果矩阵
                lowestSSE=sseSplit+sseNotSplit #更新lowestSSE
        bestClustAss[nonzero(bestClustAss[:,0].A==0)[0],0]=bestCentToSplit #更新划分得到的分配表的第0列。值更新为本次划分的簇索引
        bestClustAss[nonzero(bestClustAss[:,0].A==1)[0],0]=len(centList)   #更新划分得到的分配表的第1列。值更新为簇集合最后一个簇的索引
        centList[bestCentToSplit]=bestNewCents[0,:].tolist()[0] #对簇集合进行更新。把簇集合中的最优簇更新为划分后的第0簇
        centList.append(bestNewCents[1,:].tolist()[0])          #簇集合末尾追加划分后的第1簇
        clusterAssment[nonzero(clusterAssment[:,0].A == bestCentToSplit)[0],:]= bestClustAss #更新总的分配结果矩阵，用划分得到的分配表替换
    return mat(centList),clusterAssment#返回簇集合，分配结果矩阵

##############################################################################################
def test1():
    dataSet=loadDataSet(r'd:/python34/ML/testSet_10.txt')
    dataMat=mat(dataSet)
    print(randCent(dataMat,10))
def test2():
    dataSet=loadDataSet(r'd:/python34/ML/testSet_10.txt')
    dataMat=mat(dataSet)
    myCentroids,clusAssing=kMeans(dataMat,3)
    print(myCentroids)
    print(clusAssing)
def test3():
    dataSet=loadDataSet(r'd:/python34/ML/testSet2_10.txt')
    dataMat=mat(dataSet)
    centList,myNewAssment=biKmeans(dataMat,3)
    print(centList)
    


if __name__=='__main__':
    test2()
