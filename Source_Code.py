from tkinter import *
import tkinter.ttk as ttk
import math as m

root = Tk()
root.title("Home Page")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

heading = Label(root, text = "NERNST-CPR CALCULATOR\n", font = ("Times",70,"underline"), anchor=CENTER)
heading.pack()

line1 = Label(root, text="Hi! What calculation would you like to perform?\n\n", font = "Times 20", anchor=W)
line1.pack()

def cpr_ops():
    cpr = Tk()
    
    cpr.title("Corrosion Penetration Rate")
    cpr.geometry("{0}x{1}+0+0".format(cpr.winfo_screenwidth(), cpr.winfo_screenheight()))

    heading = Label(cpr, text = "Corossion Penetrtion Rate", font = ("Times",70,"underline"), anchor=CENTER)
    heading.grid(row=1, column=1,columnspan=10,padx=200)

    tbc = Label(cpr, text="CPR to be calculated in:", font = ("Arial",20))
    tbc.grid(row=2, column=2,pady=80,columnspan=3)
    tbc_list = ttk.Combobox(cpr, textvariable=StringVar(),font = ("Arial",20))
    tbc_list['values'] = ('mpy', 'mmpy')
    tbc_list.grid(row=2, column=4,pady=80,columnspan=3)

    wl_label = Label(cpr, text = "Weight Loss", font = ("Arial",20), anchor=CENTER)
    wl_label.grid(row = 3, column = 1,pady=30)
    wl_entry = Entry(cpr,textvariable=StringVar(),font = ("Arial",20),width=10)
    wl_entry.grid(row=3,column=2,pady=30)
    wl_unit = Entry(cpr,textvariable=StringVar(),font = ("Arial",20),width=10)
    wl_unit.grid(row=3,column=3,pady=30)
    wl_unit.insert(INSERT,"mg")

    density_label = Label(cpr, text = "Density", font = ("Arial",20), anchor=CENTER)
    density_label.grid(row = 4, column = 1,pady=40)
    density_entry = Entry(cpr,textvariable=StringVar(),font = ("Arial",20),width=10)
    density_entry.grid(row=4,column=2,pady=40)
    density_unit = Entry(cpr,textvariable=StringVar(),font = ("Arial",20),width=10)
    density_unit.grid(row=4,column=3,pady=40)
    density_unit.insert(INSERT,"g/cm^3")

    area_label = Label(cpr, text = "Area", font = ("Arial",20), anchor=CENTER)
    area_label.grid(row = 5, column = 1,pady=20)
    area_entry = Entry(cpr,textvariable=StringVar(),font = ("Arial",20),width=10)
    area_entry.grid(row=5,column=2,pady=20)
    area_unit_list = ttk.Combobox(cpr, textvariable=StringVar(),font = ("Arial",20),width=10)
    area_unit_list['values'] = ('inch^2', 'cm^2')
    area_unit_list.grid(row=5,column=3,pady=20)

    time_label = Label(cpr, text = "Time", font = ("Arial",20), anchor=CENTER)
    time_label.grid(row = 6, column = 1,pady=30)
    time_entry = Entry(cpr,textvariable=StringVar(),font = ("Arial",20),width=10)
    time_entry.grid(row=6,column=2,pady=30)
    time_unit_list = ttk.Combobox(cpr, textvariable=StringVar(),font = ("Arial",20),width=10)
    time_unit_list['values'] = ('hrs', 'years')
    time_unit_list.grid(row=6,column=3,pady=30)


    def cpr_val():
        cpr_tbc_input = tbc_list.get()
        wl_input = float(wl_entry.get())
        density_input = float(density_entry.get())
        area_input = float(area_entry.get())
        area_unit_input = area_unit_list.get()
        time_input = float(time_entry.get())
        time_unit_input = time_unit_list.get()

        if cpr_tbc_input == 'mpy':
            if time_unit_input == 'years':
                time_input = time_input*365*24
            if area_unit_input == 'cm^2':
                area_input = area_input*0.155
            cpr_val = (534*wl_input)/(density_input*area_input*time_input)
        else:
            if time_unit_input == 'years':
                time_input = time_input*365*24
            if area_unit_input == 'inch^2':
                area_input = area_input*6.45
            cpr_val = (87.6*wl_input)/(density_input*area_input*time_input)
            
        cpr_val_display.insert(INSERT,cpr_val)

    cpr_val_display = Entry(cpr,textvariable=StringVar(),font = ("Arial",20),width=10)
    cpr_val_display.grid(row = 5, column=7)
    cpr_but = Button(cpr, text = "CPR Value:", font = ("Arial",20), anchor=CENTER,command=cpr_val)
    cpr_but.grid(row = 4, column=7)

    cpr.mainloop()

