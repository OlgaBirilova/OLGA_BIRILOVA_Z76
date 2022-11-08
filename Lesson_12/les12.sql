use Lesson_12;

CREATE TABLE pc (
code int,
model VARCHAR(50),
speed smallint,
ram smallint,
hd real,
cd VARCHAR(10),
price float
);

INSERT INTO pc (model, speed, ram, hd, cd, price)
VALUES("Dell", 150, 64, 1000, "yes", 500);

INSERT INTO pc (model, speed, ram, hd, cd, price)
VALUES("Shell", 200, 64, 1000, "yes", 300);

INSERT INTO pc (model, speed, ram, hd, cd, price)
VALUES("Samsung", 150, 64, 1500, "no", 400);

INSERT INTO pc (model, speed, ram, hd, cd, price)
VALUES("Lenovo", 3000, 128, 1350, "yes", 700);

INSERT INTO pc (model, speed, ram, hd, cd, price)
VALUES("Asus", 6885, 32, 1200, "no", 755);

INSERT INTO pc (model, speed, ram, hd, cd, price)
VALUES("Acer", 4261, 64, 1200, "yes", 220);

INSERT INTO pc (model, speed, ram, hd, cd, price)
VALUES("Honor", 3000, 64, 800, "no", 250);

SELECT * FROM pc WHERE price < 400;

SELECT code, speed, hd FROM pc WHERE ram BETWEEN 8 AND 32 order by model;

SELECT price FROM pc WHERE hd < 1000;

SET SQL_SAFE_UPDATES = 0;
UPDATE pc SET price = price * 2 WHERE price > 400;



