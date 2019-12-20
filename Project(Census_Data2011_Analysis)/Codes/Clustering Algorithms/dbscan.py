from __future__ import print_function
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

from sklearn.metrics import silhouette_samples, silhouette_score
from xlrd import open_workbook
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import copy

range_n_clusters = [1]

for n_clusters in range_n_clusters:

    wb = open_workbook('FinalDataset3.xls')
    count=0
    counter=0
    for sheet in wb.sheets():
        # print("Print",sheet.cell(0,25))
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
    # print("1",len(dataset))
    # print("2",len(dataset[0]))
    
    X=copy.deepcopy(dataset)
 
    # 6 7 8 9 10 11 12 13
    # for i in range(len(X)):
    #     X[i].pop(5)
    #     X[i].pop(5)
    #     X[i].pop(5)
    #     X[i].pop(5)
    #     X[i].pop(5)
    #     X[i].pop(5)
    #     X[i].pop(5)
    #     X[i].pop(5)

    # print(len(X[0]))

    # print(X)
    clusterer = DBSCAN(eps=80)
    # clusterer = KMeans(n_clusters=n_clusters, random_state=10)
    cluster_labels = clusterer.fit_predict(X)
    print(cluster_labels)
    # print(type(cluster_labels))
    # print(type(X))
    silhouette_avg = silhouette_score(X, cluster_labels)
    print("For n_clusters =", n_clusters,"The average silhouette_score is :", silhouette_avg)
    # print(cluster_labels)
    # d=[0,0,0,0,0]
    # a=[]
    # print(len(dataset))
    # for i in range(len(cluster_labels)):
    #     if cluster_labels[i]==0:
    #         d[0]=d[0]+1
    #     elif cluster_labels[i]==1:
    #         d[1]=d[1]+1
    #     elif cluster_labels[i]==2:
    #         d[2]=d[2]+1
    #     elif cluster_labels[i]==3:
    #         # a.append(i+1)
    #         d[3]=d[3]+1
    #     else:
    #         d[4]=d[4]+1
    # print(d)
    # print(a)
   
