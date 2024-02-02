#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 10:03:48 2022

@author: dq
"""

from socket import socket, AF_INET, SOCK_DGRAM

from pythonosc import udp_client
from pythonosc import osc_message_builder
from pythonosc.osc_message_builder import OscMessageBuilder

IP_server = '192.168.86.33'
PORT1 = 50001
PORT2 = 50002

# ソケットを用意
s1 = socket(AF_INET, SOCK_DGRAM)
s2 = socket(AF_INET, SOCK_DGRAM)

# バインドしておく
s1.bind((IP_server, PORT1))
s2.bind((IP_server, PORT2))

msg1 = s1.recv(15000)
print(msg1.decode('UTF-8'))

print("\n\n\n")
msg2 = s2.recv(15000)
print(msg2.decode('UTF-8'))

# ソケットを閉じる
s1.close()
s2.close()
