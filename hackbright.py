import sqlite3

DB = None
CONN = None

def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    print """\
Student: %s %s
Github account: %s"""%(row[0], row[1], row[2])

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("hackbright.db")
    DB = CONN.cursor()

def make_new_student(first_name, last_name, github):
    query = """INSERT into Students values(?, ?, ?)"""
    DB.execute(query, (first_name, last_name, github))
    print "Successfully added student: %s %s"%(first_name, last_name)

def get_project(title):
    query= """SELECT * FROM Projects WHERE title=?"""
    DB.execute(query, (title, ))
    print DB.fetchone()
    # row1 = DB.fetchone()
    # print "Here is the %s %s %s %s"%(row1[0],row1[1], row1[2], row1[3] )

def main():
    connect_to_db()
    command = None
    while command != "quit":
        input_string = raw_input("HBA Database> ")
        tokens = input_string.split()
        command = tokens[0]
        args = tokens[1:]

        if command == "student":
            get_student_by_github(*args) 
        elif command == "new_student":
            make_new_student(*args)
        elif command == "Get_this_project":
            get_project(*args)

        CONN.commit()    
    CONN.close()        


if __name__ == "__main__":
    main()
