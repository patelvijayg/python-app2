import threading
import time
import serial

class ReceiveCommPort (threading.Thread):

    def __init__(self, port,baudrate,timeout,parity,rtscts):
        print("constructor")
        threading.Thread.__init__(self)
        self.name = "one"
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.parity = parity
        self.rtscts = rtscts
        self._commport = serial.Serial(port=self.port, baudrate=self.baudrate, timeout=self.timeout, parity=self.parity, rtscts=self.rtscts)

    def start_reading(self):
        print("reading")
        self.start_received=True

    def stop_reading(self):
        print("stop")
        self.start_received=False

    def run(self):
        print("run")
        self.listening()

    def destroy(self):
        print("destroy")
        self.join()

    def listening(self):
        print("listen")
        cp = self._commport
        while self.start_received:
            if cp.is_open:
                data=cp.read(100).decode()
                if data !='':
                    print(data,sep='\n')
            time.sleep(1)