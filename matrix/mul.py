from pyspark import SparkContext
import numpy as np
sc = SparkContext.getOrCreate()
base_path = '/Users/serena/Desktop/cornell_3rd_semester/courses/ORIE5270/hw/'
A = sc.textFile(base_path+'A').map(lambda l: [float(x) for x in l.split(' ')]).cache()
B = sc.textFile(base_path+'B').map(lambda l: [float(x) for x in l.split(' ')]).cache()
BwithIdx = B.zipWithIndex()
TransposeB = BwithIdx.map(lambda x: (x[1],x[0])) \
    .flatMap(lambda x: [ (i, (x[0], x[1][i])) for i in range(len(x[1]))]) \
    .groupByKey().mapValues(lambda iter: sorted(iter)).sortByKey() \
    .map(lambda x: [v[1] for v in x[1]])
AwithIdx = A.zipWithIndex()
broadcastB = sc.broadcast(TransposeB.collect())

def multiply(vec, b_mat):
    return [np.sum(np.array(v) * np.array(vec)) for v in b_mat.value]

res = A.map(lambda x: multiply(x, broadcastB)).collect()

print(res)