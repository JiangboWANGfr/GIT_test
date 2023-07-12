import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
import pandas as pd
import datetime
import time
# 其他需要的模块

class SerialApp:
    def __init__(self, master):
        self.master = master
        self.master.title("串口接收")
        self.running = False
        self.data = []
        self.times = []
        self.ser = None  # 初始化串口
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(1, 1, 1)

        self.port_label = ttk.Label(self.master, text="Port:")
        self.port_entry = ttk.Entry(self.master)
        self.port_label.grid(row=0, column=0)
        self.port_entry.grid(row=0, column=1)

        self.start_button = ttk.Button(self.master, text="开始", command=self.start)
        self.start_button.grid(row=1, column=0)

        self.stop_button = ttk.Button(self.master, text="停止", command=self.stop)
        self.stop_button.grid(row=1, column=1)

        self.save_button = ttk.Button(self.master, text="保存", command=self.save)
        self.save_button.grid(row=2, column=0)

        self.format_var = tk.StringVar()
        self.format_var.set("txt")
        self.format_menu = ttk.OptionMenu(self.master, self.format_var, "txt", "csv", "excel")
        self.format_menu.grid(row=2, column=1)

        self.interval_var = tk.StringVar()
        self.interval_var.set("1")
        self.interval_menu = ttk.OptionMenu(self.master, self.interval_var, *[str(i) for i in range(1, 11)])
        self.interval_menu.grid(row=3, column=0)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=4, column=0, columnspan=2)

    def start(self):
        self.port = self.port_entry.get()
        self.interval = int(self.interval_var.get())
        # 打开串口
        self.running = True
        threading.Thread(target=self.receive_data).start()

    def stop(self):
        self.running = False
        if self.ser is not None:
            # 关闭串口

    def save(self):
        # ... 与之前的函数相同
        

    def receive_data(self):
        self.start_time = time.time()
        while self.running:
            # 从串口读取数据
            data = 0  # 假设读到的数据为0
            self.data.append(data)
            self.times.append(time.time() - self.start_time)
            self.ax.plot(self.times, self.data, 'r-')
            self.canvas.draw()
            time.sleep(self.interval)

def main():
    root = tk.Tk()
    app = SerialApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
