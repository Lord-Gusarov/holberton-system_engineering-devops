#!/usr/bin/env bash
# We need at least one database and one table to set up replication
if [[ $# -lt 2 ]]; then
	echo "USAGE: $0 <user> <password>"
else
	db="tyrell_corp"
	table="nexus6"

	mysql -u"$1" -p"$2" << EOQs
	CREATE DATABASE IF NOT EXISTS $db;
	USE $db;
	CREATE TABLE IF NOT EXISTS $table(
		id INT AUTO_INCREMENT PRIMARY KEY,
		name CHAR(255) NOT NULL
		);
	INSERT INTO $table (name) VALUES ('Carlos');
	INSERT INTO $table (name) VALUES ('OSVALDO');

	GRANT SELECT ON $table to 'holberton_user'@'localhost';
	FLUSH PRIVILEGES;
EOQs
fi
