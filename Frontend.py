#Frontend

from tkinter import*
import tkinter.messagebox
import Backend


class student :

    def __init__(self, root):
        self.root = root
        self.root.title("Student Database Managment Systems")
        self.root.geometry("1359x750+0+0")
        self.root.config(bg="cadet blue")

        StdID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        DoB = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Adress = StringVar()
        Mobile = StringVar()

#===============================================Funktions=====================================================

        def iexit():
            iexit = tkinter.messagebox.askyesno("Student database management systems", "Confirm if you want to exit")
            if iexit > 0:
                root.destroy()
                return
        def clearData():
            self.txtStdID.delete(0,END)
            self.txtStdFna.delete(0,END)
            self.txtStdSna.delete(0,END)
            self.txtStdDob.delete(0,END)
            self.txtStdAge.delete(0,END)
            self.txtStdAdr.delete(0,END)
            self.txtStdGdr.delete(0,END)
            self.txtStdMbl.delete(0,END)

        def addData ():
            if (len(StdID.get()) != 0):
                Backend.addStdRecord(StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Adress.get(), Mobile.get())
                studentList.delete(0,END)
                studentList.insert(END,(StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Adress.get(), Mobile.get()))

        def displayData ():
            studentList.delete(0,END)
            for row in Backend.viewData():
                studentList.insert(END, row, str(""))

        def StudentRec (event):
            global sd
            searchStd= studentList.curselection()[0]
            sd=studentList.get(searchStd)
            self.txtStdID.delete(0, END)
            self.txtStdID.insert(END, sd[1])
            self.txtStdFna.delete(0, END)
            self.txtStdFna.insert(END, sd[2])
            self.txtStdSna.delete(0, END)
            self.txtStdSna.insert(END, sd[3])
            self.txtStdDob.delete(0, END)
            self.txtStdDob.insert(END, sd[4])
            self.txtStdAge.delete(0, END)
            self.txtStdAge.insert(END, sd[5])
            self.txtStdAdr.delete(0, END)
            self.txtStdAdr.insert(END, sd[6])
            self.txtStdGdr.delete(0, END)
            self.txtStdGdr.insert(END, sd[7])
            self.txtStdMbl.delete(0, END)
            self.txtStdMbl.insert(END, sd[8])



        def deletData ():
            if (len(StdID.get()) != 0):
                Backend.deletRecord(sd[0])
                clearData()
                displayData()

        def searchData():
            studentList.delete(0,END)
            for row in Backend.searchData(StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Adress.get(), Mobile.get()):
                studentList.insert(END, row, str(""))

        def updateData():
            if (len(StdID.get()) != 0):
                Backend.deletRecord(sd[0])
            if (len(StdID.get()) != 0):
                Backend.addStdRecord(StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Adress.get(), Mobile.get())
                studentList.delete(0,END)
                studentList.insert(END,(StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Adress.get(), Mobile.get()))





#===============================================Frames========================================================

        MainFrame = Frame(self.root, bg="cadet blue")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="Ghost White", relief= RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame, font=('arial', 47, 'bold'), text="Student Database Mangement Systems", bg="Ghost White")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1,width=1300, height=400, padx=20, pady=20, bg="Cadet blue", relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLeft = LabelFrame(DataFrame, bd=1, width=1000, height=600,padx=20, bg="Ghost White", relief=RIDGE,
                                   font=('arial', 20, 'bold'),text="Student Informations\n")
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, bg="Ghost White", relief=RIDGE,
                                    font=('arial', 20, 'bold'), text="Student Detais\n")
        DataFrameRight.pack(side=RIGHT)

