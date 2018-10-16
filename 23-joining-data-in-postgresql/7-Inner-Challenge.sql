''

Inner challenge

The table you created with the added geosize_group field has been loaded for you here with the name countries_plus. Observe the use of (and the placement of) the INTO command to create this countries_plus table:

SELECT name, continent, code, surface_area,
    CASE WHEN surface_area > 2000000
            THEN 'large'
       WHEN surface_area > 350000
            THEN 'medium'
       ELSE 'small' END
       AS geosize_group
INTO countries_plus
FROM countries;

You will now explore the relationship between the size of a country in terms of surface area and in terms of population using grouping fields created with CASE.

By the end of this exercise, you'll be writing two queries back-to-back in a single script. You got this!
Instructions 1/3
35 XP

    1
    2
    3

Using the populations table focused only for the year 2015, create a new field AS popsize_group to organize population size into

    'large' (> 50 million),
    'medium' (> 1 million), and
    'small' groups.

Select only the country code, population size, and this new popsize_group as fields.

    Take Hint (-10 XP)
''

SELECT p.country_code, p.size,
  -- start CASE here with WHEN and THEN
    CASE WHEN size > 50000000
        THEN 'large'
  -- layout other CASE conditions here
    WHEN size > 1000000
        THEN 'medium'
  -- end CASE here with ELSE & END
    ELSE 'small' END
  -- provide the alias of popsize_group to SELECT the new field
    AS popsize_group
-- which table?
FROM populations AS p
-- any conditions to check?
WHERE p.year = 2015;



SELECT country_code, size,
    CASE WHEN size > 50000000 THEN 'large'
        WHEN size > 1000000 THEN 'medium'
        ELSE 'small' END
        AS popsize_group
FROM populations
WHERE year = 2015;
