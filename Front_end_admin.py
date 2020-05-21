from tkinter import *
from tkinter import messagebox
import Back_end_admin
website_list=[]

def view_command():
    
    v_L= Back_end_admin.view()
    
    L = (len(v_L))
    
    list1.delete(0,END)
    for row in v_L:
        list1.insert(END,row)
    
    if L<5:
        for i in range(5):
            v_L.append("No Entry")
    E1.delete(0,END)
    E1.insert(END,v_L[0])
    E2.delete(0,END)
    E2.insert(END,v_L[1])
    E3.delete(0,END)
    E3.insert(END,v_L[2])
    E4.delete(0,END)
    E4.insert(END,v_L[3])
    E5.delete(0,END)
    E5.insert(END,v_L[4])

def add_command():
    website_list = [wb_1.get(),wb_2.get(),wb_3.get(),wb_4.get(),wb_5.get()] 
    list1.delete(0,END)
    (s,e) = time()
    Back_end_admin.add(website_list,s,e)
    messagebox.showinfo("Distracting Website Blocker", "Websites Added")


def time():
    start = int(s_time.get())
    end =   int(e_time.get())
    return (start,end)

"""def get_data(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
""" 
    

def update_command():
    website_list = [wb_1.get(),wb_2.get(),wb_3.get(),wb_4.get(),wb_5.get()] 
    Back_end_admin.update(website_list)
    messagebox.showinfo("Distracting Website Blocker", "Websites Updated")
    
def delete_command():
    website_list = [wb_1.get(),wb_2.get(),wb_3.get(),wb_4.get(),wb_5.get()] 
    Back_end_admin.delete(website_list)
    messagebox.showinfo("Distracting Website Blocker", "Websites Deleted")


window = Tk()
window.wm_title("Distracting Website Blocker")

L1  = Label(window,text = "Website 1")
L1.grid(row = 0, column = 0)

wb_1 = StringVar()
E1 = Entry(window,textvariable = wb_1 )
E1.grid(row = 0, column=1 )

L2  = Label(window,text = "Website 2")
L2.grid(row = 1, column = 0)

wb_2 = StringVar()
E2 = Entry(window,textvariable = wb_2 )
E2.grid(row = 1, column=1 )

L3  = Label(window,text = "Website 3")
L3.grid(row = 2, column = 0)


wb_3 = StringVar()
E3 = Entry(window,textvariable = wb_3 )
E3.grid(row = 2, column=1 )

L4  = Label(window,text = "Website 4")
L4.grid(row = 3, column = 0)

wb_4 = StringVar()
E4 = Entry(window,textvariable = wb_4 )
E4.grid(row = 3, column=1 )

L5  = Label(window,text = "Website 5")
L5.grid(row = 4, column = 0)

wb_5 = StringVar()
E5 = Entry(window,textvariable = wb_5 )
E5.grid(row = 4, column=1 )

L6 = Label(window,text = "Starting Hour[24h]")
L6.grid(row = 0, column = 2)

s_time = StringVar()
E6 = Entry(window,textvariable = s_time )
E6.grid(row = 0, column=3 )

L7 = Label(window,text = "Ending Hour[24h]")
L7.grid(row = 1, column = 2)

e_time = StringVar()
E7 = Entry(window,textvariable = e_time )
E7.grid(row = 1, column=3 )




L8 = Label(window,text = "Website List")
L8.grid(row = 2, column = 3)

list1 = Listbox(window,height = 6,width = 35)
list1.grid(row =3, column = 2,columnspan = 3,rowspan = 3)

sb1 = Scrollbar(window)
sb1.grid(row = 3,column = 4,rowspan = 6)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

#list1.bind('<<ListboxSelect>>',get_data)

b1 = Button(window,text = "Add all",width = 12, command = add_command)
b1.grid(row = 7,column = 0)

b2 = Button(window,text = "View all",width = 12,command = view_command)
b2.grid(row = 7,column = 1)

b3 = Button(window,text = "Update",width = 12,command = update_command)
b3.grid(row = 7,column = 2)

b4 = Button(window,text = "Delete all",width = 12,command = delete_command)
b4.grid(row = 7,column = 3)

b5 = Button(window,text = "Exit",width = 12)
b5.grid(row = 7,column = 4)


window.mainloop()