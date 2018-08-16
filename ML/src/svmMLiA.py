#支持向量机，利用SMO求解

import random
from numpy import *
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def loadDataSet(fileName):#创建(加载)数据
    dataMat=[]
    labelMat=[]
    fr=open(fileName)
    for line in fr.readlines():
        lineArr=line.strip().split('\t')
        dataMat.append([float(lineArr[0]),float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat,labelMat

def selectJrand(i,m):#i是第一个alpha的下标,m是所有alpha的数目。函数随机选择一个不等于i的alpha下标
    j=i
    while(j==i):
        j=int(random.uniform(0,m))
    return j

def clipAlpha(aj,H,L):#修剪函数。
    if aj>H:
        aj=H
    if aj<L:
        aj=L
    return aj

def smoSimple(dataMatIn,classLabels,C,toler,maxIter):#简化版的SMO算法,参数是:样本矩阵，类别列表，惩罚参数C,容忍度toler,最大迭代次数
    dataMatrix=mat(dataMatIn)
    labelMat=mat(classLabels).transpose()
    b=0;
    m,n=shape(dataMatrix)
    alphas=mat(zeros((m,1)))
    iter=0 #参数α没有发生变化的迭代次数
    while(iter<maxIter):#一直循环，直到连续maxIter次都没有发生变化才结束
        alphaPairsChanged=0#标志是否改变
        for i in range(m):
            fXi=float(multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[i,:].T))+b#f(xi)
            Ei=fXi-float(labelMat[i])#Ei=f(xi)-yi
            if ((labelMat[i]*Ei<-toler) and (alphas[i]<C)) or ((labelMat[i]*Ei>toler) and (alphas[i]>0)):#判断i样本是否违背KKT条件
                j=selectJrand(i,m)#随机取样j
                fXj=float(multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[j,:].T))+b #f(xj)
                Ej=fXj-float(labelMat[j]) #Ej=f(xj)-yj
                alphaIold=alphas[i].copy()#创建副本，为下面的比较做铺垫
                alphaJold=alphas[j].copy()
                if(labelMat[i]!=labelMat[j]):#yi!=yj,计算下界L和上界H
                    L=max(0,alphas[j]-alphas[i])
                    H=min(C,C+alphas[j]-alphas[i])
                else:
                    L=max(0,alphas[j]+alphas[i]-C)
                    H=min(C,alphas[j]+alphas[i])
                eta=2.0*dataMatrix[i,:]*dataMatrix[j,:].T-dataMatrix[i,:]*dataMatrix[i,:].T-dataMatrix[j,:]*dataMatrix[j,:].T #η=K11+K22-2K12,这里的eta=-η
                if eta>=0:continue #η不可能<=0,即eta不可能>=0;否则continue
                alphas[j]-=labelMat[j]*(Ei-Ej)/eta #计算未剪辑的α2
                alphas[j]=clipAlpha(alphas[j],H,L)#剪辑后的α2
                if(abs(alphas[j]-alphaJold)<0.00001):continue #如果几乎没有变化，则continue
                alphas[i]+=labelMat[i]*labelMat[j]*(alphaJold-alphas[j]) #更新α1
                b1=b-Ei-labelMat[i]*(alphas[i]-alphaIold)*dataMatrix[i,:]*dataMatrix[i,:].T-labelMat[j]*(alphas[j]-alphaJold)*dataMatrix[i,:]*dataMatrix[j,:].T
                b2=b-Ej-labelMat[i]*(alphas[i]-alphaIold)*dataMatrix[i,:]*dataMatrix[j,:].T-labelMat[j]*(alphas[j]-alphaJold)*dataMatrix[j,:]*dataMatrix[j,:].T
                if (alphas[i]>0) and (alphas[i]<C):b=b1
                elif (alphas[j]>0) and (alphas[j]<C):b=b2
                else:b=(b1+b2)/2
                alphaPairsChanged+=1
                print('iter:%d i:%d,pairs changed %d'%(iter,i,alphaPairsChanged))
        if (alphaPairsChanged==0):iter+=1
        else:iter=0
    return b,alphas


def kernelTrans(X,A,kTup):#核转换函数，参数：X样本矩阵，A某一个样本，kTup核信息元组。返回K是一个列向量，是K矩阵的某一列
    m,n=shape(X)
    K=mat(zeros((m,1)))
    if kTup[0]=='lin':K=X*A.T #线性核函数
    elif kTup[0]=='rbf': #径向基核函数
        for j in range(m):
            deltaRow=X[j,:]-A
            K[j]=deltaRow*deltaRow.T
        K=exp(K/(-1*kTup[1]**2))
    else: raise NameError('The Kernel is not recognized!')
    return K

