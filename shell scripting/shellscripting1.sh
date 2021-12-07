#!/bin/bash

echo "please provide 1, 2 or 3 for password change, password reset or something else:"

if [ $1 == "1" ]
then 
case $1 in
   "1") echo "change password";;
   "2") echo "reset password";;
   "3") echo "something";;
