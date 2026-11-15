# Creando una vista temporal para usar SQL
df_transformed.createOrReplaceTempView("netflix")

print("\n--- 1. Cantidad de Películas vs Series ---")
spark.sql("""
    SELECT type, COUNT(*) as cantidad 
    FROM netflix 
    GROUP BY type
""").show()

print("\n--- 2. Top 5 Países con más contenido ---")
spark.sql("""
    SELECT country, COUNT(*) as cantidad 
    FROM netflix 
    GROUP BY country 
    ORDER BY cantidad DESC 
    LIMIT 5
""").show()

print("\n--- 3. Top 5 Años con más contenido agregado ---")
spark.sql("""
    SELECT year_added, COUNT(*) as cantidad 
    FROM netflix 
    GROUP BY year_added 
    ORDER BY cantidad DESC 
    LIMIT 5
""").show()