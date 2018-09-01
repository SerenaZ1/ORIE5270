from pyspark import SparkContext
import numpy as np
sc = SparkContext.getOrCreate()
#base_path = '/Users/serena/Desktop/cornell_3rd_semester/courses/ORIE5270/hw/'
base_path = ''
A = sc.textFile(base_path+'A').map(lambda l: [float(x) for x in l.split(',')]).cache()
v = sc.textFile(base_path+'B').map(lambda l: [float(x) for x in l.split(',')]).cache()

#AwithIdx = A.zipWithIndex()
AwithIdx = A.map(lambda x:(x[1:],x[0]))
mat_A = AwithIdx.map(lambda x:(x[1],x[0]))\
		.flatMap(lambda x: [(i, (x[0], x[1][i])) for i in range(len(x[1]))])

#vwithIdx = v.zipWithIndex()
vwithIdx = v.map(lambda x:(x[1:],x[0]))
v =  vwithIdx.map(lambda x:(x[1],x[0]))\
		.flatMap(lambda x: [(i, x[1][i]) for i in range(len(x[1]))])
res = mat_A.join(v).map(lambda x: (x[1][0][0],x[1][0][1] * x[1][1]))
res = res.reduceByKey(lambda x,y: x+y)

print(res.collect())
