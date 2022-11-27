/*CREATE DATABASE Circus
*/
CREATE TABLE artisitc_directors (
	id int,
	name_surname varchar(255),
	PRIMARY KEY (id));

CREATE TABLE artists (
	id int,
	name_surname varchar(255),
	pseudonym varchar(255),
	PRIMARY KEY (id));

CREATE TABLE equipment (
	id int,
	name varchar(255),
	producer varchar(255),
	is_current bit,
	PRIMARY KEY (id));

CREATE TABLE performances (
    id Int,
    artistic_director_id Int,
    date_id Int,
    city varchar(255),
	PRIMARY KEY (id),
	FOREIGN KEY (artistic_director_id) REFERENCES artisitc_directors(id),
	FOREIGN KEY (date_id) REFERENCES date(id)
);

CREATE TABLE date (
    id Int,
    year Int,
	month varchar(12),
    month_no Int,
	day Int,
    day_of_week varchar(15),
	day_of_week_no Int
	PRIMARY KEY (id)

);



CREATE TABLE acts (
	id Int,
	performance_id Int,
	artist_id Int,
	equipment_id Int,
	accident_id Int,
	grade float,
	surveyed Int,
	accidents_num Int,

	PRIMARY KEY (id), 
	FOREIGN KEY (performance_id) REFERENCES performances(id),
	FOREIGN KEY (artist_id) REFERENCES artists(id),
	FOREIGN KEY (equipment_id) REFERENCES equipment(id),
	FOREIGN KEY (accident_id) REFERENCES accidents(id)
	);

CREATE TABLE accidents (
	id int,
	type int,
	report varchar(255),
	PRIMARY KEY (id)
);
-- CREATE TABLE act_equipment (
-- 	equipment_id Int,
-- 	act_id Int
-- 	PRIMARY KEY (equipement_id,act_id),
-- 	FOREIGN KEY (equipement_id) REFERENCES equipement(id),
-- 	FOREIGN KEY (act_id) REFERENCES acts(id)
-- );

-- CREATE TABLE artist_act (
-- 	artist_id int,
-- 	act_id int,
-- 	PRIMARY KEY (artist_id,act_id),
-- 	FOREIGN KEY (artist_id) REFERENCES artists(id),
-- 	FOREIGN KEY (act_id) REFERENCES acts(id)
-- );
/*
DROP DATABASE Circus;


DROP TABLE act_equipement,artist_act,incidents,acts,performances,artisitc_directors,equipement,artists;
*/