import copy
import random
from random import shuffle
import math
import csv
import numpy as np
from xlrd import open_workbook
from sklearn.metrics import silhouette_samples, silhouette_score


class genrep:

    def __init__(self, k, dataset1, n, m, choice, choice1):
        self.k = k
        self.choice = choice
        self.dataset1 = dataset1
        self.n = n
        self.m = m
        self.choice1 = choice1

    def euclideandist(self, n, x, y):
        sum = 0
        for i in range(n):
            # print("Eror",x[i],y[i])
            sum = sum+((x[i]-y[i])*(x[i]-y[i]))
        return math.sqrt(sum)

    def manhattamdist(self, n, x, y):
        sum = 0
        for i in range(n):
            sum = sum+abs(x[i]-y[i])
        return sum

    def repmean(self, clusters, k, n):
        rep1 = []
        for i in range(k):
            rep1.append([])

        for i in range(k):

            for j in range(n):
                sum = 0
                for k in range(len(clusters[i])):
                    sum = sum+clusters[i][k][j]

                f = sum/len(clusters[i])
                rep1[i].append(f)
        # print("REP : ", rep1)
        return rep1

    def check(self, data1, data2):
        l1 = len(data1)
        counter1 = 0
        for i in range(l1):
            if data1[i] in data2:
                counter1 = counter1+1
        if counter1 == l1:
            return True
        else:
            return False

    def repmedian(self, clusters, k, n):
        rep1 = []
        for i in range(k):
            rep1.append([])

        for i in range(k):

            for j in range(n):
                sd = []
                f = 0
                for k in range(len(clusters[i])):
                    sd.append(clusters[i][k][j])
                sd.sort()

                len2 = len(clusters[i])

                len2 = (int)(len2/2)
                len4 = len2-1

                if len(clusters[i]) % 2 == 0:
                    f = (sd[len2]+sd[len4])/2
                else:
                    f = sd[len2]
                rep1[i].append(f)
        # print("REP : ", rep1)
        return rep1

    def clustering(self):

        rep = []
        clusters = []
        value = []
        set1 = copy.deepcopy(dataset1)
        if choice1 == 1:
            for i in range(k):
                c = int(
                    input("Enter the datapoint index(1-k). Donot take same representative : "))
                rep.append(set1[c-1])
            # print(rep)
        if choice1 == 2:
            shuffle(set1)
            for i in range(k):
                rep.append(set1[i])
            # print(rep)
        rep2 = copy.deepcopy(rep)
        rep3 = []
        counter = 0
        if self.choice == 1:
            while counter != 1000:
                if counter != 0:
                    if self.check(rep2, rep3):
                        class_label=[]
                        for i in range(len(dataset1)):
                            class_label.append(-1)
                        print(class_label)
                        for i in range(len(dataset1)):
                            for j in range(len(clusters)):
                                if dataset1[i] in clusters[j]:
                                    class_label[i]=j
                                    break
                        print(class_label)
                        class1=np.array(class_label)
                        
                        print(type(class1))

                        
                        silhouette_avg = silhouette_score(dataset1, class1)
                        print("For n_clusters =",len(clusters),"The average silhouette_score is :", silhouette_avg)
                        # silhouttee(clusters)
                        break
                del clusters
                clusters = []
                for i in range(k):
                    clusters.append([])

                for i in range(m):
                    value = []
                    for j in range(k):
                        d = self.euclideandist(n, dataset1[i], rep2[j])
                        value.append(d)
                    l = value.index(min(value))

                    clusters[l].append(dataset1[i])
                # print(clusters)
                rep3 = copy.deepcopy(rep2)
                del rep2
                rep2 = []
                rep2 = self.repmean(clusters, k, n)
                counter = counter+1
        if self.choice == 2:

            while counter != 1000:
                if counter != 0:
                    if self.check(rep2, rep3):
                        # print("Real Clusters : ",clusters)
                        # print("Hello")
                        # hta dena
                        class_label=[]
                        for i in range(len(dataset1)):
                            class_label.append(-1)
                        print(class_label)
                        for i in range(len(dataset1)):
                            for j in range(len(clusters)):
                                if dataset1[i] in clusters[j]:
                                    class_label[i]=j
                                    break
                        print(class_label)
                        class1=np.array(class_label)
                        
                        print(type(class1))

                        
                        silhouette_avg = silhouette_score(dataset1, class1)
                        print("For n_clusters =",len(clusters),"The average silhouette_score is :", silhouette_avg) 
                        break
                del clusters
                clusters = []
                for i in range(k):
                    clusters.append([])

                for i in range(m):
                    value = []
                    for j in range(k):
                        d = self.manhattamdist(n, dataset1[i], rep2[j])
                        value.append(d)
                    l = value.index(min(value))

                    clusters[l].append(dataset1[i])
                # print(clusters)
                rep3 = copy.deepcopy(rep2)
                del rep2
                rep2 = []
                rep2 = self.repmedian(clusters, k, n)
                counter = counter+1


def nothing():
    print("Error in choosing choice ")


if __name__ == "__main__":
    # Assumptions that file contains all the faetures at all data points
    # f = open('FinalDataset.xls')
    
    wb = open_workbook('FinalDataset3.xls')
  
    count=0
    counter=0
    for sheet in wb.sheets():
        count=count+1
        if count==2:
            break
        number_of_rows = sheet.nrows
        number_of_columns = sheet.ncols
        
        
        items = []

        rows = []
        dataset = []
        for i in range(number_of_rows-1):
            dataset.append([])

        for row in range(1, number_of_rows):

            
            for col in range(5,number_of_columns):
                value  = (sheet.cell(row,col).value)
                counter=counter+1
                try:
                    value = float(value)
                except ValueError:
                    pass
                finally:
                    if col not in[25]:
                        dataset[row-1].append(value)
    # print(dataset)  
    print("Number of datapoints ",counter)
    print(number_of_columns)
    print(number_of_rows)
    # with open('ex4.txt') as csv_file:
    #     csv_reader = csv.reader(csv_file, delimiter=',')
    #     dataset = []
    #     for row in csv_reader:

            
    #         dataset.append(row)
    #     print(dataset)
    dataset1 = copy.deepcopy(dataset)


    # print(dataset1)
    m = len(dataset1)
    n = len(dataset1[0])

    k = int(input("Enter the number of Clusters want : "))

    print("Enter the Choice ")
    print("1. K - means Clustering")
    print("2. K - median Clustering")

    choice = int(input())
    if choice == 1:
        print("1. Do You want to take representative by your own ")
        print("2. Do Random select reprentative ")
        choice1 = int(input())

        p1 = genrep(k, dataset1, n, m, choice, choice1)
        p1.clustering()
    elif choice == 2:
        print("1. Do You want to take representative by your own ")
        print("2. Do Random select reprentative ")
        choice1 = int(input())
        p2 = genrep(k, dataset1, n, m, choice, choice1)
        p2.clustering()
    else:
        nothing()

