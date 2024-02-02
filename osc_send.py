#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 15:55:36 2022

@author: dq
"""


from socket import socket, AF_INET, SOCK_DGRAM

from pythonosc import udp_client
from pythonosc import osc_message_builder
# from pythonosc.osc_message_builder import OscMessageBuilder



if __name__ == "__main__":
    IP_server = '192.168.86.33'
    PORT1 = 50001   # 推奨：49152~65535
    PORT2 = 50002   

    client_0 = udp_client.UDPClient(IP_server,PORT1)
    client_1 = udp_client.UDPClient(IP_server,PORT2)

    msg1 = "Hello"
    msg2 = "World"

    m1 = osc_message_builder.OscMessageBuilder(address='/msg_1')
    m1.add_arg(msg1)
    m1 = m1.build()

    m2 = osc_message_builder.OscMessageBuilder(address='/msg_2')
    m2.add_arg(msg2)
    m2 = m2.build()

    client_0.send(m1)
    client_1.send(m2)

 