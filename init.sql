
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


insert into article(article_title, article_text, article_date) values('Первая статья', 'текст текст', '22.11.2018 20:55:12');

insert into article(article_title, article_text, article_date) values('Вторая статья', 'текст второй статьи', '22.11.2018 20:59:09');
insert into article(article_title, article_text, article_date) values('Третья статья', 'текст третой статьи', '23.11.2018 16:34:45');



insert into comments(comments_text, article_id) values('Первой комментарий', '1');
insert into comments(comments_text, article_id) values('Второй комментарий', '1');

insert into comments(comments_text, article_id) values('Третий комментарий', '1');
insert into comments(comments_text, article_id) values('Единственный коммент', '2');


insert into comments(comments_text, article_id) values('Коммент для третий статьи', '3');
