1) SELECT language,percentange,countries.name
FROM languages
JOIN countries
ON countries.id = languages.countries_id
WHERE language = 'Slovene'
ORDER BY percentange DESC
SELECT countries.name, COUNT(cities.id) as num_cities
FROM countries
	JOIN cities ON countries.id = cities.country_id
GROUP BY countries.id
order by num