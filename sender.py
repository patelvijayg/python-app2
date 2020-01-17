#pip install pyserial
import  time
from commPortUtil import CommPort

def getCOMMPort(portname,baudrate,timeout,parity,rtscts):
   return CommPort(port=portname, baudrate=baudrate, timeout=timeout, parity=parity, rtscts=rtscts)

OUTPUT =getCOMMPort(r"\\.\CNCB0",9600,0,serial.PARITY_NONE,1)
INPUT =getCOMMPort(r"\\.\CNCA0",9600,0,serial.PARITY_NONE,1)
#INPUT = serial.Serial(r"\\.\CNCB0", 9600, timeout=0, parity=serial.PARITY_NONE, rtscts=1)
i=0
while i<3:
    message="datasent"+str(i)
    OUTPUT.writeData(message)
    time.sleep(1)
    bytes = INPUT.readData(20) #Read from Serial Port

    print( bytes)
    i=i+1;

OUTPUT.close()
INPUT.close()



