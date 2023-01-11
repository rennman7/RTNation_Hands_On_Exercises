# A01 - rennman7  09-JAN-2023
# The instructor provided the following requirements.
#
# The application will be used to check if a port is open.
# Program will check for ports 80, 22, 443, 21.
# Each port will be checked by their own thread that makes the connection.
# Use single python file that uses threading to spawn a socket bind connection.
# Hint: Use a class. Reference the Person class that we created in the Classes video.
#
# Note. I did not use the bind method. However, the program still appears to work properly.
#
# Future updates
# 1. Add code that allows the user to input the IP address and port that need to be scanned
# 2. Add program usage message using argparse 

from threading import Thread
import time
import socket

# Global list variable containing the port nummbers that will be scanned.
port_list = [443, 80, 22, 21]

class Scan():
    def __init__(self, host, port):
        self.port = port
        self.host = host
        self.thread = Thread(target=self.check_port_status)
        self.thread.start()
    
    def check_port_status(self):
        # create an IPv4 socket object.
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)

        # attempt to connect to the specified port.
        try:
            sock.connect((self.host, self.port))
            sock.shutdown(2)
            if True:
                print("\nPort {0} is open".format(self.port))
        except:
            print("\nPort {0} is not open".format(self.port))


for i in port_list:
    p = i
    myscan = Scan('ENTER IP ADDRESS HERE', p)