#===============================================Labels and Entry Widget=====================================================

        self.lblStdID = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Student ID:", padx=2, pady=2, bg="Ghost White")
        self.lblStdID.grid(row=0, column=0, sticky=W)
        self.txtStdID = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=StdID, width=39)
        self.txtStdID.grid(row=0, column=1, sticky=W)

        self.lblStdFna = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Firstname:", padx=2, pady=2, bg="Ghost White")
        self.lblStdFna.grid(row=1, column=0, sticky=W)
        self.txtStdFna = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=Firstname, width=39)
        self.txtStdFna.grid(row=1, column=1, sticky=W)

        self.lblStdSna = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Surname:", padx=2, pady=3, bg="Ghost White")
        self.lblStdSna.grid(row=2, column=0, sticky=W)
        self.txtStdSna = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=Surname, width=39)
        self.txtStdSna.grid(row=2, column=1, sticky=W)

        self.lblStdDob = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Date of Birth:", padx=3, pady=2, bg="Ghost White")
        self.lblStdDob.grid(row=3, column=0, sticky=W)
        self.txtStdDob = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=DoB, width=39)
        self.txtStdDob.grid(row=3, column=1, sticky=W)

        self.lblStdAge = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Age:", padx=2, pady=3, bg="Ghost White")
        self.lblStdAge.grid(row=4, column=0, sticky=W)
        self.txtStdAge = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=Age, width=39)
        self.txtStdAge.grid(row=4, column=1, sticky=W)

        self.lblStdGdr = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Gender:", padx=2, pady=3, bg="Ghost White")
        self.lblStdGdr.grid(row=5, column=0, sticky=W)
        self.txtStdGdr = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=Gender, width=39)
        self.txtStdGdr.grid(row=5, column=1, sticky=W)

        self.lblStdAdr = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Adress:", padx=2, pady=3, bg="Ghost White")
        self.lblStdAdr.grid(row=6, column=0, sticky=W)
        self.txtStdAdr = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=Adress, width=39)
        self.txtStdAdr.grid(row=6, column=1, sticky=W)

        self.lblStdMbl = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Mobile:", padx=2, pady=3, bg="Ghost White")
        self.lblStdMbl.grid(row=7, column=0, sticky=W)
        self.txtStdMbl = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=Mobile, width=39)
        self.txtStdMbl.grid(row=7, column=1, sticky=W)

#==============================================ListBox and ScrollBar Widget============================================
        scrollbar = Scrollbar(DataFrameRight)
        scrollbar.grid(row=0, column=1, sticky='ns')

        studentList = Listbox(DataFrameRight, width=37, height=16, font=('arial', 12, 'bold'),yscrollcommand=scrollbar.set)
        studentList.bind("<<ListBoxSelect>>", StudentRec)
        studentList.grid(row=0, column=0, padx=8)
        scrollbar.config(command= studentList.yview)


#===============================================Button Widget=====================================================

        self.btnAddDate = Button(ButtonFrame, text="Add New", font=('arial', 20, 'bold'),height=1, width=9, bd=4, command=addData)
        self.btnAddDate.grid(row=0, column=0)

        self.btnDisDate = Button(ButtonFrame, text="Display", font=('arial', 20, 'bold'),height=1, width=9, bd=4, command=displayData)
        self.btnDisDate.grid(row=0, column=1)

        self.btnClrDate = Button(ButtonFrame, text="Clear", font=('arial', 20, 'bold'),height=1, width=10, bd=4, command=clearData)
        self.btnClrDate.grid(row=0, column=2)

        self.btnDltDate = Button(ButtonFrame, text="Delete", font=('arial', 20, 'bold'),height=1, width=10, bd=4, command=deletData)
        self.btnDltDate.grid(row=0, column=3)

        self.btnSrcDate = Button(ButtonFrame, text="Search", font=('arial', 20, 'bold'),height=1, width=10, bd=4, command=searchData)
        self.btnSrcDate.grid(row=0, column=4)

        self.btnUpdDate = Button(ButtonFrame, text="Update", font=('arial', 20, 'bold'),height=1, width=10, bd=4, command=updateData)
        self.btnUpdDate.grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, text="Exit", font=('arial', 20, 'bold'),height=1, width=10, bd=4, command=iexit)
        self.btnExit.grid(row=0, column=6)



if __name__=="__main__":
    root = Tk()
    application = student(root)
    root.mainloop()