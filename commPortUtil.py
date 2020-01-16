import serial

class CommPort(object):
    """\
    Commport class will be use for All the comm port communication
    """
    def __init__(self,port,baudrate,timeout,parity,rtscts):
        self.port=port
        self.baudrate=baudrate
        self.timeout=timeout
        self.parity=parity
        self.rtscts=rtscts
        self._commport=serial.Serial(port=self.port, baudrate=self.baudrate, timeout=self.timeout, parity=self.parity, rtscts=self.rtscts)

    def writeData(self,data):
        cp=self._commport
        if cp.is_open:
            cp.write(data.encode())

    def readData(self,size=100):
        cp=self._commport
        if cp.is_open:
            return cp.read(size).decode()
        else:
            raise serial.SerialException('Attempting to use a port that is not open')

    def close(self):
        self._commport.close()