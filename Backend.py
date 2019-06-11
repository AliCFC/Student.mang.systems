import sqlite3

def Student():

    con=sqlite3.connect("student.db")
    con.execute("create table if not exists student(id INTEGER PRIMARY KEY , StdID text, Firstname text, Surname text, DoB text, \
    Age text, Gender text, Adress text, Mobile text)")
    con.commit()
    con.close()

def addStdRecord (StdID, Firstname, Surname, DoB, Age, Gender, Adress, Mobile):
    con = sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("insert into student values(Null,?,?,?,?,?,?,?,?)",(StdID, Firstname, Surname, DoB, Age, Gender, Adress, Mobile))
    con.commit()
    con.close()

def viewData ():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("selecte * from student")
    rows=cur.fetchall()
    con.close()
    return rows

def deletRecord ():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("delete from student set where id=?", (id,))
    con.commit()
    con.close()

def searchData(StdID="", Firstname="", Surname="", DoB="", Age="", Gender="", Adress="", Mobile=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("select * from student set where StdID=? OR Firstname=? OR Surname=? OR DoB=? OR Age=? OR Gender=? OR Adress=? OR Mobile=?", \
                (StdID, Firstname, Surname, DoB, Age, Gender, Adress, Mobile))
    rows=cur.fetchall()
    con.close()
    return rows

def updatehData(StdID="", Firstname="", Surname="", DoB="", Age="", Gender="", Adress="", Mobile=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("update student set where StdID=? OR Firstname=? OR Surname=? OR DoB=? OR Age=? OR Gender=? OR Adress=? OR Mobile=?", \
                (StdID, Firstname, Surname, DoB, Age, Gender, Adress, Mobile, id))
    con.commit()
    con.close()

