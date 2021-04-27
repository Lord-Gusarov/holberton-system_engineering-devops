#/usr/bin/env bash
# Creates a MYSQL user for Holberton Testing purposes
if [[ $# -lt 2 ]]
then
	echo "USAGE: $0 <user> <password>"
else
	mysql -u "$1" -p"$2" << CRT_USER
		CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
		GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
		FLUSH PRIVILEGES;
CRT_USER
fi
