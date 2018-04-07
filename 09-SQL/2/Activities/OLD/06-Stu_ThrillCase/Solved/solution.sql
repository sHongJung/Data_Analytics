
-- Solution to activity
UPDATE top5000
SET artist =
CASE
  WHEN artist = 'Bill van Halen'
  THEN 'Bill van Halen and the Licks'
  WHEN artist = 'Bill Haliday'
  THEN 'Bill Haliday and the Jazz'
ELSE 'Bill Haley and the Comets'
END
WHERE position = 2;

  
-- Solution to bonus
UPDATE top5000
SET `artist` =
CASE
  WHEN artist = 'Bing Crosby'
  THEN 'Bill Throggs Neck'
  WHEN artist = 'Celine Dion'
  THEN 'Sarah Hellion'
ELSE 'Skrillex'
END
WHERE position BETWEEN 1 and 5; 
