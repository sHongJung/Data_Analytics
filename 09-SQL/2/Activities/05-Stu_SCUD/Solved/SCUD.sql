DELETE FROM globalfirepower
WHERE ReservePersonnel = 0;

UPDATE globalfirepower
SET FighterAircraft = 1
WHERE FighterAircraft = 0;

UPDATE globalfirepower
SET TotalAircraftStrength = TotalAircraftStrength + 1
WHERE FighterAircraft = 1;

SELECT AVG(TotalMilitaryPersonnel)
FROM globalfirepower;

SELECT AVG(TotalAircraftStrength)
FROM globalfirepower;

SELECT AVG(TotalHelicopterStrength)
FROM globalfirepower;

SELECT AVG(TotalPopulation)
FROM globalfirepower;

INSERT INTO globalfirepower(Country, TotalPopulation, TotalMilitaryPersonnel, TotalAircraftStrength, TotalHelicopterStrength)
VALUES ("JacobLand",85175106,741101,639,256);

SELECT * FROM globalfirepower;