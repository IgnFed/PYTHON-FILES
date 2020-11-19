from tkinter import ttk
from tkinter import *
import sqlite3()


class Product:
    db_name = 'new_database_python'
    
    def __init__(self, window):
        
        #Inicialzar 
        self.wind = window
        self.wind.title('Product Application')

    #Creating a Frame Container
    frame = LabelFrame





















if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()