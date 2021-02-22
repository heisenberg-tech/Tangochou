import tkinter as tk

bTxtList = ['accent:0','accent:1','accent:2','accent:3','accent:4','accent:5'] 
tango_dict = {'林檎': ['ringo', '0'], 'バナナ': ['banana','1'], 'online': '20'}
length = len(list(tango_dict.values()))

print(list(tango_dict.keys()))
print(list(tango_dict.values()))

class Application(tk.Frame):

    def __init__(self, master = None, tango_dict=tango_dict):
        self.count = 0
        self.entry_user = tk.Entry()

        tk.Frame.__init__(self, master)
        self.pack(expand = 1, fill = tk.BOTH, anchor = tk.NW)
        self.display_word()
        self.createWidgets()

    def display_word(self):
        self.text = tk.StringVar()
        self.text.set(list(tango_dict.keys())[self.count])
        self.label = tk.Label(textvariable=self.text)
        self.label.pack()


    def createWidgets(self):
        tk.Label(text="How to read this tango?", font=("System",12)).pack()
        self.entry_user.pack()
        tk.Label(text="What type is the accent?", font=("System",12)).pack()
        self.btn0 = tk.Button(text='0', command=self.judge, height=1,width=10)
        self.btn1 = tk.Button(text='1', command=self.judge, height=1,width=10)
        self.btn2 = tk.Button(text='2', command=self.judge, height=1,width=10)
        self.btn3 = tk.Button(text='3', command=self.judge, height=1,width=10)
        self.btn4 = tk.Button(text='4', command=self.judge, height=1,width=10)
        self.btn5 = tk.Button(text='5', command=self.judge, height=1,width=10)
        self.btn0.pack(expand = 1, fill = tk.BOTH, anchor = tk.NW)
        self.btn1.pack(expand = 1, fill = tk.BOTH, anchor = tk.NW)
        self.btn2.pack(expand = 1, fill = tk.BOTH, anchor = tk.NW)
        self.btn3.pack(expand = 1, fill = tk.BOTH, anchor = tk.NW)
        self.btn4.pack(expand = 1, fill = tk.BOTH, anchor = tk.NW)
        self.btn5.pack(expand = 1, fill = tk.BOTH, anchor = tk.NW)


    def judge(self):

        entry_user = self.entry_user.get()
        print(entry_user)

        print(list(tango_dict.values())[self.count])
        if entry_user == list(tango_dict.values())[self.count][0]:
            print("tadasii!!")
        if self.count < length - 1:
            self.count += 1
            self.text.set(list(tango_dict.keys())[self.count])
        else:
            self.text.set("終了")


root = tk.Tk().title("TangoChou")
app = Application(master = root)
app.mainloop()