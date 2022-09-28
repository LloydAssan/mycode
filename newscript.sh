#!/bin/bash


prompt() { 
 echo "Enter name here: "
 read userName
 echo "Enter group here: "
 read userGroupName
}

userCreate() {
 echo "New user add."
 sudo useradd $userName
 echo
 echo "$userName was created."
 echo "$userGroupName created and added $userGroupName"

 sudo groupadd $userGroupName
 echo "$userName added to $userGroupName"

 sudo usermod -aG $userName $userGroupName
 echo "Complete"
}

prompt
