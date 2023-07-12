import serial
import serial.tools.list_ports

class UsbPort:
    def __init__(self):
        self.port = None
        self.ser = None
        self.data = None
        self.current = None
        self.voltage = None
    def select_port(self):
        port_list = list(serial.tools.list_ports.comports())
        if len(port_list) <= 0:
            print("ERROR!")
            return None
        else:   
            return str(port_list[0].device)
    
    def open_port(self,port):
        ser = serial.Serial(port, baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
        return ser

    def close_port(ser):
        ser.close()


class ReceiveData:
    def __init__(self):
        self.current = None
        self.voltage = None
        self.usbport = UsbPort()
        self.ser = self.usbport.open_port(self.usbport.select_port())

    def send_data(self,ser, data):
        ser.write(data.encode())

    def receive_current(self):
        self.send_data(self.ser, "ISET1?")
        temp_voltage =""
        if self.ser.in_waiting:
            temp_voltage += self.ser.read(self.ser.in_waiting).decode("utf-8")
            current = self.convert_current_to_decimal(temp_voltage)

        return current
              
    def receive_voltage(self):
        self.send_data(self.ser, "VSET1?")
        temp_voltage =""
        if self.ser.in_waiting:
            temp_voltage += self.ser.read(self.ser.in_waiting).decode("utf-8")
            data_v = convert_voltage_to_decimal(temp_voltage)
            return data_v



    def convert_voltage_to_decimal(self,data):
        try:
            decimal_value = float(data.replace(".", ""))
            return decimal_value / 100
        except ValueError:
            return None
        
    def convert_current_to_decimal(self,data):
        try:
            decimal_value = float(data.replace(".", ""))
            return decimal_value / 1000
        except ValueError:
            return None
