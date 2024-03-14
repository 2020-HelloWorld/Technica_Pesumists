from scapy.all import *

from time import *



# function to modify timing information in TCP packet

def modify_timing(pkt, bit):

    # set last bit of time field to bit value

    if bit:

        sleep(0.15)

    send(pkt)



# function to send TCP packet with covert bit

def send_packet(covert_bit,data,c):

    # create TCP packet with payload of normal data

    #Sending 1000 bytes of data

    send_data = "".join(data[c:c+1000])

    pkt = IP(dst="10.0.2.5")/UDP(dport=8080)/send_data

    # modify timing information with covert bit

    modify_timing(pkt, covert_bit)

    c += 1

    return c





# covert info to be transmitted

covert_info = "This is covert info"

# convert covert info to bit stream

covert_bits = [int(b) for b in ''.join(format(ord(c), '08b') for c in covert_info)]

covert_bits.insert(0,0)

print(covert_bits)



normal_data = """

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

This is normal data.

"""

data = list(normal_data)



# loop through covert bit stream and send packets

c = 0

for bit in covert_bits:

	c = send_packet(bit,data,c)
