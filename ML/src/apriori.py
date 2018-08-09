##Apriori算法 关联分析

def loadDataSet():
    return [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]

def createC1(dataSet):#创建大小为一的所有候选项集的集合
    C1=[]
    for transaction in dataSet:#遍历每个交易记录
        for item in transaction:#遍历每个物品项
            if [item] not in C1:#要处理成[],因为python不能创建只有一个整数的集合，而[一个数] 就可以
                C1.append([item])
    C1.sort()
    return list(map(frozenset,C1))#把C1的每个[item]转化为不可变的set集合,并返回C1

def scanD(D,Ck,minSupport):#由Ck生成Lk，Lk是满足支持度最低要求的候选项集的集合
    ssCnt={}#保存每一个项集出现的次数
    for tid in D:#遍历每个交易记录
        for can in Ck:#遍历每个项集
            if can.issubset(tid):#如果该项集出现在该交易记录中
                if not can in ssCnt:#次数加一
                    ssCnt[can]=1
                else:
                    ssCnt[can]+=1
    numItems=float(len(D))#交易记录的个数
    retList=[]#最后返回的满足要求的候选项集的集合Lk
    supportData={}#统计每个项集的支持度
    for key in ssCnt:
        support=ssCnt[key]/numItems#计算每个项集的支持度
        if support>=minSupport:#满足指定要求则插入到retList
            retList.insert(0,key)
        supportData[key]=support#保存每个项集的支持度
    return retList,supportData

def aprioriGen(Lk,k):#Lk的每个项集含有k-1的元素。由Lk生成Ck+1,把Lk中的项集两两合并，生成每个项集含有k个元素。
    retList=[]
    lenLk=len(Lk)#Lk的项集数
    if lenLk<=1:return []#如果Lk的项集数是1，那么它就是最后最大的项集集合，返回[]，终止外层调用循环。
    for i in range(lenLk): #遍历每个项集
        for j in range(i+1,lenLk): #遍历每个项集
            L1=list(Lk[i])[:k-2] #项集的前部分
            L2=list(Lk[j])[:k-2] #项集的前部分
            L1.sort()
            L2.sort()
            if L1==L2: #如果相等，则把这两个合并，然后追加到返回的Ck+1集合中
                retList.append(Lk[i]|Lk[j]) #这用到了一个小的优化算法，避免了对项集集合两两合并，只选择前面相等进行合并。
    print(retList)
    return retList

def apriori(dataSet,minSupport=0.5):#Apriori算法。参数：数据集，最小支持度
    C1=createC1(dataSet) #创建项集集合C1，每个项集元素数是1
    D=list(map(set,dataSet)) #交易记录的集合
    L1,supportData=scanD(D,C1,minSupport) #由C1生成满足最小支持度的L1,统计支持度的字典
    L=[L1] #Lk的列表 
    k=2    #设置k=2,接下来要求的每个项集含有的元素数是2
    while(len(L[k-2])>0):
        Ck=aprioriGen(L[k-2],k) #生成Ck
        #print(Ck)
        Lk,supK=scanD(D,Ck,minSupport) #生成Lk
        supportData.update(supK) #更新字典
        L.append(Lk) #把本次求出的Lk保存到列表L中
        k+=1 #k加一
    return L,supportData#返回的是每次求出的Lk的列表，和最终的支持度统计字典

######################################################################################
###关联规则生成函数    概念的解释：Lk是项集的列表;Lk的每一项是频繁项集;L是Lk的列表。
    
def generateRules(L,supportData,minConf=0.7):#主函数。参数是上面生成的L和supportData,最小可信度
    bigRuleList=[] #保存关联规则
    for i in range(1,len(L)): #遍历每个Lk，从1开始是因为L0的每个项集只包含单个元素，单个元素无法生成规则
        for freqSet in L[i]: #遍历每个项集
            H1=[frozenset([item]) for item in freqSet ] #项集的单个元素组成的列表
            if (i>1):#如果i>1,则每个项集的元素数>=3
                calcConf(freqSet,H1,supportData,bigRuleList,minConf)#这一行是我自己加的。先使H1作为右部计算可信度，此时的H1是单个元素的列表。
                rulesFromConseq(freqSet,H1,supportData,bigRuleList,minConf)#再调用函数，先对H1调用aprioriGen()，对H1的每项进行两两合并，
            else:#如果i=1,则每个项集的元素数是2。直接调用函数，计算可信度。        #使H1每项长度增1，再调用calcConf(freqSet,H1)这样就使H1的每项作为规则右部再计算可信度
                calcConf(freqSet,H1,supportData,bigRuleList,minConf)
    return bigRuleList

def calcConf(freqSet,H,supportData,br1,minConf=0.7):#计算可信度并找到满足最小可信度的关联规则。参数：项集，H的每一项作为关联规则右部，支持度字典，br1代表bigRuleList
    prunedH=[]
    for conseq in H:#遍历H中的每一项，作为关联规则右部
        conf=supportData[freqSet]/supportData[freqSet-conseq]#计算可信度
        if conf>=minConf:#如果当前规则满足可信度
            print(freqSet-conseq,'-->',conseq,'conf:',conf)#输出该关联规则
            br1.append((freqSet-conseq,conseq,conf))#保存该关联规则
            prunedH.append(conseq)
    return prunedH

def rulesFromConseq(freqSet,H,supportData,br1,minConf=0.7):#参数：项集，规则右部列表，....
    m=len(H[0]) #每一项的长度
    if (len(freqSet)>(m+1)):#m+1是H合并后每项的长度，如果项集的长度大于m+1,则可以对H进行合并，然后做为右部，再计算可信度
        Hmp1=aprioriGen(H,m+1)#对H进行两两合并，每项长度增一
        Hmp1=calcConf(freqSet,Hmp1,supportData,br1,minConf)#Hmp1的每项作为右部，计算可信度
        if (len(Hmp1)>1):#如果Hmp1长度大于1，说明还可以继续对Hmp1进行合并，那么就递归进行
            rulesFromConseq(freqSet,Hmp1,supportData,br1,minConf)


#######################################################################################

def test1():
    dataSet=loadDataSet()
    C1=createC1(dataSet)
    D=list(map(set,dataSet))
    L1,supportData1=scanD(D,C1,0.5)
    print(L1)
    print(supportData1)

def test2():#生成L和支持度字典
    dataSet=loadDataSet()
    L,supportData=apriori(dataSet,0.2)
    #print(L)
def test3():#生成关联规则
    dataSet=loadDataSet()
    L,supportData=apriori(dataSet,0.2)
    rules=generateRules(L,supportData,minConf=0.5)
    print(rules)


if __name__=='__main__':
    test2()

    



            
