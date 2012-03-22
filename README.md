# addressInNetwork

Determine if a specified ip address is in the specified network.

## Usage

    # 192.168.0.1 is in 192.168.0.0/24
    $ addressInNetwork.py 192.168.0.1 192.168.0.0/24 
    $ echo $?
    0

    # 192.168.0.1 is in 192.168.0.0/255.255.255.0
    $ addressInNetwork.py 192.168.0.1 192.168.0.0/255.255.255.0
    $ echo $?
    0

    # 192.168.0.1 is _not_ in 192.168.1.0/24
    $ addressInNetwork.py 192.168.0.1 192.168.1.0/24
    $ echo $?
    1

    # 192.168.0.1 is _not_ in 192.168.1.0/255.255.255.0
    $ addressInNetwork.py 192.168.0.1 192.168.1.0/255.255.255.0
    $ echo $?
    1
