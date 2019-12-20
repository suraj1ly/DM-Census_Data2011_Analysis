import random
import math
import copy

def trainNB(data,classlabel):
    count=0
    check=['R','D']
    # for i in range(len(classlabel)):
    #     if classlabel[i] in check:
    #         pass
    #     else:
    #         check.append(classlabel[i])
    count=len(check)
    # print(count)
    prob_distribution=[]
    # print(check)
    for i in range(count):
        prob_distribution.append([])
    # print(prob_distribution)
    # print(len(data[0]))
    # print(len(data))
    for i in range(len(data[0])):
        for j in range(len(check)):
            a=[]
            for k in range(len(data)):
                if classlabel[k]==check[j]:
                    a.append(data[k][i])
            mean=sum(a)/len(a)
            s=0
            for k in range(len(a)):
                s=s+(a[k]-mean)**2
            std_dev=math.sqrt(s/len(a))
            if std_dev==0:
                std_dev=1
            prob_distribution[j].append((mean,std_dev))
    
    # print(prob_distribution)
    # print(len(prob_distribution))
    # print(len(prob_distribution[0])) 

    return prob_distribution

def pdf(data,mean,std):
    
    s=((data-mean)**2)/(2*(std**2))
    s1=math.exp((-1)*s)

    s2=std*(math.sqrt(2*math.pi))
    s3=s1/s2
    return s3

def classifyNB(trained,datapoint,prob_value):
    
    
    p=[1,1]  
    # print(prob_value)
    # print(trained[0][0][0]," ",trained[0][0][1])

    for j in range(len(prob_value)):
        
        for i in range(len(datapoint)):

            p[j]=p[j]*pdf(datapoint[i],trained[j][i][0],trained[j][i][1])
        p[j]=p[j]*prob_value[j]
    # print(p)
    if p[0]>p[1]:
        return 0
    else:
        return 1

if __name__ == "__main__":
    # Assumptions that file contains all the faetures at all data points
    f = open('train.txt')
    dataset = []
    for line in f:

        line = line.rstrip()
        line = line.lstrip()
        d = line.split(',')
        if d=='R' or d=='D':
            pass
        else:
            dataset.append(d)
        

    # print(dataset)
    # print("Length = ",len(dataset[0]))
    dataset1 = []
    classlabel=[]
    for i in range(0, len(dataset)):
        dataset1.append([])
        for j in range(0, (len(dataset[i])-1)):
            b = float(dataset[i][j])
            dataset1[i].append(b)
        classlabel.append(dataset[i][50])
    # print(dataset1)
    # print(classlabel)
    prob_class=[0,0]
    for i in range(len(classlabel)):
        if classlabel[i]=='R':
            prob_class[0]=prob_class[0]+1
        if classlabel[i]=='D':
            prob_class[1]=prob_class[1]+1
    prob_class_value=[]
    prob_class_value.append(prob_class[0]/sum(prob_class))

    prob_class_value.append(prob_class[1]/sum(prob_class))
    # print(prob_class_value)
    
    flag=-1
    learner_distribution=[]
    # print("Data 1: ",dataset1[0])
    learner_distribution=trainNB(copy.deepcopy(dataset1),copy.deepcopy(classlabel))
    datapoint=dataset1[220]
    # print("Real : ",classlabel[220])
    # print(learner_distribution)
    flag=classifyNB(copy.deepcopy(learner_distribution),datapoint,copy.deepcopy(prob_class_value))
    # print(pdf(1,1,1))



    #For checking the flag
    # if flag==0:
    #     print('R')
    # elif flag==1:
    #     print('D')
    block=len(dataset1)
    fold_number=int(block/10)
    # print(fold_number)
    accuracy=0
    main_accuracy=0
    count=0
    ac1=[0]
    for i in range(10):
        count=count+1
        dataset2=[]
        classlabel2=[]
        
        learner_distribution1=[]
        initial=i*fold_number
        final=initial+9*fold_number
        final1=final%block
        if final1<final:
            
            dataset2=copy.deepcopy(dataset1[initial:(block-1)])
            classlabel2=copy.deepcopy(classlabel[initial:(block-1)])
            for j in range(final1+1):
                dataset2.append(dataset1[j])
                classlabel2.append(classlabel[j])
            final=final1
        else:
            dataset2=copy.deepcopy(dataset1[initial:final])
            classlabel2=copy.deepcopy(classlabel[initial:final])
        # print("Size: ",len(dataset2))  
        # print("Initial ",initial," ","Final : ",final)
        learner_distribution1=trainNB(copy.deepcopy(dataset2),copy.deepcopy(classlabel2))
        # print(i," ",len(learner_distribution1[0]))
        if final<initial:

            j=final
            acc=0
            while j<initial:
                if classlabel[j]=='R':
                    d=0
                else:
                    d=1
                if classifyNB(copy.deepcopy(learner_distribution1),dataset1[j],copy.deepcopy(prob_class_value)) ==d:
                    acc=acc+1
                    # print("Hello")
                j=j+1
            accuracy=accuracy+(acc/fold_number)
        else:
            j=final
            acc=0
            while j<(block-1):
                if classlabel[j]=='R':
                    d=0
                else:
                    d=1
                if classifyNB(copy.deepcopy(learner_distribution1),dataset1[j],copy.deepcopy(prob_class_value)) ==d:
                    acc=acc+1
                    # print("Hello")
                j=j+1
            accuracy=accuracy+(acc/fold_number)
        
        
        print("Accuracy in ",i+1,"Fold :  ",(accuracy-ac1[len(ac1)-1])*100,"%")
        ac1.append(accuracy)


    main_accuracy=accuracy/10
    print()
    print("Average Accuracy : ",main_accuracy*100,"%")


    #To make a file Label.txt
    f = open('test.txt')
    dataset_test = []
    for line in f:

        line = line.rstrip()
        line = line.lstrip()
        d = line.split(',')
        
        dataset_test.append(d)
        

    # print(dataset)
    # print("Length = ",len(dataset[0]))
    dataset1_test = []

    for i in range(0, len(dataset_test)):
        dataset1_test.append([])
        for j in range(0, len(dataset_test[i])):
            b = float(dataset_test[i][j])
            dataset1_test[i].append(b)
    # print(dataset1_test)
    f = open('Label.txt','w+')
    for i in range(len(dataset1_test)):
       
        flag=classifyNB(copy.deepcopy(learner_distribution),copy.deepcopy(dataset1_test[i]),copy.deepcopy(prob_class_value))

        if flag==0:
            f.write("R\n")
        if flag==1:
            f.write("D\n")
    


    


    
    