select countries.name, languages.language,languages.percentage 
from countries 
 join languages
on 
countries.id=languages.country_id
where languages.language="Slovene"
order by languages.percentage desc
---------------------------------------------
select countries.name ,count(cities.country_id) as count
from countries 
join cities
on countries.id = cities.country_id
Group by countries.name
order by count desc
-------------------------------------------
select countries.name,cities.name,cities.population
from countries
join cities
on countries.id=cities.country_id
where cities.population >500000 
and countries.name="Mexico"
order by cities.population desc
---------------------------------------------
select countries.name,languages.language,languages.percentage
from countries 
join languages
on countries.id=languages.country_id
where languages.percentage >89
order by languages.percentage desc
-------------------------------------------
select countries.name,countries.surface_area,countries.population 
from countries
where surface_area< 501
and countries.population > 100000
--------------------------------------------------------------
select countries.name,countries.government_form,countries.life_expectancy,countries.capital
from countries
where countries.government_form="Constitutional Monarchy"
and countries.life_expectancy >75
and  countries.capital >200
--------------------------------------------------------------
select countries.name,cities.name,cities.district,cities.population
from countries
join cities
on countries.id=cities.country_id
where countries.name="Argentina"
and cities.district="Buenos Aires"
and cities.population > 500000
---------------------------------------------------------
select countries.region,count(countries.id) as count
from countries
Group by countries.region
order by count desc
------------------------------

select * from countries
select * from cities
select * from languages
