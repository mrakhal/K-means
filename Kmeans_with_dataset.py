from sklearn.cluster import KMeans
import pandas as pd
from matplotlib import pyplot as plt


df = pd.read_csv("macampendapatan.csv")
df.head()

plt.scatter(df.Umur,df['Pendapatan'])
plt.xlabel('Umur')
plt.ylabel('Pendapatan')

km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(df[['Umur','Pendapatan']])
y_predicted
df['cluster']=y_predicted
df.head()
km.cluster_centers_

df1 = df[df.cluster==0]
df2 = df[df.cluster==1]
df3 = df[df.cluster==2]
plt.scatter(df1.Umur,df1['Pendapatan'],color='red')
plt.scatter(df2.Umur,df2['Pendapatan'],color='green')
plt.scatter(df3.Umur,df3['Pendapatan'],color='blue')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='black',marker='*',label='centroid')
plt.xlabel('umur')
plt.ylabel('Pendapatan')
plt.legend()
plt.show()