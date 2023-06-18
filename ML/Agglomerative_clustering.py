from pyspark.shell import spark
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import Normalizer
from pyspark.ml.linalg import DenseVector
from pyspark.ml.feature import SQLTransformer
import pyspark.sql.functions as F
from pyspark.ml.clustering import AgglomerativeClustering
from pyspark.ml.linalg import DenseVector, Vectors
from pyspark.sql import SparkSession

file = 'data/insurance.csv'
data = spark.read.csv(file, inferSchema=True, header=True)

assembler = VectorAssembler(inputCols=data.columns, outputCol='features')
assembledData = assembler.transform(data).select('features')

# Assembled features
normalizer = Normalizer(inputCol="features", outputCol="normalized_features")
normalizedData = normalizer.transform(assembledData)

# Calculate Euclidean distance
sql_transformer = SQLTransformer(statement="SELECT a.id AS pointA, b.id AS pointB, SQRT(POW(a.normalized_features[0] - b.normalized_features[0], 2) + POW(a.normalized_features[1] - b.normalized_features[1], 2) + ...) AS dissimilarity FROM __THIS__ a CROSS JOIN __THIS__ b WHERE a.id <> b.id")
dissimilarity_matrix = sql_transformer.transform(normalizedData).select("pointA", "pointB", "dissimilarity")

dissimilarity_matrix = dissimilarity_matrix.pivot("pointA", "pointB").agg(F.first("dissimilarity")).orderBy("pointA")

# Assuming you have a dissimilarity matrix as a DataFrame called 'dissimilarityMatrix'
# The dissimilarity matrix should have 'pointA', 'pointB', and 'dissimilarity' columns
# representing the pairwise dissimilarities between data points

# Convert the dissimilarity matrix to a vector column
dissimilarityMatrix = dissimilarity_matrix.withColumn("dissimilarity_vector", Vectors.dense(dissimilarity_matrix["dissimilarity"]))

# Create an instance of AgglomerativeClustering
agglomerative = AgglomerativeClustering().setFeaturesCol("dissimilarity_vector")

# Fit the model to the dissimilarity matrix
model = agglomerative.fit(dissimilarityMatrix)

# Obtain the predicted cluster labels for the dissimilarity matrix
predictions = model.transform(dissimilarityMatrix)

# Show the predicted cluster labels
predictions.select("prediction").show()
