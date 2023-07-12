import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=780
        height=900
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GListBox_468=tk.Listbox(root)
        GListBox_468["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_468["font"] = ft
        GListBox_468["fg"] = "#333333"
        GListBox_468["justify"] = "center"
        GListBox_468.place(x=530,y=90,width=236,height=800)

        GListBox_560=tk.Listbox(root)
        GListBox_560["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_560["font"] = ft
        GListBox_560["fg"] = "#333333"
        GListBox_560["justify"] = "center"
        GListBox_560.place(x=20,y=190,width=500,height=700)

        GButton_234=tk.Button(root)
        GButton_234["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_234["font"] = ft
        GButton_234["fg"] = "#000000"
        GButton_234["justify"] = "center"
        GButton_234["text"] = "Button4"
        GButton_234.place(x=30,y=110,width=105,height=55)
        GButton_234["command"] = self.GButton_234_command

        GButton_111=tk.Button(root)
        GButton_111["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_111["font"] = ft
        GButton_111["fg"] = "#000000"
        GButton_111["justify"] = "center"
        GButton_111["text"] = "Button3"
        GButton_111.place(x=350,y=40,width=149,height=55)
        GButton_111["command"] = self.GButton_111_command

        GButton_430=tk.Button(root)
        GButton_430["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_430["font"] = ft
        GButton_430["fg"] = "#000000"
        GButton_430["justify"] = "center"
        GButton_430["text"] = "Button5"
        GButton_430.place(x=150,y=110,width=105,height=55)
        GButton_430["command"] = self.GButton_430_command

        GMessage_48=tk.Message(root)
        ft = tkFont.Font(family='Times',size=16)
        GMessage_48["font"] = ft
        GMessage_48["fg"] = "#333333"
        GMessage_48["justify"] = "center"
        GMessage_48["text"] = "Time Voltage Current Power"
        GMessage_48.place(x=530,y=50,width=236,height=34)

        GButton_85=tk.Button(root)
        GButton_85["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_85["font"] = ft
        GButton_85["fg"] = "#000000"
        GButton_85["justify"] = "center"
        GButton_85["text"] = "Button1"
        GButton_85.place(x=30,y=40,width=140,height=55)
        GButton_85["command"] = self.GButton_85_command

        GButton_934=tk.Button(root)
        GButton_934["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_934["font"] = ft
        GButton_934["fg"] = "#000000"
        GButton_934["justify"] = "center"
        GButton_934["text"] = "Button2"
        GButton_934.place(x=190,y=40,width=140,height=55)
        GButton_934["command"] = self.GButton_934_command

        GButton_525=tk.Button(root)
        GButton_525["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_525["font"] = ft
        GButton_525["fg"] = "#000000"
        GButton_525["justify"] = "center"
        GButton_525["text"] = "Button6"
        GButton_525.place(x=270,y=110,width=105,height=55)
        GButton_525["command"] = self.GButton_525_command

        GButton_931=tk.Button(root)
        GButton_931["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_931["font"] = ft
        GButton_931["fg"] = "#000000"
        GButton_931["justify"] = "center"
        GButton_931["text"] = "Button7"
        GButton_931.place(x=390,y=110,width=105,height=55)
        GButton_931["command"] = self.GButton_931_command

        GMessage_689=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_689["font"] = ft
        GMessage_689["fg"] = "#333333"
        GMessage_689["justify"] = "left"
        GMessage_689["text"] = "Message"
        GMessage_689.place(x=20,y=180,width=501,height=57)

    def GButton_234_command(self):
        print("command")


    def GButton_111_command(self):
        print("command")


    def GButton_430_command(self):
        print("command")


    def GButton_85_command(self):
        print("command")


    def GButton_934_command(self):
        print("command")


    def GButton_525_command(self):
        print("command")


    def GButton_931_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
