Sistema de Gestión de Red Wi‑Fi Comunitaria

Este proyecto presenta la implementación de una base de datos NoSQL utilizando MongoDB para la gestión de una red Wi‑Fi comunitaria. La solución fue desarrollada con el propósito de administrar la información relacionada con los usuarios registrados, los puntos de acceso disponibles y las conexiones realizadas dentro de la red, permitiendo almacenar y consultar datos de manera eficiente mediante un modelo documental.

La base de datos denominada wifi_comunitaria está compuesta por tres colecciones principales: usuarios, donde se almacena la información de las personas registradas en la red; puntos_acceso, destinada a gestionar los diferentes puntos de conexión distribuidos en la comunidad; y conexiones, encargada de registrar el historial de acceso y el consumo de datos de los usuarios. Esta estructura permite representar de manera flexible las relaciones y operaciones propias del sistema propuesto.

Como parte del proceso de implementación se cargó un conjunto de datos de prueba superior a cien documentos, distribuidos entre las diferentes colecciones de la base de datos. Estos registros permitieron validar el funcionamiento de las operaciones y consultas requeridas para la actividad, simulando un entorno real de administración de una red Wi‑Fi comunitaria.

Durante el desarrollo del proyecto se implementaron las operaciones básicas de gestión de datos (CRUD), incluyendo la inserción de nuevos documentos, la consulta de información almacenada, la actualización de registros existentes y la eliminación de documentos. Estas operaciones permitieron verificar la capacidad de MongoDB para manipular información de forma dinámica y eficiente.

Adicionalmente, se realizaron consultas utilizando filtros y operadores de búsqueda para recuperar información específica de acuerdo con diferentes criterios, tales como usuarios con determinados planes de servicio o rangos de edad. También se implementaron consultas de relación entre colecciones mediante el operador $lookup, permitiendo asociar la información de los usuarios con los registros de conexiones realizados en la red.

Con el fin de obtener información estadística relevante para la administración del sistema, se desarrollaron consultas de agregación orientadas al análisis de datos. Estas consultas permitieron calcular el número de usuarios registrados, el consumo total de datos y el consumo promedio por conexión, demostrando la utilidad de MongoDB para procesar y analizar grandes volúmenes de información en aplicaciones de tipo comunitario.

Los resultados obtenidos evidencian que MongoDB constituye una alternativa adecuada para el almacenamiento y gestión de información en sistemas de conectividad comunitaria, gracias a su flexibilidad, escalabilidad y facilidad para realizar operaciones de consulta y análisis sobre datos estructurados en formato documental.

Autor: Harold Erney Hernandez Rodriguez
 Programa: Ingeniería de Sistemas - UNAD
 Actividad: Implementación de una Base de Datos NoSQL en MongoDB
 Caso de Estudio: Sistema de Gestión de Red Wi‑Fi Comunitaria.
