# Eliminando duplicados
df_clean = df.dropDuplicates()

# Llenar nulos en country y director por Unknown
df_clean = df_clean.fillna({"country": "Unknown", "director": "Unknown"})

# Verificando el conteo
print("Conteo después de limpieza:", df_clean.count())

# Mostrndo las primeras filas para verificar
df_clean.select("country", "director").show(5)