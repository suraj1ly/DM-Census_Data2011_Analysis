
# imported the requests library 
import requests 
import os
import zipfile
from bs4 import BeautifulSoup
def insertChar(mystring, position, chartoinsert):
    longi = len(mystring)
    mystring   =  mystring[:position] + chartoinsert + mystring[position:] 
    return mystring 
a=[]
r=requests.get("http://www.censusindia.gov.in/2011census/HLO/HL_PCA/Houselisting-housing-HLPCA.html")
r=requests.get("http://www.censusindia.gov.in/2011census/dchb/DCHB.html")
soup=BeautifulSoup(r.content,features="lxml")
for link in soup.find_all("a"):
    a.append(link.get("href"))
# for i in range(len(a)):
#     print(a[i])
count=0
# i=0
i=0
j=len(a)
while i<j:
    if a[i] is None or a[i]=="None":
        count=count+1
        a.pop(i)
        j=j-1
    i=i+1
i=5
# print()
# print("Hello ")
# print()
b=[]
while i<(len(a)-5):
    b.append("http://www.censusindia.gov.in/2011census/dchb/" + a[i])
    i=i+5
b.append(a[i])
# print(b)
# print(count)
# print(count)
# print(len(b))
# for i in range(len(b)):
#     print(b[i])
# 
i=27
while i<len(b):
    
    a=[]
    c=[]
    g=[]
    l=[]
    j=0
    count=0
    for j in range(len(b[i])):
        if b[i][j]=='/':
            count=count+1
        if count==5:
            g=b[i][j+1:]
            break
    # print(g)
    j=0
    for j in range(len(g)):
        if g[j]=='.':
            l=g[:j]
            break
    os.mkdir(l)
    os.chdir(l)
    print("hello state dir")
    #l is statenamed directory
    r=requests.get(b[i])
    soup=BeautifulSoup(r.content,features="lxml")
    a=[]
    for link in soup.find_all("a"):
        a.append(link.get("href"))
    # print(a)
    j=9
    while j <(len(a)):
        c="http://www.censusindia.gov.in/2011census/dchb/"+ a[j]
        count=0
        m=0
        for m in range(len(c)):
            if c[m]=='/':
                count=count+1
            if count==5:
                h=c[m+1:]
                break
        p=0
        for p in range(len(h)):
            if h[p]=='.':
                q=h[:p]
        
        w=0
        
        while w < len(a[j]):
            if a[j][w]==' ':
                a[j]=insertChar(a[j],w,'%')
                a[j]=insertChar(a[j],w+1,'2')
                a[j]=insertChar(a[j],w+2,'0')
                w=w+3
            w=w+1
        a[j]=a[j].replace(" ","")
                
        v="http://www.censusindia.gov.in/2011census/dchb/"+ a[j]
        r=requests.get(v)
        count=0
     
        m=0
        count=0
        j=j+1

        
        
        with open(h,'wb') as f: 
            f.write(r.content) 
        fantasy_zip = zipfile.ZipFile('C:\\Users\\Dell-pc\\Desktop\\'+l+'\\'+h)
        fantasy_zip.extractall('C:\\Users\\Dell-pc\\Desktop\\'+l)
        for filename in os.listdir(q):
            if not (filename.startswith('T41') or filename.startswith('T40') or filename.startswith('T39') or filename.startswith('T01')
            or filename.startswith('T20') or filename.startswith('T30') or filename.startswith('T36') or filename.startswith('T41')
            or filename.startswith('T44') or filename.startswith('T05') or  filename.startswith('T13') or  filename.startswith('T33') 
            or  filename.startswith('T39') or  filename.startswith('Appendix_I_') or filename.startswith('Town Statement-I_') 
            or filename.startswith('Town Statement-V_') or filename.startswith('Town Statement-III')):
                os.chdir(q)
                os.unlink(filename)
                os.chdir('..')
        fantasy_zip.close()

    i=i+1   
    os.chdir('..')   
        
        
        


    for j in range(len(c)):
        print(c[j])
    



    
#print(soup.prettify)
  
