import time
import serial
import serial.tools.list_ports

def select_port():
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

def open_port(port):
    ser = serial.Serial(port, baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
    return ser

def close_port(ser):
    ser.close()

def send_data(ser, data):
    ser.write(data.encode())

def receive_current(ser):
    temp_voltage =""
    if ser.in_waiting:
        temp_voltage += ser.read(ser.in_waiting).decode("utf-8")
        current = convert_current_to_decimal(temp_voltage)
        # print("in_waiting:", ser.in_waiting)
        # print("接收到的数据：", temp_voltage)
        # print("电压值为：", current)
        return current
    
def receive_voltage(ser):
    temp_voltage =""
    if ser.in_waiting:
        temp_voltage += ser.read(ser.in_waiting).decode("utf-8")
        voltage = convert_voltage_to_decimal(temp_voltage)
        # print("接收到的数据：", temp_voltage)
        # print("电压值为：", voltage)
        return voltage

def received_data(ser):

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

def main():
    port = select_port()
    if port is not None:
        try:
            ser = open_port(port)
            if ser.isOpen():
                print("串口已打开")
                # send_data(ser, "VSET1?")
                # print("voltage comment send.")    
                # decimal_value = receive_voltage(ser)
                # print("voltage:", decimal_value)
                # time.sleep(2)
                VOLTAGE_FLAG = True
                while True:
                    if VOLTAGE_FLAG:
                        send_data(ser, "VOUT1?")
                        decimal_value = receive_voltage(ser)
                        print("voltage:", decimal_value)
                        time.sleep(0.5)
                        VOLTAGE_FLAG = False
                    else:
                        send_data(ser, "IOUT1?")
                        decimal_value = receive_current(ser)
                        print("current:", decimal_value)
                        time.sleep(0.5)
                        VOLTAGE_FLAG = True


            else:
                print("串口未打开")
        except Exception as e:
            print(f"打开串口失败，错误信息：{e}")
        finally:
            if 'ser' in locals() or 'ser' in globals():
                close_port(ser)

if __name__ == "__main__":
    main()
