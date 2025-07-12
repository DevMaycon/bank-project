CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	username VARCHAR(255) UNIQUE NOT NULL,
	password VARCHAR(255),
	email VARCHAR(255) UNIQUE NOT NULL,
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
	user_id INTEGER UNIQUE,
	value FLOAT
);

INSERT INTO users (username, password, email, address, birthdate, name, gender) VALUES (
	'admin', 'admin', 'admin@financeadmin.com', 'Access Administrator 100.', '2000-01-01', 'Administrator', 'M'
);

INSERT INTO balances (user_id, value) SELECT id, 1000000000000000.00 FROM users WHERE email = 'admin@financeadmin.com';