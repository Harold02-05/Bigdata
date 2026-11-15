from pyspark.sql.functions import year, to_date

# prmero: Convertir 'date_added' a formato fecha y extraer el año

df_transformed = df_clean.withColumn("date_added_clean", to_date(df_clean["date_added"], "MMMM d, yyyy"))
df_transformed = df_transformed.withColumn("year_added", year("date_added_clean"))

# Segundo: Verificar que se creó la nueva columna (mostrar título, fecha original y año)
print("--- Años extraídos ---")
df_transformed.select("title", "date_added", "year_added").show(5)