cpr_button = Button(root,text="Corrosion Penetration Rate", width=30, height=2, font = "Times 30",command=cpr_ops)
cpr_button.pack()

blank1 = Label(root, text="\n", font = "Times 20", anchor=W)
blank1.pack()

def emf_ops():
    nernst = Tk()
    nernst.title("NERNST Equation")
    nernst.geometry("{0}x{1}+0+0".format(nernst.winfo_screenwidth(), nernst.winfo_screenheight()))

    heading = Label(nernst, text = "Cell Conc. - Nernst Equation", font = ("Times",70,"underline"), anchor=CENTER)
    heading.grid(row=1, column=1,columnspan=10,padx=200)

    tbc = Label(nernst, text="Calculation of EMF Using Nernst Equation", font = ("Arial",20))
    tbc.grid(row=2, column=2,pady=80,columnspan=6)

    temp_label = Label(nernst, text = "Temperature", font = ("Arial",20), anchor=CENTER)
    temp_label.grid(row = 3, column = 1,pady=30)
    temp_entry = Entry(nernst,textvariable=StringVar(),font = ("Arial",20),width=10)
    temp_entry.grid(row=3,column=2,pady=30)
    temp_unit = Entry(nernst,textvariable=StringVar(),font = ("Arial",20),width=10)
    temp_unit.grid(row=3,column=3,pady=30)
    temp_unit.insert(INSERT,"kelvin")

    ne_label = Label(nernst, text = "No. of electrons", font = ("Arial",20), anchor=CENTER)
    ne_label.grid(row = 4, column = 1,pady=40)
    ne_entry = Entry(nernst,textvariable=StringVar(),font = ("Arial",20),width=10)
    ne_entry.grid(row=4,column=2,pady=40)
    ne_unit = Entry(nernst,textvariable=StringVar(),font = ("Arial",20),width=10)
    ne_unit.grid(row=4,column=3,pady=40)
    ne_unit.insert(INSERT,"No unit")

    c1_label = Label(nernst, text = "C1", font = ("Arial",20), anchor=CENTER)
    c1_label.grid(row = 5, column = 1,pady=20)
    c1_entry = Entry(nernst,textvariable=StringVar(),font = ("Arial",20),width=10)
    c1_entry.grid(row=5,column=2,pady=20)
    c1_unit = Entry(nernst,textvariable=StringVar(),font = ("Arial",20),width=10)
    c1_unit.grid(row=5,column=3,pady=40)
    c1_unit.insert(INSERT,"Molar")

    c2_label = Label(nernst, text = "C2", font = ("Arial",20), anchor=CENTER)
    c2_label.grid(row = 6, column = 1,pady=20)
    c2_entry = Entry(nernst,textvariable=StringVar(),font = ("Arial",20),width=10)
    c2_entry.grid(row=6,column=2,pady=20)
    c2_unit = Entry(nernst,textvariable=StringVar(),font = ("Arial",20),width=10)
    c2_unit.grid(row=6,column=3,pady=40)
    c2_unit.insert(INSERT,"Molar")

    def emf_val():
        temp_entry_input = float(temp_entry.get())
        ne_entry_input = float(ne_entry.get())
        c1_entry_input = float(c1_entry.get())
        c2_entry_input = float(c2_entry.get())

        if c1_entry_input>c2_entry_input:
            emf_val = ((2.303*8.314*temp_entry_input)/(ne_entry_input*96500))*m.log10(c1_entry_input/c2_entry_input)
        else:
            emf_val = ((2.303*8.314*temp_entry_input)/(ne_entry_input*96500))*m.log10(c2_entry_input/c1_entry_input)
        
        emf_val_display.insert(INSERT,emf_val)

    emf_but = Button(nernst, text = "EMF Value:", font = ("Arial",20), anchor=CENTER, command=emf_val)
    emf_but.grid(row = 4, column=6)
    emf_val_display = Entry(nernst,textvariable=StringVar(),font = ("Arial",20),width=10)
    emf_val_display.grid(row = 5, column=6)
    emf_unit_display = Entry(nernst,textvariable=StringVar(),font = ("Arial",20),width=10)
    emf_unit_display.grid(row = 5, column=7)
    emf_unit_display.insert(INSERT,"Volts")

    nernst.mainloop()

nernst_button = Button(root,text="EMF of Concentration Cell Using\nNernst Equation", width=30, height=2, font = "Times 30", command=emf_ops)
nernst_button.pack()

frame = Frame(root, height=180)
frame.pack(side=BOTTOM, fill=X)

label = Label(frame, text="Developed By,\nParvathy            Pracheta             Rishwik            Rudransh          Samprati\n", font=("Arial", 25))
label.pack(side=BOTTOM)

root.mainloop()