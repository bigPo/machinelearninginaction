# -*- coding: utf-8 -*-

def loadDataSet():
    dataMat = []; labelMat = []
    #加路径的话要写作:open('D:\\testSet.txt','r') 缺省为只读
    fr = open('testSet.txt') 
    #readlines()函数一次读取整个文件,并自动将文本分拆成一个行的列表, 
    #该列表支持python使用for...in...的结构进行处理 (一次只处理一行)   
    for line in fr.readlines():
        #strip()函数 删除字符串中的首尾空格或制表符等  
        #split()函数 按照符号(制表符)进行分割
        lineArr = line.strip().split()
        #每一行加入第零维 1
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat
    
def sigmoid(inX):
    return 1.0/(1 + exp(-inX))
    
def gradAscent(dataMatIn, classLabels):
    #mat()函数是numpy内置的, 将数组转化为numpy矩阵   
    dataMatrix = mat(dataMatIn)
    labelMat = mat(classLabels).transpose()
    #shape()函数是numpy内置的, 读取矩阵的行和列    
    m,n = shape(dataMatrix)
    alpha = 0.001
    maxCycles = 500
    weights = ones((n,1))
    
    for k in range(maxCyckes):
        h = sigmoid(dataMatrix*weights)
        error = (labelMat - h)  # 梯度上升算法
        weights = weights + alpha * dataMatrix.transpose() * error
    return weights
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    