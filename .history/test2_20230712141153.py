
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk, font as tkFont
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
import pandas as pd
import datetime
import time
import serial.tools.list_ports
from matplotlib.ticker import FuncFormatter
from ReceiveData import ReceiveData

# 其他需要的模块

class SerialApp:
    def __init__(self, master):
        self.receivedata = ReceiveData()
        self.master = master
        self.master.title("ADCS VOltage Current Power Monitor")
        width=780
        height=900
        screenwidth = master.winfo_screenwidth()
        screenheight = master.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        master.geometry(alignstr)
        master.resizable(width=False, height=False)

        self.running = False
        self.pause = False
        self.voltage = []
        self.current = []
        self.power = []
        self.times = []
        self.ser = None  # 初始化串口
        self.fig = Figure(figsize=(5, 9), dpi=100)
        self.ax1 = self.fig.add_subplot(3, 1, 1)
        self.ax2 = self.fig.add_subplot(3, 1, 2)
        self.ax3 = self.fig.add_subplot(3, 1, 3)

        self.ax1.set_ylabel('Voltage (V)')
        self.ax1.yaxis.set_label_position("right")
        self.ax2.set_ylabel('Current (A)')
        self.ax2.yaxis.set_label_position("right")
        self.ax3.set_ylabel('Power (mW)')
        self.ax3.yaxis.set_label_position("right")
        self.ax3.set_xlabel('Time (s)')
        
        formatter = FuncFormatter(self.two_decimal)

        self.ax1.yaxis.set_major_formatter(formatter)
        self.ax2.yaxis.set_major_formatter(formatter)
        self.ax3.yaxis.set_major_formatter(formatter)

        #port menu
        ports = [port.device for port in serial.tools.list_ports.comports()]
        self.port_var = tk.StringVar()
        if ports:
            self.port_var.set(ports[0])
        port_menu = tk.OptionMenu(self.master, self.port_var, *ports)
        port_menu.place(x=30, y=40, width=140, height=55)
        helv36 = tkFont.Font(family='Times', size=10)
        port_menu.config(font=helv36)

        # start button
        GButton_234=tk.Button(master)
        GButton_234["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_234["font"] = ft
        GButton_234["fg"] = "#000000"
        GButton_234["justify"] = "center"
        GButton_234["text"] = "Start"
        GButton_234.place(x=30,y=110,width=105,height=55)
        GButton_234["command"] = self.start

        # stop button
        GButton_111=tk.Button(master)
        GButton_111["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_111["font"] = ft
        GButton_111["fg"] = "#000000"
        GButton_111["justify"] = "center"
        GButton_111["text"] = "Stop"
        GButton_111.place(x=150,y=110,width=105,height=55)
        GButton_111["command"] = self.stop
        
        # save button
        GButton_430=tk.Button(master)
        GButton_430["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_430["font"] = ft
        GButton_430["fg"] = "#000000"
        GButton_430["justify"] = "center"
        GButton_430["text"] = "Continue"
        GButton_430.place(x=270,y=110,width=105,height=55)
        GButton_430["command"] = self.cotinue

        GButton_931=tk.Button(master)
        GButton_931["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_931["font"] = ft
        GButton_931["fg"] = "#000000"
        GButton_931["justify"] = "center"
        GButton_931["text"] = "Save"
        GButton_931.place(x=390,y=110,width=105,height=55)
        GButton_931["command"] = self.save

        # time voltage current power label
        GMessage_48=tk.Label(master)
        ft = tkFont.Font(family='Times',size=15)
        GMessage_48["font"] = ft
        GMessage_48["fg"] = "#333333"
        GMessage_48["justify"] = "center"
        GMessage_48["text"] = "Time Voltage Current Power"
        GMessage_48.place(x=530,y=50,width=236,height=34)

        # format menu for setting the format of the saved data
        self.format_var = tk.StringVar()
        self.format_var.set("txt")
        self.format_menu = tk.OptionMenu(self.master, self.format_var, "txt", "csv", "excel")
        self.format_menu.place(x=190, y=40, width=140, height=55)
        helv36 = tkFont.Font(family='Times', size=10)
        self.format_menu.config(font=helv36)

        # interval menu for setting the interval of data collection
        self.interval_var = tk.StringVar()
        self.interval_var.set("1")
        self.interval_menu = tk.OptionMenu(self.master, self.interval_var, *[str(i) for i in range(1, 11)])
        self.interval_menu.place(x=350,y=40,width=149,height=55)
        helv36 = tkFont.Font(family='Times', size=10)
        self.interval_menu.config(font=helv36)

        # canvas for drawing the plot
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=10, y=190, width=500, height=700)


        self.text = tk.Text(self.master, height=50, width=30)
        self.text.place(x=520, y=90, width=236, height=800)

        
        self.notelabel=tk.Label(self.master)
        # set Font color to rad
        self.notelabel["justify"] = "left"
        ft = tkFont.Font(family='Times',size=15,weight=tkFont.BOLD,slant=tkFont.ITALIC)
        self.notelabel["font"] = ft
        self.notelabel["fg"] = "red"
        self.notelabel["text"] = "Warning: Make sure the device is connected !"
        self.notelabel.place(x=10,y=180,width=500,height=57)


    def start(self):
        if self.ser is not None:
            self.ser.close()
            self.running = False
            if self.t.is_alive():
                print("alive")
            else:   
                print("not alive")

        self.port = self.port_var.get()
        while self.port == "COM5" or self.port == "COM6":
            self.notelabel["text"] = "Please select a port correctly !"
            # self.port = self.port_var.get()
            # continue
        self.notelabel["text"] = "Connected with " + self.port + " with save format " + self.format_var.get() + " and preiod " + self.interval_var.get() + "s"
        self.interval = int(self.interval_var.get())
        # 打开串口
        self.running = True
        self.t = threading.Thread(target=self.receive_data)
        if self.t.is_alive():
            print("alive")
        else:   
            print("not alive")
        self.t.start()
        if self.t.is_alive():
            print("alive")
        else:   
            print("not alive")

    def stop(self):
        self.pause = True
    
    def cotinue(self):
        self.pause = False
        # threading.Thread(target=self.receive_data).start()

    def save(self):
        if self.format_var.get() == "txt":
            with open('output.txt', 'w') as f:
                f.write("time\tvoltage\tcurrent\tpower\n")
                for time, voltage, current, power in zip(self.times, self.voltage, self.current, self.power):
                    f.write(f"{time:.2f}\t{voltage:.2f}\t{current:.3f}\t{power:.3f}\n")
        elif self.format_var.get() == "csv":
            with open('output.csv', 'w') as f:
                f.write("time,voltage,current,power\n")
                for time, voltage, current, power in zip(self.times, self.voltage, self.current, self.power):
                    f.write(f"{time:.2f}\t{voltage:.2f}\t{current:.3f}\t{power:.3f}\n")
        elif self.format_var.get() == "excel":
            df = pd.DataFrame({"time": self.times, "voltage": self.voltage, "current": self.current, "power": self.power})
            df.to_excel("output.xlsx", index=False)
        

    def receive_data(self):
        self.start_time = time.time()
        while self.running:
            if self.pause:
                continue
            # voltage, current, power = 0.01, 1.04, 2.45  # example data
            voltage, current = self.receivedata.received_data(self.port_var.get())
            if voltage is None or current is None:
                self.notelabel["text"] = "Error: Make sure the device is opened !"
                continue
            else:   
                self.notelabel["text"] = "Connected with " + self.port + " with save format "+ self.format_var.get() + " and preiod " + self.interval_var.get() + "s"
            # print(voltage, current)
            power =voltage*current
            self.voltage.append(voltage)
            self.current.append(current)
            self.power.append(power)
            self.times.append(time.time() - self.start_time)
            self.ax1.plot(self.times, self.voltage, 'r-')
            self.ax2.plot(self.times, self.current, 'g-')
            self.ax3.plot(self.times, self.power, 'b-')
            self.canvas.draw()

            # 更新Text部件的内容
            self.text.delete('1.0', tk.END)
            self.text.insert(tk.END, "\n".join([f"{t:.2f}s: {d1:.2f}V, {d2:.3f}A, {d3:.3f}mW" for t, d1, d2, d3 in zip(self.times[-60:], self.voltage[-60:], self.current[-60:], self.power[-60:])]))

            time.sleep(self.interval-1)  # using 1 second to receive data 
        
        

    def two_decimal(self,x,pos):
        'The two arguments are the value and tick position'
        return '%.3f' % x

if __name__ == "__main__":
    root = tk.Tk()
    app = SerialApp(root)
    root.mainloop()