class optStruct:
    def __init__(self,dataMatIn,classLabels,C,toler,kTup):
        self.X=dataMatIn
        self.labelMat=classLabels
        self.C=C
        self.tol=toler #容忍度
        self.m=shape(dataMatIn)[0]
        self.alphas=mat(zeros((self.m,1)))
        self.b=0 
        self.eCache=mat(zeros((self.m,2))) #存放Ei,第一列是标志位，第二列是Ei
        self.K=mat(zeros((self.m,self.m)))
        for i in range(self.m):#构造K矩阵
            self.K[:,i]=kernelTrans(self.X,self.X[i,:],kTup)

def calcEk(oS,k):#计算Ek
    fXk=float(multiply(oS.alphas,oS.labelMat).T*oS.K[:,k]+oS.b)
    Ek=fXk-float(oS.labelMat[k])
    return Ek

def selectJ(i,oS,Ei):#计算Ej
    maxK = -1; maxDeltaE = 0; Ej = 0
    oS.eCache[i] = [1,Ei]  
    validEcacheList = nonzero(oS.eCache[:,0].A)[0]#有效位是1的对应的下标array
    if (len(validEcacheList)) > 1:
        for k in validEcacheList:  
            if k == i: continue 
            Ek = calcEk(oS, k)
            deltaE = abs(Ei - Ek)
            if (deltaE > maxDeltaE):
                maxK = k; maxDeltaE = deltaE; Ej = Ek
        return maxK, Ej
    else:#第一次选择Ej的时候,随机选择   
        j = selectJrand(i, oS.m)
        Ej = calcEk(oS, j)
    return j, Ej
              
def updateEk(oS,k):#更新Ek
    Ek=calcEk(oS,k)
    oS.eCache[k]=[1,Ek]

def innerL(i,oS):#内循环
    Ei=calcEk(oS,i)
    if ((oS.labelMat[i]*Ei<-oS.tol) and (oS.alphas[i]<oS.C)) or ((oS.labelMat[i]*Ei>oS.tol) and (oS.alphas[i]>0) ):#如果Ei不违背KKT，不需要进行更新
        j,Ej=selectJ(i,oS,Ei)#选择最优j和Ej
        alphaIold=oS.alphas[i].copy()#创建副本
        alphaJold=oS.alphas[j].copy()
        if (oS.labelMat[i]!=oS.labelMat[j]):#求上限H和下限L
            L=max(0,oS.alphas[j]-oS.alphas[i])
            H=min(oS.C,oS.C+oS.alphas[j]-oS.alphas[i])
        else:
            L=max(0,oS.alphas[j]+oS.alphas[i]-oS.C)
            H=min(oS.C,oS.alphas[j]+oS.alphas[i])
        if L==H:return 0
        eta=2.0*oS.K[i,j]-oS.K[i,i]-oS.K[j,j]# η
        if eta>=0:return 0 
        oS.alphas[j]-=oS.labelMat[j]*(Ei-Ej)/eta#未剪辑的αj
        oS.alphas[j]=clipAlpha(oS.alphas[j],H,L)#剪辑后的αj
        updateEk(oS,j)#更新Ej
        if(abs(oS.alphas[j]-alphaJold)<0.00001):return 0#如果αj没有发生变化，则退出
        oS.alphas[i]+=oS.labelMat[j]*oS.labelMat[i]*(alphaJold-oS.alphas[j])#更新αi
        updateEk(oS,i)#更新Ei
        b1=oS.b-Ei-oS.labelMat[i]*(oS.alphas[i]-alphaIold)*oS.K[i,i]-oS.labelMat[j]*(oS.alphas[j]-alphaJold)*oS.K[i,j]
        b2=oS.b-Ej-oS.labelMat[i]*(oS.alphas[i]-alphaIold)*oS.K[i,j]-oS.labelMat[j]*(oS.alphas[j]-alphaJold)*oS.K[j,j]
        if ((oS.alphas[i]>0) and (oS.alphas[i]<oS.C)):oS.b=b1
        elif ((oS.alphas[j]>0) and (oS.alphas[j]<oS.C)):oS.b=b2
        else:oS.b=(b1+b2)/2.0
        return 1
    else:
        return 0

def smoP(dataMatIn,classLabels,C,toler,maxIter,kTup=('lin',0)):#SMO算法外层部分
    oS=optStruct(mat(dataMatIn),mat(classLabels).transpose(),C,toler,kTup)#初始化oS
    iter=0 #迭代次数
    entireSet=True #标志,整个数据集
    alphaPairsChanged=0 #标志，是否发生了变化
    while (iter < maxIter) and ((alphaPairsChanged>0) or (entireSet) ):
        alphaPairsChanged=0
        if entireSet:#遍历整个数据集
            for i in range(oS.m):
                temp=innerL(i,oS)
                alphaPairsChanged+=temp
                if(temp==1):print('fullSet,iter:%d i:%d,pairs changed'%(iter,i))
            iter+=1
        else:#遍历非边界α对应的数据集
            nonBoundIs=nonzero((oS.alphas.A>0)*(oS.alphas.A<C))[0]
            for i in nonBoundIs:
                temp=innerL(i,oS)
                alphaPairsChanged+=temp
                if(temp==1):print('fullSet,iter:%d i:%d,pairs changed'%(iter,i))
            iter+=1
        if entireSet:entireSet=False #本次遍历的是整个数据集，下次不再遍历整个数据集，如果本次遍历没有发生变化，则for循环退出
        elif(alphaPairsChanged==0):entireSet=True #本次是遍历的是非边界α对应的数据集，并且没有发生变化，那么下次遍历整个数据集
    print('iteration number:%d'%iter)
    return oS.b,oS.alphas

