#!/usr/bin/bash

user='root'
password='xGOjiagJ3dN'
host='localhost'
command='SHOW DATABASES;'
mysql -u $user -p$password -h $host -e "$command"

