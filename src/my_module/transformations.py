from pyspark.sql import DataFrame

def clean_data(df: DataFrame) -> DataFrame:
    return df.dropna().dropDuplicates()
