#!/bin/bash
#shell script that prints all databases
user='root'
password='root'
command='SHOW DATABASES;'
mysql -u $user -p$password -e "$command"
