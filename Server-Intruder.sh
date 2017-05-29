#!/bin/bash
# -*- coding: utf-8 -*-

########################################
# Author: Souhardya Sardar             #
#                                      #
# Build: Server-Intruder 1.0           #
########################################


G='\033[1;32m'

echo -e "\x1B[01;38m    ################### \x1B[0m"
echo -e "\x1B[01;38m    ################### \x1B[0m"
echo -e "\x1B[01;38m    #                 \x1B[01;38m#\x1B[0m"
echo -e "\x1B[01;38m   ## \x1B[0m                \x1B[01;38m##\x1B[0m"
echo -e "\x1B[01;38m  ### \x1B[0m                \x1B[01;38m###\x1B[0m"
echo -e "\x1B[01;38m #### \x1B[0m\x1B[01;33mSOUHARDYA SARDAR\x1B[0m \x1B[01;38m######\x1B[0m"  " SERVER INTRUDER "
echo -e "\x1B[01;38m  ### \x1B[0m\x1B[01;36m\x1B[0m  \x1B[01;38m\x1B[0m"
echo -e "\x1B[01;38m   ## \x1B[0m                \x1B[01;38m##\x1B[0m"
echo -e "\x1B[01;38m    # \x1B[0m                \x1B[01;38m#\x1B[0m"
echo -e "\x1B[01;38m    ################### \x1B[0m"
echo -e "\x1B[01;38m    ################### \x1B[0m"
echo -e ""

 


echo -e "${G}Server Intruder : An automation script written in bash for checking intruder 
IP which may have logged into your system :3 ${G} " 



echo -e "                        ~ Coded by Souhardya Sardar ~ "




echo -e " [*] Discover how many usernames logged in the system :D [*] "
users
echo -e "[*] If you discover new usernames then you are fucked :3 [*]"
sleep 5s


echo -e " [*] Let's take a look at secure.log [*] "
cat /var/log/secure
echo -e " [*] Look how many failed login attempts you got [*] "
echo -e " [*] Additionally you might see shit load of bruteforce attempts [*] "
sleep 10s


echo -e " [*] Let's take a look at Message Logs [*] "
cat /var/log/messages 
echo -e " [*] Time sleep value increased as file might be big [*] "
sleep 15s 

echo -e " [*] Let's take a look at the bash / shell history [*] "
cat .bash_history 
echo -e " [*] If you compromised then maybe some scripts were run or new modules were installed [*] "
sleep 10s

echo -e " [*] Let's find the exact count of failed logins [*] "
cat /var/log/secure | grep sshd.*opened 
echo -e " [*] This will show you the ssh logins attempted and succesfull [*] "
