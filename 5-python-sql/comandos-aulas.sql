------------------------------------------------------------------------------
-- Lista Acumulativa de Comandos usados em Aula
------------------------------------------------------------------------------

CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);

INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'London', 415);
INSERT INTO flights (origin, destination, duration) VALUES ('Shangai', 'Paris', 760);
INSERT INTO flights (origin, destination, duration) VALUES ('Istanbul', 'Tokyo', 700);
INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'Paris', 435);
INSERT INTO flights (origin, destination, duration) VALUES ('Moscow', 'Paris', 245);
INSERT INTO flights (origin, destination, duration) VALUES ('Lima', 'New York', 455);

SELECT * FROM flights;

SELECT origin, destination FROM flights;

SELECT * FROM flights WHERE id = 3;

SELECT * FROM flights WHERE origin = 'New York';

SELECT * FROM flights WHERE duration > 700;

SELECT * FROM flights WHERE destination = 'Paris' AND duration > 700;

SELECT * FROM flights WHERE destination = 'Paris' OR duration >= 700;

SELECT AVG(duration) FROM flights;

SELECT AVG(duration) FROM flights WHERE origin = 'New York';

SELECT COUNT(duration) FROM flights;

SELECT COUNT(duration) FROM flights WHERE origin = 'New York';

SELECT * FROM flights WHERE origin IN ('New York', 'Lima');

SELECT * FROM flights WHERE origin LIKE 'New%';

SELECT UPPER(origin), UPPER(destination) FROM flights WHERE destination = 'Paris';

SELECT UPPER(origin), UPPER(destination) FROM flights WHERE UPPER(destination) = 'PARIS';

SELECT UPPER(origin), UPPER(destination) FROM flights WHERE LOWER(destination) = 'paris';

--------------------------

SELECT destination, COUNT(destination) FROM flights
GROUP BY destination

SELECT destination, COUNT(*) FROM flights
GROUP BY destination

-- Vai dar erro:
SELECT destination, origin, count(*) FROM flights
GROUP BY destination 


SELECT destination, COUNT(*), SUM(duration) FROM flights
GROUP BY destination


SELECT destination, COUNT(*) FROM flights
GROUP BY destination
HAVING COUNT(*) > 1


SELECT destination, COUNT(*) FROM flights GROUP BY destination HAVING COUNT(*) > 1
