CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	username VARCHAR(255),
	password VARCHAR(255),
	email VARCHAR(255),
	address VARCHAR(100),
	birthdate DATE,
	name VARCHAR(255),
	gender VARCHAR(50)
);

CREATE TABLE transactions(
	transaction_id SERIAL PRIMARY KEY,
	user_origin_id INTEGER,
	user_destination_id INTEGER,
	value FLOAT
);

CREATE TABLE balances(
	balance_id SERIAL PRIMARY KEY,
	user_id INTEGER,
	value FLOAT
);
