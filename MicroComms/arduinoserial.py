from asyncio.timeouts import timeout
import serial  
import time 

arduino=serial.Serial(
port = '/dev/tty**',
baudrate = 115200,
bytesize = serial.PARITY_NONE,
stopbits = serial.STOPBITS_ONE,
timeout = 5,
xonxoff = False,
rtscts = False,
dsrdtr = False,
writeTimeout = 2
)

while True:
    try: 
        arduino.write("Command from Jetson|".enconde())
        data = 