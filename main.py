import tkinter as tk
from ui.frame import Frame

class Main:
    def __init__(self, master):
        self.master = master
        self.init_app()

    def init_app(self):
        Frame(self.master)

    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.run()
