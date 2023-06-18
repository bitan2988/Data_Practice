-- Creating DWH tables

-- Dimension Table
CREATE TABLE dim_date
(
	date_key SERIAL PRIMARY KEY,
	date DATE NOT NULL,
	year year NOT NULL,
	quarter smallint NOT NULL,
	month month NOT NULL,
	week smallint NOT NULL,
	day day NOT NULL,
	is_weekend boolean NOT NULL
);

CREATE TABLE dim_movie
(
	movie_key SERIAL PRIMARY KEY,
	film_id integer,
	title varchar(255),
	description text,
	release_year smallint,
	language varchar(255),
	original_language varchar(255),
	length smallint,
	ratings numeric(3,1),
	special_features varchar[]
)

CREATE TABLE dim_customers
(

)

CREATE TABLE dim_store
(

)


select * from film;

select column_name, data_type from information_schema.columns
where table_name = 'film'