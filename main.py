from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    entrada = None
    tipoUnidad = None
    
    def __init__(self):
        Tk.__init__(self)
        self.title("Termometro")
        self.geometry("200x150")
        self.configure(bg = "#DED789")
        
        self.temperatura = StringVar(value="")
        self.tipoUnidad = StringVar(value="C")
        
        self.createLayout()
    
    def createLayout(self):
        self.entrada = ttk.Entry(self, variable=self.temperatura)
        

        
    def start(self):
        self.mainloop()
        
if __name__ == "__main__":
    app = mainApp()
    app.start()