import tkinter

def welcome_interface():
    welcome_window = tkinter.Tk()
    welcome_window.title("Alpha")
    welcome_window.geometry("400x100")
    welcome_window.resizable(False, False)
    welcome_window.configure(bg="white")
    welcome_window.mainloop()