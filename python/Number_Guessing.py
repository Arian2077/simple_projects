from random import randint
import tkinter as tk


class numberguessing():
    
    def __init__(self , root):
        self.root = root
        self.root.title("Number Guessing game")
        
        # Making the input part
        tk.Label(root,text="Enter your number ==>",font=(0,15)).grid(row=0,column=0,padx=0,pady=10)
        tk.Entry(root,font=(0,15),justify="center").grid(row=0,column=1,padx=10,pady=0)
        
        # Sending the number for robot
        tk.Button(root,text="Guess",font=(0,15),command=guess_number).grid(row=5, column=0, columnspan=2, pady=1)
        
        
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = numberguessing(root)
    root.mainloop()