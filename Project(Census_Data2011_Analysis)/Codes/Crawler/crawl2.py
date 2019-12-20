
# imported the requests library 
import requests 
import os
import random
import zipfile
import copy
from bs4 import BeautifulSoup
def insertChar(mystring, position, chartoinsert):
    longi = len(mystring)
    mystring   =  mystring[:position] + chartoinsert + mystring[position:] 
    return mystring 
a=[]
r=requests.get("http://www.censusindia.gov.in/2011census/HLO/HL_PCA/Houselisting-housing-HLPCA.html")
#r=requests.get("http://www.censusindia.gov.in/2011census/dchb/DCHB.html")
soup=BeautifulSoup(r.content,features="lxml")
for link in soup.find_all("a"):
    a.append(link.get("href"))
# for i in range(len(a)):
#     print(a[i])








count=0
# i=0
i=0
j=len(a)
# while i<j:
#     if a[i] is None or a[i]=="None":
#         count=count+1
#         a.pop(i)
#         j=j-1
#     i=i+1
# i=5
# print()
# print("Hello ")
# print()
b=[]
i=0
while i<j:
    b.append("http://www.censusindia.gov.in/2011census/HLO/HL_PCA/" + a[i])
    i=i+1
# b.append(a[i])
# for i in range(len(b)):
#     print(b[i])
print(b[0])
i=0

# print(len(b))
# for i in range(len(b)):
#     print(b[i])



#Use this

# print(b[1])
# r=requests.get(b[1])
# soup=BeautifulSoup(r.content,features="lxml")
# headline = soup.find(attrs={'href' : 'HH_PCA1/HLPCA-06070-2011_H14_census.xlsx'})
# print(headline.string)


#till this


i=0


while i<len(b)-1:
    
    a=[]
    c=[]
    g=[]
    l=[]
    j=0
    count=0
    for j in range(len(b[i])):
        if b[i][j]=='/':
            count=count+1
        if count==6:
            g=copy.deepcopy(b[i][0:j])
            break
    j=0
    print(b[i])
    count=0
    for j in range(len(b[i])):
        if b[i][j]=='-':
            count=count+1
        if count==2:
            q=b[i][j+1:]
            break
    print("Hello",q)
    count=0
    for j in range(len(q)):
        if q[j]=='.':
            l=q[:j]
            break
    print(l) 
    # print(g)
    j=0
    # print(g)
    # i=i+1
    
   
    # print("G",g)
    # i=i+1




    os.mkdir(l)
    os.chdir(l)




    # print("hello state dir")
    #l is statenamed directory
    r=requests.get(b[i])
    soup=BeautifulSoup(r.content,features="lxml")
    a=[]
    for link in soup.find_all("a"):
        a.append(link.get("href"))
    
    print(a)
    print(g)
    # i=i+1
    j=0
    # for j in range(len(a)):
    #     c=g +"/"+ a[j]
    #     count=0
    #     m=0
    #     for m in range(len(c)):
    #         if c[m]=='/':
    #             count=count+1
    #         if count==5:
    #             h=c[m+1:]
    #             break
    #     p=0
    #     for p in range(len(h)):
    #         if h[p]=='.':
    #             q=h[:p]
        
    #     w=0
        
    #     while w < len(a[j]):
    #         if a[j][w]==' ':
    #             a[j]=insertChar(a[j],w,'%')
    #             a[j]=insertChar(a[j],w+1,'2')
    #             a[j]=insertChar(a[j],w+2,'0')
    #             w=w+3
    #         w=w+1
    #     a[j]=a[j].replace(" ","")
    for j in range(len(a)):
    
        r=requests.get(b[i])
        
        soup=BeautifulSoup(r.content,features="lxml")
        headline = soup.find(attrs={'href' : a[j]})
        # print(headline.string)





        r1=requests.get(g+"/"+a[j])
       
        print("Directory",g+"/"+a[j])
        
        print("Applae",a[j])
      
        qw=headline.string
        h=0
        line=[]
        print(qw)
        line=str(qw)
        count=0
        line=""
        for y in range(len(qw)):
            if qw[y].isalpha():
                line=line+qw[y]
        


        
                
        print(len(qw))
        print(line)
        print(len(line))
        os.mkdir(line)
        os.chdir(line)
        
        with open(line+".xlsx",'wb') as f: 
            f.write(r1.content)
        os.chdir('..') 


    # v=g + a[j]
    # r=requests.get(v)
    count=0
    
    m=0
    

        
        
        # with open(h,'wb') as f: 
        #     f.write(r.content) 
        # fantasy_zip = zipfile.ZipFile('C:\\Users\\Dell-pc\\Desktop\\'+l+'\\'+h)
        # fantasy_zip.extractall('C:\\Users\\Dell-pc\\Desktop\\'+l)
        # for filename in os.listdir(q):
        #     if not (filename.startswith('T41') or filename.startswith('T40') or filename.startswith('T39') or filename.startswith('T01')
        #     or filename.startswith('T20') or filename.startswith('T30') or filename.startswith('T36') or filename.startswith('T41')
        #     or filename.startswith('T44') or filename.startswith('T05') or  filename.startswith('T13') or  filename.startswith('T33') 
        #     or  filename.startswith('T39') or  filename.startswith('Appendix_I_') or filename.startswith('Town Statement-I_') 
        #     or filename.startswith('Town Statement-V_') or filename.startswith('Town Statement-III')):
        #         os.chdir(q)
        #         os.unlink(filename)
        #         os.chdir('..')
        # fantasy_zip.close()

    i=i+1   
    os.chdir('..')   
        
        
        


    # for j in range(len(c)):
    #     print(c[j])
    



    
#print(soup.prettify)
  
