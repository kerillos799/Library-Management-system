create table authors(
	id INT not null identity(1,1),
	fname varchar(50) not null,
	lname varchar(50), 
	date_of_birth date, 
	primary key(id)
);
create table book(
	id INT not null identity(1,1),
	name text not null,
	isbn varchar(50) unique not null,
	published_year int,
	author_id INT references authors (id),
	primary key(id)
);
create table members (
	id INT not null identity(1,1),
	fname varchar(50) not null,
	lname varchar(50),
	tele_num varchar(15),
	membership_date date
	primary key(id)
);
create table borrow(
	id INT not null identity(1,1), 
	loan_date date not null,
	return_date date,
	member_id INT references members(id),
	book_id INT references book(id),
	primary key(id)
);
