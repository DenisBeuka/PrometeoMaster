
-- 1. Mostrar los nombres de todas las películas con una clasificación por edades de ‘R’.
SELECT title
FROM film
WHERE rating = 'R';

-- 2. Encuentra los nombres de los actores que tengan un “actor_id” entre 30 y 40.
SELECT first_name, last_name
FROM actor
WHERE actor_id BETWEEN 30 AND 40;

-- 3. Mostrar las películas cuyo idioma coincide con el idioma original
-- (Esta consulta devuelve vacío porque en los datos no hay coincidencias reales o hay muchos NULLs).
SELECT title
FROM film
WHERE original_language_id IS NOT NULL
  AND language_id = original_language_id;

-- 4. Ordenar las películas por duración de forma ascendente
SELECT title, length
FROM film
ORDER BY length ASC;

-- 5. Encontrar el nombre y apellido de los actores que tengan ‘Allen’ en su apellido
SELECT first_name, last_name
FROM actor
WHERE ILIKE('%Allen%');

-- Alternativa estándar para otros gestores de bases de datos (usando LOWER)
-- SELECT first_name, last_name FROM actor WHERE LOWER(last_name) LIKE '%allen%';

-- 6. Encuentra la cantidad total de películas en cada clasificación de la tabla film
-- Muestra la clasificación (rating) junto con el número de películas
SELECT rating, COUNT(*) AS total_peliculas
FROM film
GROUP BY rating
ORDER BY rating;

-- 7. Películas que son 'PG-13' o tienen duración mayor a 180 minutos
-- Se evita considerar los valores NULL en la duración
SELECT title, rating, length
FROM film
WHERE rating = 'PG-13' OR (length IS NOT NULL AND length > 180);

-- 8. Encuentra la variabilidad de lo que costaría reemplazar las películas
-- Se muestra el mínimo, máximo, promedio, desviación estándar y varianza del campo replacement_cost
SELECT 
  MIN(replacement_cost) AS minimo,
  MAX(replacement_cost) AS maximo,
  AVG(replacement_cost) AS promedio,
  STDDEV(replacement_cost) AS desviacion_estandar,
  VARIANCE(replacement_cost) AS varianza
FROM film;


-- 9. Mostrar los títulos de las películas y los nombres de los idiomas en los que están disponibles
SELECT f.title, l.name AS idioma
FROM film f
JOIN language l ON f.language_id = l.language_id;

-- 10. Listar los clientes con su ciudad y país
SELECT c.first_name, c.last_name, ci.city, co.country
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id;

-- 11. Mostrar el título de las películas y los actores que participan en ellas
SELECT f.title, a.first_name, a.last_name
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
ORDER BY f.title, a.last_name;

-- 12. Mostrar los nombres de los clientes que han alquilado al menos una película
SELECT DISTINCT c.first_name, c.last_name
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id;
