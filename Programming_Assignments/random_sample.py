#Suraj Pandey
#MT18025
stream=[]
sample=[]
import copy
import random
#2 a)

def getNextStream(n):
    s=[]
    f=[]
    for i in range(1,n+1):
        s.append("A"+str(i))
    k=n+1
    for i in range(1,k):
        h=random.randint(1,k-1)
        f.append(s[h-1])
        s.pop(h-1)
        k=k-1
    return f
#2 b)
def updateSample(str,c):
    global s,sample
    if c<=s:
        sample.append(str)
    else:
        
        if s/c > 0.5:
            r=random.randint(0,s-1)
            sample.pop(r)
            sample.append(str)

def mainmethod():
    global n,stream
    for i in range(1,(n+1)):
        updateSample(stream[i-1],i)
    

if __name__ == "__main__":
    global s
    s=int(input("Enter the Sample Size "))
    n=int(input("Enter n"))
    count=[]
    for i in range(n):
        count.append(int(0))
    stream=getNextStream(n)
    
#   For 100 times
    for i in range(100):
        mainmethod()
        for j in range(len(stream)):
            if stream[j] in sample:
                count[j]=count[j]+1
        sample=[]
    print("For 100 times : ")
    print(count)
    count=[]
    for i in range(n):
        count.append(int(0))
    for i in range(500):
        mainmethod()
        for j in range(len(stream)):
            if stream[j] in sample:
                count[j]=count[j]+1
        sample=[]
    print("For 500 times : ")
    print(count)
    count=[]
    for i in range(n):
        count.append(int(0))
    for i in range(1000):
        mainmethod()
        for j in range(len(stream)):
            if stream[j] in sample:
                count[j]=count[j]+1
        sample=[]
    print("For 1000 times : ")
    print(count)
    count=[]
    for i in range(n):
        count.append(int(0))
    for i in range(10000):
        mainmethod()
        for j in range(len(stream)):
            if stream[j] in sample:
                count[j]=count[j]+1
        sample=[]
    print("For 10000 times : ")
    print(count)
    print(stream)
    


s=0
n=0