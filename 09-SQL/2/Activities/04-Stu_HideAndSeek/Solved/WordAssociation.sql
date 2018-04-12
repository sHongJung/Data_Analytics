SELECT * FROM wordassociation
WHERE source = "AC";

SELECT * FROM wordassociation
WHERE source = "BC";

SELECT * FROM wordassociation
WHERE source = "CC";

SELECT * FROM wordassociation
WHERE author >= 0 AND author <= 20;

SELECT * FROM wordassociation
WHERE word1 = "pie" OR word2 = "pie";