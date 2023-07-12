import serial
import serial.tools.list_ports
import time

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
            print("Didn't find any serial port")
            return None
        else:
            for i in range(0,len(port_list)):
                print(f"{i+1}. {port_list[i]}")
            while True:
                port_num = input("Please select the serial port：")
                if port_num.isdigit() and 0 < int(port_num) <= len(port_list):
                    port_num = int(port_num)
                    break
                else:
                    print("Input error, please re-enter")
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
        self.usbport = UsbPort()
        # self.ser = self.usbport.open_port(self.usbport.select_port())

    def send_data(self,ser, data):
        ser.write(data.encode())

    def receive_current(self):
        temp_voltage =""
        if self.ser.in_waiting:
            temp_voltage += self.ser.read(self.ser.in_waiting).decode("utf-8")
            current = self.convert_current_to_decimal(temp_voltage)
            return current
              
    def receive_voltage(self):
        temp_voltage =""
        if self.ser.in_waiting:
            temp_voltage += self.ser.read(self.ser.in_waiting).decode("utf-8")
            voltage = self.convert_voltage_to_decimal(temp_voltage)
            return voltage
        
    def first_received_data(self,port):
        self.ser = self.usbport.open_port(port)
        try:
            if self.ser.isOpen():
                    self.send_data(self.ser, "IOUT1?")
                    actual_voltage = self.receive_voltage()
                    time.sleep(0.5)
                    self.send_data(self.ser, "VOUT1?")
                    actual_current = self.receive_current()
                    time.sleep(0.5)
            else:
                print("Serial port is not open")
        except Exception as e:
            
    def received_data(self,port):
        self.ser = self.usbport.open_port(port)
        try:
            if self.ser.isOpen():
                # print("Serial port is open")
                VOLTAGE_FLAG = True
                for i in range(0,2):  # 2 times loop to receive voltage and current
                    if VOLTAGE_FLAG:
                        self.send_data(self.ser, "IOUT1?")
                        actual_voltage = self.receive_voltage()
                        # print("voltage:", actual_voltage)
                        time.sleep(0.5)
                        VOLTAGE_FLAG = False
                    else:
                        self.send_data(self.ser, "VOUT1?")
                        actual_current = self.receive_current()
                        # print("current:", actual_current)
                        time.sleep(0.5)
                        VOLTAGE_FLAG = True
                return actual_voltage, actual_current
                
            else:
                print("Serial port is not open")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if 'ser' in locals() or 'ser' in globals():
                self.usbport.close_port(self.ser)

    def stop_receive(self):
        self.usbport.close_port(self.ser)

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


if __name__ == "__main__":
    receive_data = ReceiveData()
    while True:
        voltage, current = receive_data.received_data()
        print(voltage, current)