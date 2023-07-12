import time
def receive_data(self):
    self.start_time = time.time()
    while self.running:
        while self.running and not self.pause:
            try:
                # voltage, current, power = 0.01, 1.04, 2.45  # example data
                voltage, current = self.receivedata.received_data(self.port_var.get())
                if voltage is None or current is None:
                    self.master.after(0, self.update_notelabel, "Warning: Make sure the device is connected !")
                    continue
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
            except Exception as e:
                print("Error while receiving data:", e)
        time.sleep(0.1)  # prevent the loop from running too fast when paused

def start(self):
    self.GButton_234["text"] = "Restart"
    self.clear()
    self.running = True

def stop(self):
    self.running = False

def cotinue(self):
    self.running = True

def clear(self):
    self.start_time = time.time()
   
    # clear the plot
    self.ax1.clear()
    self.ax2.clear()
    self.ax3.clear()
    self.voltage = []
    self.current = []
    self.power = []
    self.times = []
    # clear the text
    self.text.delete('1.0', tk.END)

    self.port = self.port_var.get()
    self.interval = int(self.interval_var.get())
    self.running = True
    self.paused = False
