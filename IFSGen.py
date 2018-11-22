'''To Do:
This will be an exe, just run it to get gui and work from there.
'''

import tkinter as tk    
from tkinter import messagebox
import generator as gen

    
    
#####Functions that will be used        
        
def get_evaluation():
    """ get evaluation from entry fields """
    dim = int(enter_dim.get())
    if dim not in (1, 2, 3):   
        messagebox.showwarning("Warning","The dimension must be 1, 2 or 3!")
        
    precision = int(enter_precision.get())
    if precision<=0:   
        messagebox.showwarning("Warning","The precision must be a positive number!")
    
    num_maps = int(enter_num_maps.get())
    return (dim, num_maps, precision)


def update_gui():
    """ update the number of maps """
    dim, num_maps, precision = get_evaluation()    
    for widg in list(root.winfo_children())[8:]:
        widg.destroy()
    
    if dim == 1:
        for i in range(num_maps):                   
            tk.Label(root, text='Map '+str(i+1)+ ': x coord').grid(row=i+5)
            mapi = tk.Entry(root)
            mapi.grid(row=i+5, column=1)
        
    if dim == 2:
        for i in range(num_maps):                   
            tk.Label(root, text='Map '+str(i+1)+ ': x coord').grid(row=i+5)
            mapi = tk.Entry(root)
            mapi.grid(row=i+5, column=1)
        
        for i in range(num_maps):                   
            tk.Label(root, text='y coord').grid(row=i+5,column = 2)
            mapi = tk.Entry(root)
            mapi.grid(row=i+5, column=3)
        
    if dim == 3:
        for i in range(num_maps):                   
            tk.Label(root, text='Map '+str(i+1)+ ': x coord').grid(row=i+5)
            mapi = tk.Entry(root)
            mapi.grid(row=i+5, column=1)
        
        for i in range(num_maps):                   
            tk.Label(root, text='y coord').grid(row=i+5,column = 2)
            mapi = tk.Entry(root)
            mapi.grid(row=i+5, column=3)
        
        for i in range(num_maps):                   
            tk.Label(root, text='z coord').grid(row=i+5,column = 4, padx=5)
            mapi = tk.Entry(root)
            mapi.grid(row=i+5, column=5)
    tk.Button(root, text='Generate Fractal', command=make_pic).grid(sticky = 'w')


def check_maps(map_entries):
    for map_func in map_entries:
        if len(str(map_func.get())) == 0:   
            return True    
    
def make_pic():
    """ get maps from map fields, makes a picture """
    dim, num_maps, precision = get_evaluation()
    map_entries = list(root.winfo_children())[9:-1][::2]
    if check_maps(map_entries):
        messagebox.showwarning("Warning","Maps can't be empty!")
        return 
    maps = [map_func.get() for map_func in map_entries]
    gen.gen_maps(maps,precision,dim)
    
    


    
    

        
if __name__ == '__main__':        
    
    #%matplotlib qt
    
    #Initial set-up
    root = tk.Tk() 
    root.title("IFSGen")
    root.geometry("700x700")
    root.resizable(True, True)
    
    #Add buttons and entry boxes dynamically     
    message= tk.Label(root, text='Welcome to IFSGen!')
    message.grid(row=0,columnspan=5, sticky = 'n')
    
        
    tk.Label(root, text='How many dimensions would you like in your IFS? (either 1, 2 or 3)').grid(row=1,sticky = 'w', columnspan = 3)
    enter_dim = tk.Entry(root)
    enter_dim.grid(row=1, column=3)
    enter_dim.insert(0,'2')        
        

    tk.Label(root, text='How many functions would you like in your IFS?').grid(row=2,sticky = 'w', columnspan = 3)
    enter_num_maps = tk.Entry(root)
    enter_num_maps.grid(row=2, column=3)
    enter_num_maps.insert(0,'5')
        
        
    tk.Label(root, text='How many levels would you like to see? (Try 100 to start with)').grid(row=3,sticky = 'w',columnspan = 3)
    enter_precision = tk.Entry(root)
    enter_precision.grid(row=3, column=3)
    enter_precision.insert(0,'100')
    
    tk.Button(root, text='Update', command=update_gui).grid(row=4,sticky = 'w')
    

    for i in range(5):                   
        tk.Label(root, text='Map '+str(i+1)+ ': x coord').grid(row=i+5)
        mapi = tk.Entry(root)
        mapi.grid(row=i+5, column=1)
    
    for i in range(5):
        tk.Label(root, text='y coord').grid(row=i+5,column=2)
        mapi = tk.Entry(root)
        mapi.grid(row=i+5, column=3)    
    
    
    tk.Button(root, text='Generate Fractal', command=make_pic).grid(sticky = 'w')
     
        
    root.mainloop()
    