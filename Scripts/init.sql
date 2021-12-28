CREATE TABLE gamesales (
  rank INT PRIMARY KEY,
  name varchar(500) NOT NULL,
  platform varchar(30) NOT NULL ,
  year int,
  genre varchar(20) NOT NULL,
  publisher varchar(50)
  NA_sales float NOT NULL,
  EU_sales float NOT NULL,
  JP_sales float NOT NULL,
  other_sales float NOT NULL,
  global_sales float NOT NULL
);