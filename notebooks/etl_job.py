from my_module.transformations import clean_data

df = spark.read.table("catalog.schema.raw_table")
df_clean = clean_data(df)
df_clean.write.mode("overwrite").saveAsTable("catalog.schema.cleaned_table")
