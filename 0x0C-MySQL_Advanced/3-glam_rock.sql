--SQL script that lists all bands with Glam rock
-- as their main style, ranked by their longevity
SELECT DISTINCT band_name,
    IFNULL(split, YEAR(CURDATE())) - IFNULL(formed, 0) as lifespan
FROM metal_bands
WHERE FIND_IN_SET('Glam rock', style)
ORDER BY lifespan DESC;
