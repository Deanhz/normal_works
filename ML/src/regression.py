from numpy import *
import matplotlib.pyplot as plt
import math

def loadDataSet(fileName):#读数据
    numFeat=len(open(fileName).readline().split('\t'))-1
    dataMat=[]
    labelMat=[]
    fr=open(fileName)
    for line in fr.readlines():
        lineArr=[]
        curLine=line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat,labelMat

def standRegres(xArr,yArr):#利用公式w=[(xT*x)^-1]*(xT*y)
    xMat=mat(xArr)
    yMat=mat(yArr).T
    xTx=xMat.T*xMat
    if linalg.det(xTx)==0:#判断是否可逆
        print('this matrix cannot inverse')
        return
    ws=xTx.I*(xMat.T*yMat)
    return ws

def plotStandRegres(xArr,yArr,ws):#画标准线性回归拟合图
    xMat=mat(xArr)
    yMat=mat(yArr)
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.scatter(xMat[:,1].T.A[0],yMat.A[0]) #画散点
    xCopy=xMat.copy()
    xCopy.sort(0) #依次对每一列排序
    yPre=xCopy*ws #y=x*ws
    ax.plot(xCopy[:,1].T.A[0],yPre.T.A[0])
    plt.show()

def lwlr(testPoint,xArr,yArr,k=1.0):#局部加权回归函数。testPoint是一个测试样本,xArr是训练数据集，yArr是对应值，k是参数
    xMat=mat(xArr)
    yMat=mat(yArr).T
    m,n=shape(xArr)
    weights=mat(eye(m))
    for j in range(m):#计算weights权值矩阵
        diffMat=testPoint-xMat[j,:]
        weights[j,j]=exp(diffMat*diffMat.T/(-2.0*k**2))
    xTx=xMat.T*weights*xMat
    if linalg.det(xTx)==0:
        print('this matrix cannot inverse')
        return
    ws=xTx.I*xMat.T*weights*yMat
    yPre=testPoint*ws
    return yPre.A[0][0]

def lwlrTest(testArr,xArr,yArr,k=1.0):#testArr是测试样本集
    m=shape(testArr)[0]
    yPre=zeros(m)
    for i in range(m):
        yPre[i]=lwlr(testArr[i],xArr,yArr,k)
    return yPre
def plotLWLR(xArr,yArr,yPre,k):#画局部加权回归拟合图,yPre是xArr预测的值集合，k是参数
    xMat=mat(xArr)
    srtInd=xMat[:,1].argsort(0) #按列排序，返回下标
    xsort=xMat[srtInd][:,0,:]
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.plot(xsort[:,1].T.A[0],yPre[srtInd])#拟合线
    ax.scatter(xMat[:,1].T.A[0],yArr,s=9,c='red')#数据散点图
    plt.show()

def rssError(yArr,yPreArr):#求残差平方和，越小说明拟合的越好
    return ((yArr-yPreArr)**2).sum()

def regularize(xMat):#标准化函数
    inMat=xMat.copy()
    inMeans=mean(inMat,0)
    inVar=var(inMat,0)
    reMat=(inMat-inMeans)/sqrt(inVar) #如果inVar中有0，那么reMat对应的值就是nan
    #m,n=shape(reMat)
    #for j in range(n):#把矩阵中的nan替换为0
    #    if math.isnan(reMat[0,j]):
    #        for i in range(m):
    #            reMat[i,j]=0
    return reMat


def ridgeRegres(xMat,yMat,lam=0.2):#岭回归
    xTx=xMat.T*xMat
    denom=xTx+eye(shape(xMat)[1])*lam
    if linalg.det(denom)==0:
        print('this matrix cannot do inverse')
        return
    ws=denom.I*(xMat.T*yMat)
    return ws
