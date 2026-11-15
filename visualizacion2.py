import os

# 1. Mostrar la gráfica en texto
print("\n--- VISUALIZACIÓN EN TEXTO (Distribución por Tipo) ---")
df_movies = spark.sql("SELECT COUNT(*) as count FROM netflix WHERE type = 'Movie'").collect()[0]['count']
df_tv = spark.sql("SELECT COUNT(*) as count FROM netflix WHERE type = 'TV Show'").collect()[0]['count']
print(f"Movies : {'*' * 50} ({df_movies})")
print(f"TV Show: {'*' * 22} ({df_tv})")

# 2. Guardar en carpeta local de Ubuntu (sin errores de permisos)
print("\n--- GUARDANDO RESULTADOS LOCALMENTE ---")
paises_df = spark.sql("SELECT country, COUNT(*) as cantidad FROM netflix GROUP BY country ORDER BY cantidad DESC LIMIT 5")
anios_df = spark.sql("SELECT year_added, COUNT(*) as cantidad FROM netflix GROUP BY year_added ORDER BY cantidad DESC LIMIT 5")

# Guardamos en /tmp (carpeta temporal de Ubuntu)
paises_df.coalesce(1).write.csv("/tmp/top_paises_temp", header=True, mode="overwrite")
anios_df.coalesce(1).write.csv("/tmp/top_anios_temp", header=True, mode="overwrite")

print("Datos procesados. Ahora ejecuta los comandos de Linux para moverlos a Windows.")