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
            print("未发现串口!")
            return None
        else:
            for i in range(0,len(port_list)):
                print(f"{i+1}. {port_list[i]}")
            while True:
                port_num = input("请选择需要的串口号：")
                if port_num.isdigit() and 0 < int(port_num) <= len(port_list):
                    port_num = int(port_num)
                    break
                else:
                    print("输入错误，请重新输入!")
            return str(port_list[port_num-1].device)
    
    def open_port(self,port):
        ser = serial.Serial(port, baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
        return ser

    def close_port(ser):
        ser.close()


class ReceiveData:
    def __init__(self):
        self.current = None
        self.voltage = None
        self.port = 

    def send_data(self,ser, data):
        ser.write(data.encode())

    def receive_current(self,ser):
        temp_voltage =""
        if ser.in_waiting:
            temp_voltage += ser.read(ser.in_waiting).decode("utf-8")
            current = convert_current_to_decimal(temp_voltage)

        return current
              
    def receive_voltage(self,ser):
        self.send_data(ser, "VSET1?")
        temp_voltage =""
        if ser.in_waiting:
            temp_voltage += ser.read(ser.in_waiting).decode("utf-8")
            data_v = convert_voltage_to_decimal(temp_voltage)
            return data_v



def convert_voltage_to_decimal(data):
    try:
        decimal_value = float(data.replace(".", ""))
        return decimal_value / 100
    except ValueError:
        return None
    
def convert_current_to_decimal(data):
    try:
        decimal_value = float(data.replace(".", ""))
        return decimal_value / 1000
    except ValueError:
        return None
