
import tkinter as tk
from tkinter import ttk, font as tkFont
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
import pandas as pd
import datetime
import time
import serial.tools.list_ports
# 其他需要的模块

class SerialApp:
    def __init__(self, master):
        self.master = master
        self.master.title("串口接收")
        self.master.geometry("800x600")  # 根据需要调整
        self.running = False
        self.data1 = []
        self.data2 = []
        self.data3 = []
        self.times = []
        self.ser = None  # 初始化串口
        self.fig = Figure(figsize=(5, 9), dpi=100)
        self.ax1 = self.fig.add_subplot(3, 1, 1)
        self.ax2 = self.fig.add_subplot(3, 1, 2)
        self.ax3 = self.fig.add_subplot(3, 1, 3)

        self.ax1.set_xlabel('Time (s)')
        self.ax1.set_ylabel('Voltage (V)')
        self.ax2.set_xlabel('Time (s)')
        self.ax2.set_ylabel('Current (A)')
        self.ax3.set_xlabel('Time (s)')
        self.ax3.set_ylabel('Power (mW)')

        ports = [port.device for port in serial.tools.list_ports.comports()]
        self.port_var = tk.StringVar()
        if ports:
            self.port_var.set(ports[0])
        tk.Label(self.master, text="Ports:").place(x=10, y=10)
        self.port_menu = ttk.OptionMenu(self.master, self.port_var, *ports)
        self.port_menu.place(x=100, y=10)

        self.start_button = ttk.Button(self.master, text="开始", command=self.start)
        self.start_button.place(x=10, y=40)

        tk.Label(self.master, text="Stop receive data:").place(x=10, y=70)
        self.stop_button = ttk.Button(self.master, text="停止", command=self.stop)
        self.stop_button.place(x=100, y=70)

        self.save_button = ttk.Button(self.master, text="保存", command=self.save)
        self.save_button.place(x=10, y=100)

        tk.Label(self.master, text="Save data form:").place(x=10, y=130)
        self.format_var = tk.StringVar()
        self.format_var.set("txt")
        self.format_menu = ttk.OptionMenu(self.master, self.format_var, "txt", "csv", "excel")
        self.format_menu.place(x=100, y=130)

        tk.Label(self.master, text="Receive data period:").place(x=10, y=160)
        self.interval_var = tk.StringVar()
        self.interval_var.set("1")
        self.interval_menu = ttk.OptionMenu(self.master, self.interval_var, *[str(i) for i in range(1, 11)])
        self.interval_menu.place(x=100, y=160)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=10, y=190, width=370, height=400)

        ft = tkFont.Font(family='Times',size=10)
        self.text = tk.Listbox(self.master, font=ft, borderwidth=1, fg="#333333", justify="center")
        self.text.place(x=380, y=10, width=236, height=584)
