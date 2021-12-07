#1/bin/bash

selection=0

while [ $selection -le 4 ]

do

   echo "please select an option:"
   echo "1-tv"
   echo "2-radio"
   echo "3-laptops"
   echo "4-desktops"
   echo "5-exit"
   
   echo ""
   read selection

   case $selection in
	"1") echo "you selected TV";;
	"2") echo "you selected radio";;
	"3") echo "you selected laptops";;
	"4") echo "you selected desktop";;

   esac

done

echo "goodbye"


