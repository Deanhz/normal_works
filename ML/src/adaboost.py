from numpy import *
import matplotlib.pyplot as plt
def loadSimpData():#创建数据集
    datMat=mat([[1.,2.1],
                [2.,1.1],
                [1.3,1.],
                [1.,1.],
                [2.,1.]])
    classLabels=[1,1,-1,-1,1]
    return datMat,classLabels

def stumpClassify(dataMatrix,dimen,threshVal,threshIneq):#根据阀值进行分类。参数:数据矩阵，第dimen个特征值,阀值,不等式(lt是小于号,gt是大于号)
    retArray=ones((shape(dataMatrix)[0],1)) #列向量，初始化为1
    if threshIneq=='lt':                #根据不等式，把满足条件的对应数值置为-1
        retArray[dataMatrix[:,dimen]<=threshVal]=-1.0
    else:
        retArray[dataMatrix[:,dimen]>threshVal]=-1.0
    return retArray

def buildStump(dataArr,classLabels,D):#(根据分类误差最小)构建的最优单层决策树(弱分类器)
    dataMatrix=mat(dataArr)
    labelMat=mat(classLabels).T
    m,n=shape(dataMatrix)
    numSteps=10 #总的步数
    bestStump={}#保存最优分类器的有关信息
    bestClasEst=mat(zeros((m,1)))#最优的分类情况
    minError=inf# inf代表正无穷大
    for i in range(n):#遍历每一个特征
        rangeMin=dataMatrix[:,i].min()#该特征的最小值
        rangeMax=dataMatrix[:,i].max()#最大值
        stepSize=(rangeMax-rangeMin)/numSteps#每一步的大小
        for j in range(-1,numSteps+1):#遍历每一步
            for inequal in ['lt','gt']:#遍历＜和＞不等号
                threshVal=rangeMin+stepSize*j #阀值
                predictedVals=stumpClassify(dataMatrix,i,threshVal,inequal) #根据阀值条件分类的情况
                errArr=mat(ones((m,1)))#错误向量，初始化为1
                errArr[predictedVals==labelMat]=0 #把预测正确的对应值置为0
                weightedError=D.T*errArr #分类误差率
                #print('split: dim %d,thresh %.2f,thresh inequal:%s,the weighted error is %.3f'%(i,threshVal,inequal,weightedError))
                if weightedError<minError:#找最小的分类误差率
                    minError=weightedError
                    bestClasEst=predictedVals.copy()
                    bestStump['dim']=i
                    bestStump['thresh']=threshVal
                    bestStump['ineq']=inequal
    return bestStump,minError,bestClasEst#返回该弱分类器，最小误差率，最优分类情况

def adaBoostTrainDS(dataArr,classLabels,numIt=40): #基于弱分类器的Adaboost算法构建最终分类器;numIt确定弱分类器的最大数目
    weakClassArr=[] #保存每个弱分类器
    m,n=shape(dataArr)
    D=mat(ones((m,1))/m) #数据点的权值
    aggClassEst=mat(zeros((m,1)))#sign(aggClassEst)为最终分类器在训练数据集的分类结果
    for i in range(numIt):
        bestStump,error,classEst=buildStump(dataArr,classLabels,D)#根据权值D，构建弱分类器
        print('D:',D.T)
        alpha=float(0.5*log((1.0-error)/max(error,1e-16)))#计算分类器的权值
        print('alpha:',alpha)
        bestStump['alpha']=alpha
        weakClassArr.append(bestStump)
        print('classEst:',classEst)
        expon=multiply(-1*alpha*mat(classLabels).T,classEst)#列向量，-α*y*G(x)
        D=multiply(D,exp(expon)) #列向量, w*exp(-α*y*G(x))
        D=D/D.sum() #更新后的权值D向量
        aggClassEst+=alpha*classEst #累加弱分类器
        print('aggClassEst:',aggClassEst.T)
        aggErrors=multiply(sign(aggClassEst)!=mat(classLabels).T,ones((m,1))) #小技巧！
        errorRate=aggErrors.sum()/m #计算分类错误率
        print('total error:',errorRate)
        if errorRate==0.0:break #如果错误率为0，则退出循环
    return weakClassArr,aggClassEst #返回弱分类器集合

def adaClassify(datToClass,classifierArr):#对datToclass进行分类
    dataMatrix=mat(datToClass) #转化为矩阵类型
    m,n=shape(dataMatrix)
    aggClassEst=mat(zeros((m,1)))#弱分类器的累加情况
    for i in range(len(classifierArr)):
        classEst=stumpClassify(dataMatrix,classifierArr[i]['dim'],classifierArr[i]['thresh'],classifierArr[i]['ineq'])
        aggClassEst+=classEst*classifierArr[i]['alpha']
    return sign(aggClassEst)#分类结果
        

def loadDataSet(filename):#通用的加载数据的方法，特征的个数任意
    numFeat=len(open(filename).readline().split('\t'))
    dataMat=[]
    labelMat=[]
    fr=open(filename)
    for line in fr.readlines():
        lineArr=[]
        curLine=line.strip().split('\t')
        for i in range(numFeat-1):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat,labelMat

def plotROC(predStrengths,classLabels):#绘制ROC曲线
    cur=(0,0)
    ySum=0.0
    numPosClas=sum(array(classLabels)==1.0)
    yStep=1/float(numPosClas)
    xStep=1/float(len(classLabels)-numPosClas)
    sortedIndex=predStrengths.argsort()
    sortedList=sortedIndex.tolist()[0]
    sortedList.reverse()
    fig=plt.figure()
    fig.clf()
    ax=plt.subplot(111)
    for index in sortedList:
        if classLabels[index]==1.0:
            delX=0
            delY=yStep
        else:
            delX=xStep
            delY=0
            ySum+=cur[1]
        ax.plot([cur[0],cur[0]+delX],[cur[1],cur[1]+delY],c='b')
        cur=(cur[0]+delX,cur[1]+delY)
    ax.plot([0,1],[0,1],'b--')
    ax.axis([0,1,0,1])
    plt.show()
    print('the Area Under the Curve is:',ySum*xStep)

    

def test(): 
    D=mat(ones((5,1))/5)
    datMat,classLabels=loadSimpData()
    weakClassArr,aggClassEst=adaBoostTrainDS(datMat,classLabels)
    theclass=adaClassify([[5,5],[0,0],[1,1]],weakClassArr)
    print(theclass)

def test2():
    datArr,labelArr=loadDataSet('horseColicTraining2.txt')
    classifierArray,aggClassEst=adaBoostTrainDS(datArr,labelArr,50)
    testArr,testLabelArr=loadDataSet('horseColicTest2.txt')
    prediction10=adaClassify(testArr,classifierArray)
    errArr=mat(ones((67,1)))
    errSum=errArr[prediction10!=mat(testLabelArr).T].sum()
    print(errSum/67)
def test3():
    datArr,labelArr=loadDataSet('horseColicTraining2.txt')
    classifierArray,aggClassEst=adaBoostTrainDS(datArr,labelArr,10)
    plotROC(aggClassEst.T,labelArr)

if __name__=='__main__':
    test()

#adaboost构建分类决策树和通过C4.5构建决策树的不同处,
#两者都适应二分类的情况
#C4.5的输入数据特征值是离散的，就是1或0；而adaboost算法可以处理特征值是非离散的情况，取值可以是无限种情况
#C4.5每次构建树是选择信息增益最大的特征作为分类，而adaboost构建每个弱分类器是选择分类错误率最小的特征条件作为分类

