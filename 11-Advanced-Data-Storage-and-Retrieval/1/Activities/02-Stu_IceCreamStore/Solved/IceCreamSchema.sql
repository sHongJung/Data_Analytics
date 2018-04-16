--- USE <DB NAME>;

-- Create Table
DROP TABLE icecreamstore;

CREATE TABLE `icecreamstore` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `Flavors` VARCHAR(45) NULL,
  `Quantities` INT NULL,
  `Price` DECIMAL(65,2) NULL,
  PRIMARY KEY (`ID`));
  
-- Insert Rows
INSERT INTO `icecreamstore` (`Flavors`, `Quantities`, `Price`)
VALUES ('Vanilla', '100', '1.00'),('Chocolate', '150', '1.25'),('Strawberry', '95', '1.25'),('Rocky Road', '50', '1.50'),('Cookie Dough', '75', '1.50');

-- Select ALl Records
select * from icecreamstore

-- Select Single Record
select * from icecreamstore where Price=1.25;