def ridgeTest(xArr,yArr):#取30个不同的lamda参数，求出30个不同的weights，分析他们的效果和不同
    xMat=mat(xArr)
    yMat=mat(yArr).T
    yMean=mean(yMat,0)
    xMat=regularize(xMat) #标准化
    yMat=yMat-yMean
    numTestPts=30
    wMat=zeros((numTestPts,shape(xMat)[1])) #矩阵，每一行是一个weights,共30行
    for i in range(numTestPts):
        ws=ridgeRegres(xMat,yMat,exp(i-10))#lamda是指数变化，这样可以取到非常小和非常大的值，从而看出显著的影响
        wMat[i,:]=ws.T
    return wMat #30个不同的lamda参数对应w的矩阵
def ridgePre(w,testArr,xArr,yArr):
    testMat=mat(testArr)
    xMat=mat(xArr)
    yMat=mat(yArr)
    m,n=shape(testMat)
    yPre=zeros(m)
    for i in range(m):
        yPre[i]=w*testMat[i].T
    return yPre
    

def stageWise(xArr,yArr,eps=0.01,numIt=100):#前向逐步回归求w;eps是步长，numIt是迭代次数
    xMat=mat(xArr)
    yMat=mat(yArr).T
    xMat=regularize(xMat)
    yMat=regularize(yMat)
    m,n=shape(xMat)
    returnMat=zeros((numIt,n))
    ws=zeros((n,1))
    wsTest=ws.copy()
    wsMax=ws.copy()
    for i in range(numIt):#迭代numIt次,每次求出移动后误差率最小的那个w
        lowestError=inf
        for j in range(n):#遍历每个特征，依次对每个特征变化一个步长
            for s in [-1,1]: #步长是s*eps,两个方向都遍历
                wsTest=ws.copy()
                wsTest[j]+=eps*s
                yTest=xMat*wsTest
                rssE=rssError(yMat.A,yTest.A)
                if rssE<lowestError:
                    lowestError=rssE
                    wsMax=wsTest
        ws=wsMax.copy()
        returnMat[i,:]=ws.T
    return returnMat #矩阵，第m行是第m+1次迭代后的w

   


    

def test1():#ex0的数据有两个特征，x0=1,x1;#所以求出来的线性模型是y=w0+w1*x1
    xArr,yArr=loadDataSet(r'D:/python34/ML/ex0.txt')
    ws=standRegres(xArr,yArr)
    plotStandRegres(xArr,yArr,ws)
    print(ws)
    xMat=mat(xArr)
    yMat=mat(yArr)
    yPre=xMat*ws #求预测值
    e=corrcoef(yPre.T,yMat)#计算yPre和yHat的相关系数矩阵，使用了numpy的函数，默认是行向量，如果是列向量需要参数rowvar=0
    print(e)
def test2():
    xArr,yArr=loadDataSet(r'D:/python34/ML/ex0.txt')
    yPre=lwlrTest(mat(xArr),xArr,yArr,0.01)#对整个样本集求预测值
    plotLWLR(xArr,yArr,yPre,0.01)#画拟合图
    print(yPre)
def test3():#通过预测鲍鱼年龄。分析取不同参数时的训练误差和测试误差
    abX,abY=loadDataSet(r'd:/python34/ML/abalone.txt')
    yPre1=lwlrTest(abX[0:99],abX[0:99],abY[0:99],0.1)
    yPre2=lwlrTest(abX[0:99],abX[0:99],abY[0:99],1)
    yPre3=lwlrTest(abX[0:99],abX[0:99],abY[0:99],10)
    #以下计算的是训练误差
    print(rssError(abY[0:99],yPre0.T))
    print(rssError(abY[0:99],yPre1.T)) #56.7
    print(rssError(abY[0:99],yPre2.T)) #429.8
    print(rssError(abY[0:99],yPre3.T)) #549
    yPre11=lwlrTest(abX[100:199],abX[0:99],abY[0:99],0.1)
    yPre22=lwlrTest(abX[100:199],abX[0:99],abY[0:99],1)
    yPre33=lwlrTest(abX[100:199],abX[0:99],abY[0:99],10)
    #以下计算的是测试误差
    print(rssError(abY[100:199],yPre00.T))
    print(rssError(abY[100:199],yPre11.T))#36531.0
    print(rssError(abY[100:199],yPre22.T))#573.5
    print(rssError(abY[100:199],yPre33.T))#517.5
