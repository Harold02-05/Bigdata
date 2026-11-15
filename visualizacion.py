print("\n--- VISUALIZACIÓN EN TEXTO (Distribución por Tipo) ---")
# Creamos una gráfica de barras "manual" con asteriscos
df_movies = spark.sql("SELECT COUNT(*) as count FROM netflix WHERE type = 'Movie'").collect()[0]['count']
df_tv = spark.sql("SELECT COUNT(*) as count FROM netflix WHERE type = 'TV Show'").collect()[0]['count']

print(f"Movies : {'*' * 50} ({df_movies})")
print(f"TV Show: {'*' * 22} ({df_tv})")

print("\n--- EXPORTANDO RESULTADOS A CSV ---")
# Guardar el Top 5 de países en la carpeta compartida
paises_df = spark.sql("""
    SELECT country, COUNT(*) as cantidad 
    FROM netflix 
    GROUP BY country 
    ORDER BY cantidad DESC 
    LIMIT 5
""")
# Spark guarda en una carpeta, así que lo escribimos así:
paises_df.coalesce(1).write.csv("/media/sf_Downloads/top_paises_netflix.csv", header=True, mode="overwrite")

# Guardar el Top 5 de años
anios_df = spark.sql("""
    SELECT year_added, COUNT(*) as cantidad 
    FROM netflix 
    GROUP BY year_added 
    ORDER BY cantidad DESC 
    LIMIT 5
""")
anios_df.coalesce(1).write.csv("/media/sf_Downloads/top_anios_netflix.csv", header=True, mode="overwrite")

print("¡Archivos CSV guardados con éxito en Windows (carpeta Descargas)!")