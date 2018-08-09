#FP-growth算法

class treeNode:#FP树的类定义
    def __init__(self,nameValue,numOccur,parentNode):
        self.name=nameValue
        self.count=numOccur
        self.nodeLink=None
        self.parent=parentNode
        self.children={}

    def inc(self,numOccur):
        self.count+=numOccur

    def disp(self,ind=1):
        print(' '*ind,self.name,' ',self.count)
        for child in self.children.values():
            child.disp(ind+1)
#########################################################
###FP树构建函数

def createTree(dataSet,minSup=1):#FP树的构建函数
    headerTable={}#头指针表
    for trans in dataSet: #遍历数据集，dataSet是一个字典
        for item in trans:#遍历每个记录
            headerTable[item]=headerTable.get(item,0)+dataSet[trans]
    for k in list(headerTable.keys()):#处理头指针表
        if headerTable[k]<minSup:#把满足支持度的每一项筛选出来
            del(headerTable[k])
    freqItemSet=set(headerTable.keys())#元素的集合
    if len(freqItemSet)==0:return None,None #如果没有，则返回None
    for k in headerTable: #头指针表字典的值，一个是本身元素，一个指针
        headerTable[k]=[headerTable[k],None]
    #print(headerTable)
    retTree=treeNode('Null Set',1,None)#生成根节点
    for tranSet,count in dataSet.items():#遍历数据字典，tranSet是一个数据记录，count其出现的次数
        localD={} #保存本条记录的每一个元素
        for item in tranSet:#记录的每个元素
            if item in freqItemSet:
                localD[item]=headerTable[item][0]#出现次数      
        if len(localD)>0:
            orderedItems=[v[0] for v in sorted(localD.items(),key=lambda p:p[1],reverse=True)]#对本条记录的元素进行排序
            updateTree(orderedItems,retTree,headerTable,count)#调用函数，把本条记录插入到树中
    return retTree,headerTable

def updateTree(items,inTree,headerTable,count):#参数:items一条记录，inTree父结点,headerTable头指针表，count出现次数
    #本程序先插入记录的第一个元素结点，再递归地插入其他的元素结点
    if items[0] in inTree.children: #如果首结点是父结点的孩子，则直接进行计数增加即可
        inTree.children[items[0]].inc(count)
    else: #不是孩子结点
        inTree.children[items[0]]=treeNode(items[0],count,inTree)#生成孩子结点
        #把该生成的结点插入到头指针表
        if headerTable[items[0]][1]==None:#如果头指针表没有结点
            headerTable[items[0]][1]=inTree.children[items[0]]#直接插入
        else:#否则就调用函数，找到尾部，再插入
            updateHeader(headerTable[items[0]][1],inTree.children[items[0]])
    if len(items)>1:#递归调用，插入本条记录的剩余元素结点
        updateTree(items[1:],inTree.children[items[0]],headerTable,count)

def updateHeader(nodeToTest,targetNode):#更新头指针表函数，找到尾部，再插入
    while(nodeToTest.nodeLink!=None):
        nodeToTest=nodeToTest.nodeLink
    nodeToTest.nodeLink=targetNode

###############################################################
def loadSimpDat():#生成数据集
    simpDat=[['r','z','h','j','p'],
             ['z','y','x','w','v','u','t','s'],
             ['z'],
             ['r','x','n','o','s'],
             ['y','r','x','z','q','t','p'],
             ['y','z','x','e','q','s','t','m']]
    return simpDat

def createInitSet(dataSet):#把数据集转化为字典的形式
    retDict={}
    for trans in dataSet:
        retDict[frozenset(trans)]=1
    return retDict

################################################################
################################################################
###从一颗FP树中挖掘频繁项集

#############发现以给定元素项结尾的所有路径的函数
def ascendTree(leafNode,prefixPath):#找到leafNode结点的前缀,并保存在prefixPat中
    if leafNode.parent!=None:
        prefixPath.append(leafNode.name)
        ascendTree(leafNode.parent,prefixPath)

def findPrefixPath(basePat,treeNode):#参数:basePat指定元素，treeNode头指针表的结点
    condPats={}
    while treeNode!=None:
        prefixPath=[]
        ascendTree(treeNode,prefixPath)#调用函数查找
        if len(prefixPath)>1:
            condPats[frozenset(prefixPath[1:])]=treeNode.count #前缀的次数等于本结点的次数
        treeNode=treeNode.nodeLink #移动头指针表的结点
    return condPats #指定元素的前缀的集合字典
############################################
########递归查找频繁项集的函数（难）
def mineTree(inTree,headerTable,minSup,preFix,freqItemList):#参数:inTree树，headerTable头指针表，preFix前缀，freqItemList保存频繁项集
    bigL=[v[0] for v in sorted(headerTable.items(),key=lambda p:p[1][0],reverse=False)] #元素集合
    for basePat in bigL: #遍历所有元素
        newFreqSet=preFix.copy() #前缀集合
        newFreqSet.add(basePat)  #增加当前元素
        freqItemList.append(newFreqSet) 
        condPattBases=findPrefixPath(basePat,headerTable[basePat][1])#查找前缀
        myCondTree,myHead=createTree(condPattBases,minSup) #构建条件树(前缀的树)
        if myHead!=None:#如果存在
            print('conditional tree for: ',newFreqSet)
            mineTree(myCondTree,myHead,minSup,newFreqSet,freqItemList)#递归调用
        

############################################
################################################################
################################################################

            


def test1():
    rootNode=treeNode('pyramid',9,None)
    rootNode.children['eye']=treeNode('eye',13,None)
    rootNode.children['phoenix']=treeNode('phoenix',3,None)
    rootNode.disp()

def test2():#构造FP树
    simpDat=loadSimpDat()
    initSet=createInitSet(simpDat)
    print(simpDat)
    myFPtree,myHeaderTable=createTree(initSet,3)
    myFPtree.disp()
def test3():#查找前缀
    simpDat=loadSimpDat()
    initSet=createInitSet(simpDat)
    myFPtree,myHeaderTable=createTree(initSet,3)
    condPats=findPrefixPath('r',myHeaderTable['r'][1])
    print(condPats)
def test4():#根据FP树，挖掘频繁项集
    simpDat=loadSimpDat()
    initSet=createInitSet(simpDat)
    myFPtree,myHeaderTable=createTree(initSet,3)
    freqItems=[]
    mineTree(myFPtree,myHeaderTable,3,set([]),freqItems)
    print(freqItems)
def test5():
    parsedDat=[line.split() for line in open('kosarak.dat').readlines()]
    initSet=createInitSet(parsedDat)
    myFPtree,myHeaderTable=createTree(initSet,10000)
    myFreqList=[]
    mineTree(myFPtree,myHeaderTable,10000,set([]),myFreqList)
    print(myFreqList)
    print(len(myFreqList))
    
    

if __name__=='__main__':
    test5()
