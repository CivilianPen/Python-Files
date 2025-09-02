from tkinter import *
def suma(a,b):
    a = str(a)
    b = str(b)
    dot_a = a.find('.')
    dot_b = b.find('.')
    if dot_a == -1:
        a += '.0'
        dot_a = a.find('.')
    if dot_b == -1:
        b += '.0'
        dot_b = b.find('.')

    zeros = (max(len(a[dot_a + 1:]), len(b[dot_b + 1:]))) * '0'
    d = '1'+zeros
    return ((float(a)*int(d)) + (float(b)*int(d)))/ int(d)
def mult(a,b):
    a = str(a)
    b = str(b)
    dot_a = a.find('.')
    dot_b = b.find('.')
    if dot_a == -1:
        a += '.0'
        dot_a = a.find('.')
    if dot_b == -1:
        b += '.0'
        dot_b = b.find('.')

    zeros = (min(len(a[dot_a + 1:]), len(b[dot_b + 1:]))) * '0'
    d = '1' + zeros
    return ((float(a)*int(d)) * (float(b)*int(d)))/ int(d+'0')
def diff(a, b):
    a = str(a)
    b = str(b)
    dot_a = a.find('.')
    dot_b = b.find('.')
    if dot_a == -1:
        a += '.0'
        dot_a = a.find('.')
    if dot_b == -1:
        b += '.0'
        dot_b = b.find('.')

    zeros = (max(len(a[dot_a + 1:]), len(b[dot_b + 1:]))) * '0'
    d = '1' + zeros
    return ((float(a) * int(d)) - (float(b) * int(d))) / int(d)
def divi(a, b):
    try:
        return float(a)/float(b)
    except:
        return 'Error'

global width
global height
class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = ""
        self.lbl = Label(text=self.formula, font=("Times New Roman", 28, "bold"), bg="#000", foreground="#FFF")
        self.lbl.place(x=11, y=25)
        btns = [
            "C", "DEL", "", "",
            "1", "2", "3", "*",
            "4", "5", "6", "/",
            "7", "8", "9", "+",
            "0", ".", "=", "-"
        ]
        x = 10
        y = 112
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="#FFF",
                   font=("Times New Roman", 21),
                   command=com).place(x=x, y=y,
                                      width=int(width/4.3),
                                      height=int(height/7.3))
            x += int(width/4.3)+2
            if x >  int(width/4.3)*4:
                x = 10
                y += int(height/7.3) +2
    def logicalc(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "=":
            if '*' in self.formula:
                a = self.formula[:self.formula.find('*')]
                b = self.formula[self.formula.find('*')+1:]
                self.formula = str(mult(a,b))
            elif '/' in self.formula:
                a = self.formula[:self.formula.find('/')]
                b = self.formula[self.formula.find('/')+1:]
                self.formula = str(divi(a,b))
            elif '+' in self.formula:
                a = self.formula[:self.formula.find('+')]
                b = self.formula[self.formula.find('+')+1:]
                self.formula = str(suma(a,b))
            elif '-' in self.formula:
                a = self.formula[:self.formula.find('-')]
                b = self.formula[self.formula.find('-')+1:]
                self.formula = str(diff(a,b))
        else:
            self.formula += operation
        self.update()
    def update(self):
        self.lbl.configure(text=self.formula)
if __name__ == '__main__':
    width = 350
    height = 400
    root = Tk()
    root["bg"] = "#000"
    root.geometry(f"{width}x{height}+100+100")
    root.title("Калькулятор")
    root.resizable(True, True)
    app = Main(root)
    app.pack()
    root.mainloop()
