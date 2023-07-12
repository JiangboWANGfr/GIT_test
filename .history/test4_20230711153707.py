import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=672
        height=880
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_125=tk.Button(root)
        GButton_125["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_125["font"] = ft
        GButton_125["fg"] = "#d92424"
        GButton_125["justify"] = "center"
        GButton_125["text"] = "Button"
        GButton_125.place(x=380,y=50,width=179,height=52)
        GButton_125["command"] = self.GButton_125_command

        GCheckBox_428=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_428["font"] = ft
        GCheckBox_428["fg"] = "#333333"
        GCheckBox_428["justify"] = "center"
        GCheckBox_428["text"] = "CheckBox"
        GCheckBox_428.place(x=400,y=130,width=70,height=25)
        GCheckBox_428["offvalue"] = "0"
        GCheckBox_428["onvalue"] = "1"
        GCheckBox_428["command"] = self.GCheckBox_428_command

        GListBox_333=tk.Listbox(root)
        GListBox_333["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_333["font"] = ft
        GListBox_333["fg"] = "#333333"
        GListBox_333["justify"] = "center"
        GListBox_333.place(x=380,y=290,width=236,height=584)

        GLineEdit_788=tk.Entry(root)
        GLineEdit_788["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_788["font"] = ft
        GLineEdit_788["fg"] = "#333333"
        GLineEdit_788["justify"] = "center"
        GLineEdit_788["text"] = "Entry"
        GLineEdit_788.place(x=0,y=0,width=374,height=880)

        GMessage_688=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_688["font"] = ft
        GMessage_688["fg"] = "#333333"
        GMessage_688["justify"] = "center"
        GMessage_688["text"] = "Message"
        GMessage_688.place(x=380,y=230,width=237,height=57)

    def GButton_125_command(self):
        print("command")


    def GCheckBox_428_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
