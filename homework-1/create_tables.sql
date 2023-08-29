-- Создание базы данных
CREATE DATABASE north;

-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	title varchar(100) NOT NULL,
	birth_date date NOT NULL,
	notes text
);

CREATE TABLE customer_data
(
	customer_id varchar(5) PRIMARY KEY,
	company_name varchar(200),
	contact_name varchar(100) NOT NULL
);

CREATE TABLE orders_data
(
	order_id int PRIMARY KEY,
	customer_id varchar(5) UNIQUE REFERENCES customer_data(customer_id),
	employee_id int UNIQUE REFERENCES employees(employee_id),
	order_date date NOT NULL,
	ship_city varchar(100) NOT NULL
);

