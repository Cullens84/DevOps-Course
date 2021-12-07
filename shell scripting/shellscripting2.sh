#!/bin/bash

if [ $1 == "5" ]
then
   x=$1
   y=$2
   echo $((x+y))

   fname=$3
   lname=$4
   echo $fname $lname


   message=$5
   echo $message
else
   echo "the first paramenter is expected to be 5"
fi

case $1 in 
   #case 1
   "1") echo "you enteres 1";;
   "2")echo "you entered 2";;
   "3") echo "you entered 3";;
esac