def test4():#岭回归测试
    abX,abY=loadDataSet(r'd:/python34/ML/abalone.txt')
    xMat=mat(abX)
    yMat=mat(abY).T
    ws=standRegres(abX,abY)
    ridgeWeights=ridgeTest(abX,abY)
    yPre=ridgePre(ridgeWeights[0],abX[0:99],abX[0:99],abY[0:99])
    #unreguYpre=unregularize(mat(yPre).T,yMat[0:99])
    #print(unreguYpre)
    print(yPre)
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.plot(ridgeWeights)
    plt.show()
    print(ridgeWeights[0])
    #yPre1=xMat[0:99]*ws #求预测值
    print(ws)
    #print(yPre1)
def test5():#前向逐步回归测试
    xArr,yArr=loadDataSet(r'd:/python34/ML/abalone.txt')
    ws=stageWise(xArr,yArr,0.001,6000)
    xMat=regularize(xArr)#因为前向逐步回归中应用了标准化，为了和标准线性回归比较,
    yMat=regularize(yArr)#在应用标准线性回归之前，也对数据进行标准化处理
    ws2=standRegres(xMat,yMat)
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.plot(ws) #画出w每个分量变化情况
    plt.show()
    print(ws)
    print(ws2.T)




    
#在test2中设置不同k值，当k=1时，拟合线近似直线，效果与最小二乘法差不多。
#当k=0.01时，拟合效果比较理想。当k=0.003时，过拟合，考虑了太多的噪声
#总结线性回归和局部加权回归的不同.
#局部加权回归的拟合效果比线性回归要好，但是它的计算量比较大。因为求参数w，线性回归w=[(xT*x)^-1]*xT*y 对每个点是一样的w;
#而局部加权回归的w是根据每个点的权值矩阵weights而不同的，所以每个点有不同的weights,每次都得求w,拟合了m条直线(m是测试样本个数)

#通过test3()发现，k=0.1时训练误差最小，但是测试误差最大，造成了过拟合;k=10时，训练误差较大，但是测试误差较小，具有很好的预测效果        
#k的取值要根据其数据集合，分析其训练误差和测试误差，综合分析取值。
    
#岭回归和前向逐步回归都求出了w的集合，是矩阵的形式，每一行是一个w,对应着不同的线性模型，我们可以通过其他方法再来判断到底哪个w的效果更好。
#岭回归求出w的集合，可以利用留一交叉验证和计算残差平方和 来选择最佳的那个w
########################################################################################
from time import sleep
import json
import urllib
def scrapePage(inFile,outFile,yr,numPce,origPrc):
    from bs4 import BeautifulSoup
    fr = open(inFile,encoding='utf8');#一定要用utf8解码
    fw=open(outFile,'a') #a is append mode writing
    soup = BeautifulSoup(fr.read())
    i=1
    currentRow = soup.findAll('table', r="%d" % i)
    while(len(currentRow)!=0):
        currentRow = soup.findAll('table', r="%d" % i)
        title = currentRow[0].findAll('a')[1].text
        lwrTitle = title.lower()
        if (lwrTitle.find('new') > -1) or (lwrTitle.find('nisb') > -1):
            newFlag = 1.0
        else:
            newFlag = 0.0
        soldUnicde = currentRow[0].findAll('td')[3].findAll('span')
        if len(soldUnicde)==0:
            print ("item #%d did not sell" % i)
        else:
            soldPrice = currentRow[0].findAll('td')[4]
            priceStr = soldPrice.text
            priceStr = priceStr.replace('$','') #strips out $
            priceStr = priceStr.replace(',','') #strips out ,
            if len(soldPrice)>1:
                priceStr = priceStr.replace('Free shipping', '') #strips out Free Shipping
            print ("%s\t%d\t%s" % (priceStr,newFlag,title))
            fw.write("%d\t%d\t%d\t%f\t%s\n" % (yr,numPce,newFlag,origPrc,priceStr))
        i += 1
        currentRow = soup.findAll('table', r="%d" % i)
    fw.close()
    
