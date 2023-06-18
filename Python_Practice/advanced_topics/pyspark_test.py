import pyspark

from pyspark import SparkContext

arr = sc.parallelize([1,2,3,4,5,6,7,8]);

arr.take(6);