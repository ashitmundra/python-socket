#!/usr/bin/python
import socket
import thread
import os
import espeak
#importing libraries
rec_ip="192.168.43.253"
myport=8888
#own ip hosting details
contact_ip=raw_input("Enter Contact IP address: ")
contact_port=raw_input("Enter contact port: ")
#taking contact ip details
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((rec_ip, myport))
#socket binding for udp
name=raw_input("Enter your name:   ")
#entering your name
contact_name=s.recvfrom(100)
#recieving contact name
s.sendto(name, (contact_ip, int(contact_port)))
def snd():
 #sending function
 while True:
  send=raw_input()
  s.sendto(send, (contact_ip, int(contact_port)))
def rce():
 #recieving function
 while True:
  msg=s.recvfrom(1000)
  print (contact_name[0]+":" +msg[0])
  #printing message

thread.start_new_thread(snd,())
thread.start_new_thread(rce,())
#threading for parallel process


while True:
  pass
