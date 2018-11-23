#!/usr/bin/python

#import sys
#import socket
#
#host=str(sys.argv[1])
#
#result=socket.gethostbyaddr(host)
#
#print(result[0])

import sys
import datetime
import socket

modulename = 'sys'
if modulename not in sys.modules:
    print('You have not imported the {} module'.format(modulename))

ip = "8.8.8.8"

domain = (socket.gethostbyaddr(ip))

print(domain[0])
