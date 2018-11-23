
create table post(
	id serial,
	title varchar(255) not null, 
	body text
);


create table users(
	id serial,
	username varchar(255) not null, 
	email varchar(255) not null, 
	password varchar(255) not null
);


create table article(
	article_id serial,
	article_title varchar(255) not null, 
	article_text text not null, 
	article_date timestamp not null
);

create table comments(
	comments_id serial,
	comments_text text not null, 
	article_id int not null
);




