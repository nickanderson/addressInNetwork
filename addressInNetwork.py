#!/usr/bin/env python
# encoding: utf-8
author="Nick Anderson"
email="nick@cmdln.org"
url="http://www.github.com/nickanderson/addressInNetwork"
desc="""This script will exit with 0 if a given ip is in the given network
range, and will return 1 if it is not """



import sys
import socket,struct
from optparse import OptionParser

# addressInNetwork and calcDottedNetmaks (the important bits) shamelessly
# swiped from Nitin Khanna http://stackoverflow.com/a/5467511
def addressInNetwork(ip,net):
    '''This function allows you to check if on IP belogs to a Network'''
    ipaddr = struct.unpack('=L',socket.inet_aton(ip))[0]
    netaddr,bits = net.split('/')

    # Here we expect a cidr formatted network, if it fails we then assume a
    # dotted netmask was provided and try to use that, if we still fail, we
    # give up.
    try:
        netmask = struct.unpack('=L',socket.inet_aton(calcDottedNetmask(int(bits))))[0]
    except ValueError:
        try:
            netmask = struct.unpack('=L',socket.inet_aton(bits))[0]
        except:
            print "Something went wrong, probably you provided some poorly formed ip address or netmask."
            sys.exit(1)

    network = struct.unpack('=L',socket.inet_aton(netaddr))[0] & netmask
    return (ipaddr & netmask) == (network & netmask)

def calcDottedNetmask(mask):
    bits = 0
    for i in xrange(32-mask,32):
        bits |= (1 << i)
    return "%d.%d.%d.%d" % ((bits & 0xff000000) >> 24, (bits & 0xff0000) >> 16, (bits & 0xff00) >> 8 , (bits & 0xff))

if __name__=="__main__":
    parser = OptionParser(usage='Usage: %prog ip network/[bits|dottednetmask]', description=desc)
    (options, args) = parser.parse_args()
    if not len(args) == 2:
        parser.print_help()
        sys.exit(1)
    if addressInNetwork(args[0], args[1]):
        sys.exit(0)
    else:
        sys.exit(1)
