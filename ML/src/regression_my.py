from numpy import *
import matplotlib.pyplot as plt
import math

def loadDataSet(fileName):
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

def standRegres(xArr,yArr):#直接公式求出ws
    xMat=mat(xArr)
    yMat=mat(yArr).T
    xTx=xMat.T*xMat
    if linalg.det(xTx)==0:
        return
    ws=xTx.I*(xMat.T*yMat)
    return ws

def gradDesc(xArr,yArr):#批梯度下降法，结果肯定不如上面的准确
    xMat=mat(xArr)
    yMat=mat(yArr).T
    m,n=shape(xMat)
    alpha=0.001 #设置0.001比较理想，0.01直接导致结果错误
    maxCycle=30 #当α是0.001时，30次迭代差不多收敛
    ws=ones((n,1))
    for k in range(maxCycle):
        ws=ws-alpha*xMat.T*(xMat*ws-yMat)
    return ws
def plotStandRegres(xArr,yArr,ws):
    xMat=mat(xArr)
    yMat=mat(yArr)
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.scatter(xMat[:,1].T.A[0],yMat.A[0],s=20) #画散点
    xCopy=xMat.copy()
    yPre=xCopy*ws
    ax.plot(xCopy[:,1].T.A[0],yPre.T.A[0])
    plt.show()

def lwlr(testPoint,xArr,yArr,k=1.0):
    xMat=mat(xArr)
    yMat=mat(yArr).T
    m,n=shape(xArr)
    weights=mat(eye(m))
    for j in range(m):
        diffMat=testPoint-xMat[j,:]
        weights[j,j]=exp(diffMat*diffMat.T/(-2.0*k**2))
    xTx=xMat.T*weights*xMat
    if linalg.det(xTx)==0:
        return
    ws=xTx.I*xMat.T*weights*yMat
    yPre=testPoint*ws
    return yPre[0,0]

def lwlrTest(testArr,xArr,yArr,k=1.0):
    m=shape(testArr)[0]
    yPre=zeros(m)
    for i in range(m):
        yPre[i]=lwlr(testArr[i],xArr,yArr,k)
    return yPre

def plotLWLR(xArr,yArr,yPre):
    xMat=mat(xArr)
    srtInd=xMat[:,1].argsort(0)
    xsort=xMat[srtInd][:,0,:]
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.scatter(xMat[:,1].T.A[0],yArr,s=9,c='red')
    ax.plot(xsort[:,1].T.A[0],yPre[srtInd])
    plt.show()
    
    


    



def test1():#线性回归
    dataMat,labelMat=loadDataSet(r'D:/python34/ML/ex0.txt')
    ws=standRegres(dataMat,labelMat)
    plotStandRegres(dataMat,labelMat,ws)
    print(ws)
def test2():
    xArr,yArr=loadDataSet(r'D:/python34/ML/ex0.txt')
    yHat=lwlrTest(xArr,xArr,yArr,0.03)
    plotLWLR(xArr,yArr,yHat)
    
if __name__=='__main__':
    test2()
