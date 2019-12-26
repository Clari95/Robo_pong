#!/usr/bin/env python
#  
import socket 
import struct
import time

class TCPClient:

    def __init__(self):
        # specify server IP
        self.TCP_IP = '10.38.236.84'           # ITRI PC: WLAN receiver IP
        # TCP_IP = '10.38.197.195'          # Jakobs wlan ip
        # TCP_IP = '127.0.0.1'              # Standard loopback interface address (localhost)

        # Port to listen on (non-privileged ports are > 1023)
        self.TCP_PORT = 27015                  # ITRI PC
        # TCP_PORT = 5005                   # Jakob Laptop

        self.BUFFER_SIZE = 4
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        print('start connect ...')
        self.s.connect((self.TCP_IP, self.TCP_PORT))
        print('connection successful.')

    def close(self):
        self.s.close()

    
    def send_message(self,MESSAGE):

        # create list of bytes
        B_MESSAGE = []
        for number in MESSAGE:
            number = float(number)
            B_MESSAGE.append(bytearray(struct.pack("f", number)))

        for byte_array in B_MESSAGE:
            self.s.send(byte_array)
            #print('sent {}'.format(byte_array))

    # TODO: code that recieves robot coordinate as 3 point array
    # def recieve_message(self):
    #     data = "data"
    #     while data is not None:
    #         data = self.s.recv(self.BUFFER_SIZE)
    #         print("received data:", repr(data))
    #     return data
        

def main():
    client = TCPClient()
    DEFAULT_MESSAGE = [200.0, 400.0, 50.0]
    client.send_message(DEFAULT_MESSAGE)


if __name__ == '__main__':
    main()