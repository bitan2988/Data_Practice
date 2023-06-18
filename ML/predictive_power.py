from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import RegressionEvaluator, BinaryClassificationEvaluator, MulticlassClassificationEvaluator
from pyspark.ml.feature import OneHotEncoder

def predictive_power(data, target_variable, categorical_columns, numerical_columns, task="regression"):
    maescores = dict()
    # Index the target variable (if it's a classification task)
    if task == "classification":
        indexer = StringIndexer(inputCol=target_variable, outputCol="indexed_target")
        data = indexer.fit(data).transform(data)
        target_col = "indexed_target"
    else:
        target_col = target_variable
    # Index and encode categorical columns
    for cat_col in categorical_columns:
        indexer = StringIndexer(inputCol=cat_col, outputCol=f"{cat_col}_index")
        data = indexer.fit(data).transform(data)
        encoder = OneHotEncoder(inputCol=f"{cat_col}_index", outputCol=f"{cat_col}_onehot")
        data = encoder.fit(data).transform(data)
    # Initialize the model and evaluator
    if task == "regression":
        model = LinearRegression(labelCol=target_col)
        evaluator = RegressionEvaluator(labelCol=target_col, metricName="r2")
    else:
        model = LogisticRegression(labelCol=target_col)
        auc_evaluator = BinaryClassificationEvaluator(labelCol=target_col, metricName="areaUnderROC")
        f1_evaluator = MulticlassClassificationEvaluator(labelCol=target_col, metricName="f1")


    # Calculate the predictive power of each feature
    encoded_columns = [str(colName)+"_onehot" for colName in categorical_columns]
    numerical_columns.extend(encoded_columns)
    input_columns = numerical_columns

    for column in input_columns:
        if column not in categorical_columns:
            assembler = VectorAssembler(inputCols=[column], outputCol="features")
            feature_data = assembler.transform(data)

            # Split the data into training and test sets
            train_data, test_data = feature_data.randomSplit([0.8, 0.2])

            # Train and evaluate the model
            fitted_model = model.fit(train_data)
            predictions = fitted_model.transform(test_data)

            if task == "regression":
                mae = evaluator.evaluate(predictions)
                maescores[column] = mae
            else:
                length_raw_prediction = len(predictions.select(["rawPrediction"]).first()[0])
                if length_raw_prediction <= 2:
                    auc = auc_evaluator.evaluate(predictions)
                    f1_score = None
                else:
                    f1_score = f1_evaluator.evaluate(predictions)
                    auc = None
                maescores[column] = {"auc": auc, "f1_score": f1_score}
    return maescores

# Initialize the Spark session
spark = SparkSession.builder.master("local").appName("PredictivePower").getOrCreate()

# Load the dataset
data = spark.read.csv("data/insurance.csv", header=True, inferSchema=True)

# Define the target variable
target_variable = "region"

categorical_columns = ["sex"]
numerical_columns = ["children", "bmi", "age", "charges"]

maescores = predictive_power(data, target_variable, categorical_columns, numerical_columns, "regression")