def setDataCollect():
    scrapePage('setHtml/lego8288.html','out.txt', 2006, 800, 49.99)
    scrapePage('setHtml/lego10030.html','out.txt', 2002, 3096, 269.99)
    scrapePage('setHtml/lego10179.html','out.txt', 2007, 5195, 499.99)
    scrapePage('setHtml/lego10181.html','out.txt', 2007, 3428, 199.99)
    scrapePage('setHtml/lego10189.html','out.txt', 2008, 5922, 299.99)
    scrapePage('setHtml/lego10196.html','out.txt', 2009, 3263, 249.99)

def mytest1():
    lgX,lgY=loadDataSet(r'd:/python34/ML/out.txt')
    
    lgX1=mat(ones((63,5)))
    lgX1[:,1:5]=mat(lgX)
    ws=standRegres(lgX1,lgY)
    print(lgX1[0]*ws)
    print(lgX1[-1]*ws)
    
################################################################################################
def crossValidation(xArr,yArr,numVal=10):#K-fold 交叉验证，共验证K=numVal次
    m = len(yArr)                           
    indexList = list(range(m))
    errorMat = zeros((numVal,30))#第ij个元素是，第i+1次验证时，第j+1次取参lamda得到的误差
    for i in range(numVal):#重复numVal次
        trainX=[]; trainY=[]
        testX = []; testY = []
        random.shuffle(indexList)
        for j in range(m):#随机取90%做训练数据集，10%做测试数据集。这里的K=10，所以1/10的数据集作为测试集，9/10作为训练集。
            if j < m*0.9: 
                trainX.append(list(xArr[indexList[j]]))
                trainY.append(yArr[indexList[j]])
            else:
                testX.append(list(xArr[indexList[j]]))
                testY.append(yArr[indexList[j]])
        wMat=ridgeTest(trainX,trainY)#w的矩阵，每一行对应着不同的lamda参数
        for k in range(30):#计算30个误差，因为共30个不同的w
            matTestX = mat(testX); matTrainX=mat(trainX)
            meanTrain = mean(matTrainX,0)
            varTrain = var(matTrainX,0)
            matTestX = (matTestX-meanTrain)/varTrain #regularize test with training params
            yEst = matTestX * mat(wMat[k,:]).T + mean(trainY)  
            errorMat[i,k]=rssError(yEst.T.A,array(testY)) #放到矩阵的i,k个元素位置
            
    meanErrors = mean(errorMat,0)#按列求均值
    minMean = float(min(meanErrors))#最小的那个平均误差
    bestWeights = wMat[nonzero(meanErrors==minMean)]#最小的那个平均误差对应的w
    xMat = mat(xArr); yMat=mat(yArr).T
    meanX = mean(xMat,0); varX = var(xMat,0)
    xMat=(xMat-meanX)/varX
    yPre=xMat*bestWeights.T+ mean(yMat) #求其预测结果，列向量
    print(yPre)
    
        

def mytest2():#交叉验证
    lgX,lgY=loadDataSet(r'd:/python34/ML/out.txt')
    crossValidation(lgX,lgY)
def mytest3():#原始岭回归
    lgX,lgY=loadDataSet(r'd:/python34/ML/out.txt')
    w=ridgeTest(lgX,lgY)
    print(w)



if __name__=='__main__':
    test2()
















    
