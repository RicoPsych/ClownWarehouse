/*CREATE DATABASE Circus
*/
CREATE TABLE artisitc_directors (
	id int,
	name varchar(255),
	surname varchar(255),
	PRIMARY KEY (id));

CREATE TABLE artists (
	id int,
	name varchar(255),
	surname varchar(255),
	pseudonym varchar(255),
	PRIMARY KEY (id));

CREATE TABLE equipment (
	id int,
	name varchar(255),
	producer varchar(255),
	PRIMARY KEY (id));

CREATE TABLE performances (
    id Int,
    artistic_director_id Int,
    time date,
    location varchar(255),
	PRIMARY KEY (id),
	FOREIGN KEY (artistic_director_id) REFERENCES artisitc_directors(id)
);


CREATE TABLE acts (
	id Int,
	performance_id Int,
	artist_id Int,
	equipment_id Int,
	name varchar(255),
	description varchar(255),
	
	PRIMARY KEY (id), 
	FOREIGN KEY (performance_id) REFERENCES performances(id),
	FOREIGN KEY (artist_id) REFERENCES artists(id),
	FOREIGN KEY (equipment_id) REFERENCES equipment(id)
	);

CREATE TABLE accidents (
	id int,
	type int,
	report varchar(255),
	act_id int,
	PRIMARY KEY (id), 
	FOREIGN KEY (act_id) REFERENCES acts(id));

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