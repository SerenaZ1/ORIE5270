import sys
from pyspark import SparkConf, SparkContext
import numpy as np
import math


#data_path = "/Users/serena/Desktop/cornell_3rd_semester/courses/ORIE5270/hw/data.txt"
#centroids_path = "/Users/serena/Desktop/cornell_3rd_semester/courses/ORIE5270/hw/c1.txt"

dist = math.inf

conf = SparkConf()
sc = SparkContext(conf=conf)

def closest_centroid(point,centroids):
    min_dis = math.inf
    cluster_id = 0
    for i in range(len(centroids)):
        dis = np.sum((point - centroids[i]) ** 2)
        if dis < min_dis:
            min_dis = dis
            cluster_id = i
    return cluster_id

data = sc.textFile(sys.argv[1]).map(
   lambda line: np.array([float(x) for x in line.split(' ')])).cache()
#data = sc.textFile(data_path).map(
 #  lambda line: np.array([float(x) for x in line.split(' ')])).cache()
# Load the initial centroids
#centroids = sc.textFile(sys.argv[2]).map(
   #lambda line: np.array([float(x) for x in line.split(' ')])).cache()
c = open(sys.argv[2],'r')
#c = open(centroids_path,'r')
centroids = []
for line in c:
    centroids.append(np.array([float(x) for x in line.split(' ')]))

centroids = np.array(centroids)
dim_centroids = np.shape(centroids)[1] * np.shape(centroids)[0]
num = 1

while dist:
    if num > 1000:
        break
    num += 1
    old_centroids = centroids
    closest = data.map(lambda p: (closest_centroid(p,centroids),(1,p)))
    closest = closest.reduceByKey(lambda x,y:(x[0]+y[0],x[1]+y[1]))
    centroids = closest.map(lambda x: (x[0],(x[1][1] / x[1][0]))).sortByKey().map(lambda x:x[1]).collect()
    centroids = np.array(centroids)
    dist = dim_centroids - np.sum(old_centroids == centroids)
print (centroids)

sc.stop()