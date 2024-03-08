import numpy as nm    
import matplotlib.pyplot as mtp    
import pandas as pd

dataset = pd.read_csv('Mall_Cust1.csv')
x = dataset.iloc[:, [2, 4]].values

 
from sklearn.cluster import KMeans  
wcss_list= []  

kmeans = KMeans(n_clusters=3, init='k-means++', random_state= 42)  
y_predict= kmeans.fit_predict(x)

mtp.scatter(x[y_predict == 0, 0], x[y_predict == 0, 1], s = 100, c = 'blue', label = 'Cluster 1')  
mtp.scatter(x[y_predict == 1, 0], x[y_predict == 1, 1], s = 100, c = 'green', label = 'Cluster 2')   
mtp.scatter(x[y_predict== 2, 0], x[y_predict == 2, 1], s = 100, c = 'red', label = 'Cluster 3')  

mtp.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroid')   
mtp.title('Clusters of customers')  
mtp.xlabel('Age ')  
mtp.ylabel('Spending Score (1-100)')  
mtp.legend()  
mtp.show() 
