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
        GListBox_468.place(x=530,y=10,width=240,height=880)

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
        GButton_234["text"] = "Button"
        GButton_234.place(x=120,y=30,width=160,height=55)
        GButton_234["command"] = self.GButton_234_command

        GButton_111=tk.Button(root)
        GButton_111["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_111["font"] = ft
        GButton_111["fg"] = "#000000"
        GButton_111["justify"] = "center"
        GButton_111["text"] = "Button"
        GButton_111.place(x=300,y=30,width=160,height=55)
        GButton_111["command"] = self.GButton_111_command

        GButton_430=tk.Button(root)
        GButton_430["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_430["font"] = ft
        GButton_430["fg"] = "#000000"
        GButton_430["justify"] = "center"
        GButton_430["text"] = "Button"
        GButton_430.place(x=300,y=110,width=160,height=55)
        GButton_430["command"] = self.GButton_430_command

        GLabel_394=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_394["font"] = ft
        GLabel_394["fg"] = "#333333"
        GLabel_394["justify"] = "center"
        GLabel_394["text"] = "label"
        GLabel_394.place(x=20,y=50,width=70,height=25)

        GLabel_248=tk.Label(root)
        GLabel_248["anchor"] = "center"
        GLabel_248["cursor"] = "spider"
        ft = tkFont.Font(family='Times',size=18)
        GLabel_248["font"] = ft
        GLabel_248["fg"] = "#333333"
        GLabel_248["justify"] = "center"
        GLabel_248["text"] = "label"
        GLabel_248.place(x=70,y=130,width=70,height=25)

        GLabel_420=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_420["font"] = ft
        GLabel_420["fg"] = "#333333"
        GLabel_420["justify"] = "center"
        GLabel_420["text"] = "label"
        GLabel_420.place(x=170,y=130,width=70,height=25)

    def GButton_234_command(self):
        print("command")


    def GButton_111_command(self):
        print("command")


    def GButton_430_command(self):
        print("command")

class Settext:
    

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
