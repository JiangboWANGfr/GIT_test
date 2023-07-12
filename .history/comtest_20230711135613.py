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

def receive_data(ser):
    while True:
        if ser.in_waiting:
            data = ser.read().decode("utf-8")
            return data

def main():
    port = select_port()
    if port is not None:
        try:
            ser = open_port(port)
            if ser.isOpen():
                print("串口已打开")
                data = input("请输入需要发送的数据：")
                send_data(ser, data)
                print("数据已发送，等待接收数据...")
                while True:
                    if ser.in_waiting:
                         print("接收的数据为：", receive_data(ser))
            else:
                print("串口未打开")
        except Exception as e:
            print(f"打开串口失败，错误信息：{e}")
        finally:
            if 'ser' in locals() or 'ser' in globals():
                close_port(ser)

if __name__ == "__main__":
    main()
