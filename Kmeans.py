import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'x' : [13,22,30,20,31,35,25,47,46,54,53,56,58,55,58,63,67,73,76],
    'y' : [41,38,32,54,58,49,59,62,65,73,70,65,61,27,17,9,21,9,27]
})

np.random.seed(200)
k=3
#centroids[i] = [x,y]
centroids = {
    i+1: [np.random.randint(0, 80), np.random.randint(0, 80)]
    for i in range(k)
}

fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x'],df['y'],color='k')
colmap = {1: 'r', 2: 'g', 3: 'b'}
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 80)
plt.ylim(0, 80)
plt.show()