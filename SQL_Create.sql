CREATE performances (
    id Int,
    artistic_director_id Int,
    time time,
    location varchar(255)
);

CREATE acts (id Int,performance_id Int,name varchar(255),decription varchar(255));

CREATE act_equipement (equipement_id Int,act_id Int);

CREATE equipements (id int,name varchar(255));

CREATE artist_act (artist_id int,act_id int);

CREATE artists (id int,name varchar(255),surname varchar(255),pseudonym varchar(255));

CREATE incidents (id int,type int,report varchar(255),act_id int);

CREATE artisitc_directors (id int,name varchar(255),surname varchar(255))