def calcWs(alphas,dataArr,classLabels):#计算w
    X=mat(dataArr)
    labelMat=mat(classLabels).transpose()
    m,n=shape(X)
    w=zeros((n,1))
    for i in range(m):
        w+=multiply(alphas[i]*labelMat[i],X[i,:].T)
    return w



def testRbf(k1=1.3):
    dataArr,labelArr=loadDataSet(r'd:/python34/ML/testSetRBF.txt')
    b,alphas=smoP(dataArr,labelArr,200,0.00001,10000,('rbf',k1))
    datMat=mat(dataArr)
    labelMat=mat(labelArr).transpose()
    svInd=nonzero(alphas.A>0)[0]#α>0对应的下标array
    sVs=datMat[svInd]#支持向量
    labelSV=labelMat[svInd]#支持向量对应的类标签
    print('there are %d Support Vectors'%shape(sVs)[0])
    m,n=shape(datMat)
    errorCount=0
    for i in range(m):#计算训练错误率
        kernelEval=kernelTrans(sVs,datMat[i,:],('rbf',k1))
        predict=kernelEval.T*multiply(labelSV,alphas[svInd])+b
        if sign(predict)!=sign(labelArr[i]):
            errorCount+=1
    print('the training error rate is:%f'%(float(errorCount/m)))
    dataArr,labelArr=loadDataSet(r'd:/python34/ML/testSetRBF2.txt')
    errorCount=0
    datMat=mat(dataArr)
    labelMat=mat(labelArr).transpose()
    m,n=shape(datMat)
    for i in range(m):#计算预测错误率
        kernelEval=kernelTrans(sVs,datMat[i,:],('rbf',k1))
        predict=kernelEval.T*multiply(labelSV,alphas[svInd])+b
        if sign(predict)!=sign(labelArr[i]):errorCount+=1
    print('the test error rate is:%f'%(float(errorCount/m)))
    return datMat,labelMat,sVs,labelSV

    
    
    
              
    


def test():
    dataArr,labelArr=loadDataSet(r'./testSet.txt')
    b,alphas=smoP(dataArr,labelArr,0.6,0.001,40)
    ws=calcWs(alphas,dataArr,labelArr)
    datMat=mat(dataArr)
    c=datMat*ws+b
    #print(ws)
    print(c)

def plotSV():
    dataArr,labelArr=loadDataSet(r'./testSetRBF.txt')
    m,n=shape(dataArr)
    b,alphas=smoP(dataArr,labelArr,200,0.00001,10000,('rbf',0.5))
    datMat=mat(dataArr)
    labelMat=mat(labelArr).transpose()
    svInd=nonzero(alphas.A>0)[0]#α>0对应的下标array
    sumSv=len(svInd)
    print('the number of SV is %d'%sumSv)
    
    x1cord0=[]#-1类的点
    x2cord0=[]
    x1cord1=[]#1类的点
    x2cord1=[]
    svx1=[]#支持向量
    svx2=[]
    for i in range(m):
        if i in svInd:
            svx1.append(dataArr[i][0])
            svx2.append(dataArr[i][1])
        if labelArr[i]==-1:
            x1cord0.append(dataArr[i][0])
            x2cord0.append(dataArr[i][1])
        else:
            x1cord1.append(dataArr[i][0])
            x2cord1.append(dataArr[i][1])
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.scatter(x1cord0,x2cord0,marker='s',s=60)#画类-1的点
    ax.scatter(x1cord1,x2cord1,marker='o',s=60)#画类1的点
    for i in range(sumSv):#只能通过循环依次画每个圈
        circle=Circle((svx1[i],svx2[i]),0.04,facecolor='none',edgecolor=(0,0.8,0.8),linewidth=3,alpha=0.5)
        ax.add_patch(circle)
    plt.show()
    

if __name__=='__main__':
    test()
    plotSV()
   




    
    
#100个样本点分类时，径向基函数的参数k的不同取值情况,
#当k=0.1时,支持向量个数为85左右，训练错误率约为0，测试错误率约为0.07
#当k=0.5时,支持向量个数为23左右，训练错误率约为0，测试错误率约为0.06
#当k=1.3时,支持向量个数为26左右，训练错误率约为0.09，测试错误率约为0.16
#当k=2时,支持向量个数为31左右，训练错误率约为0.09，测试错误率约为0.16
#当k=3时,支持向量个数为43左右，训练错误率约为0.05，测试错误率约为0.16
