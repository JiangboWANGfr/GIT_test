
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
        self.master.title("ADCS VOltage Current Power Monitor")
        width=780
        height=900
        screenwidth = master.winfo_screenwidth()
        screenheight = master.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        master.geometry(alignstr)
        master.resizable(width=False, height=False)

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

        self.ax1.set_ylabel('Voltage (V)')
        self.ax2.set_ylabel('Current (A)')
        self.ax3.set_xlabel('Time (s)')
        self.ax3.set_ylabel('Power (mW)')

        ports = [port.device for port in serial.tools.list_ports.comports()]
        self.port_var = tk.StringVar()
        if ports:
            self.port_var.set(ports[0])

        self.port_menu = ttk.OptionMenu(self.master, self.port_var, *ports)
        ft = tkFont.Font(family='Times',size=10)
         self.port_menu["font"] = ft
         self.port_menu["fg"] = "#333333"
         self.port_menu["justify"] = "center"
        self.port_menu.place(x=100, y=10)

        self.start_button = ttk.Button(self.master, text="Start", command=self.start)
        self.start_button.place(x=10, y=40)

        self.stop_button = ttk.Button(self.master, text="Stop", command=self.stop)
        self.stop_button.place(x=100, y=70)

        self.save_button = ttk.Button(self.master, text="保存", command=self.save)
        self.save_button.place(x=10, y=100)

        self.format_var = tk.StringVar()
        self.format_var.set("txt")
        self.format_menu = ttk.OptionMenu(self.master, self.format_var, "txt", "csv", "excel")
        self.format_menu.place(x=100, y=130)

        self.interval_var = tk.StringVar()
        self.interval_var.set("1")
        self.interval_menu = ttk.OptionMenu(self.master, self.interval_var, *[str(i) for i in range(1, 11)])
        self.interval_menu.place(x=100, y=160)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=10, y=190, width=500, height=700)


        self.text = tk.Text(self.master, height=50, width=30)
        self.text.place(x=520, y=10, width=236, height=1100)

    def start(self):
        self.port = self.port_var.get()
        self.interval = int(self.interval_var.get())
        # 打开串口
        self.running = True
        threading.Thread(target=self.receive_data).start()

    def stop(self):
        self.running = False
        if self.ser is not None:
            # 关闭串口
            pass

    def save(self):
        if self.format_var.get() == "txt":
            with open('output.txt', 'w') as f:
                for t, d in zip(self.times, self.data):
                    f.write(f"{t} - {d}\n")
        elif self.format_var.get() == "csv":
            df = pd.DataFrame({"Time": self.times, "Data": self.data})
            df.to_csv('output.csv', index=False)
        elif self.format_var.get() == "excel":
            df = pd.DataFrame({"Time": self.times, "Data": self.data})
            df.to_excel('output.xlsx', index=False)

    def receive_data(self):
        self.start_time = time.time()
        while self.running:
            # 从串口读取数据
            data1, data2, data3 = 0, 1, 1  # 假设读到的数据为0
            self.data1.append(data1)
            self.data2.append(data2)
            self.data3.append(data3)
            self.times.append(time.time() - self.start_time)
            self.ax1.plot(self.times, self.data1, 'r-')
            self.ax2.plot(self.times, self.data2, 'g-')
            self.ax3.plot(self.times, self.data3, 'b-')
            self.canvas.draw()

            # 更新Text部件的内容
            self.text.delete('1.0', tk.END)
            self.text.insert(tk.END, "\n".join([f"{t:.2f}s: {d1:.2f}V, {d2:.2f}A, {d3:.2f}mW" for t, d1, d2, d3 in zip(self.times[-53:], self.data1[-53:], self.data2[-53:], self.data3[-53:])]))
            
            time.sleep(self.interval)

def main():
    root = tk.Tk()
    app = SerialApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
