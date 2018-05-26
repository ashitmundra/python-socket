#!/usr/bin/python
import socket
import thread
#importing libraries

rec_ip="127.0.0.1"
myport=8888

contact_ip=raw_input("Enter Contact IP address: ")
contact_port=raw_input("Enter contact port: ")

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#socket for udp
s.bind((rec_ip, myport))
#Binding ip address with port

name=raw_input("Enter Your Name    ")
#entering chat name
s.sendto(name, (contact_ip, int(contact_port)))
#sending data to the ip
name_recieve=s.recvfrom(100)
#ecieving data back


def rc():   
 #recieving function
 while True:
  rec_msg=s.recvfrom(1000)
  print (name_recieve[0]+":"+rec_msg[0])
  #printing msg


def sc():
 #sending function
 while True:
  msg=raw_input()
  #taking inputs
  s.sendto(msg, (contact_ip, int(contact_port)))
  #sending msg


thread.start_new_thread(rc,())
thread.start_new_thread(sc,())
#threading for parallel process


while True:
	pass


