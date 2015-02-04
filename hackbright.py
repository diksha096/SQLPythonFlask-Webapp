import sqlite3

DB = None
CONN = None

def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    return """\
Student: %s %s
Github account: %s"""%(row[0], row[1], row[2])

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("hackbright.db")
    DB = CONN.cursor()

def make_new_student(first_name, last_name, github):
    query = """INSERT into Students values(?, ?, ?)"""
    DB.execute(query, (first_name, last_name, github))
    CONN.commit()
    return "Successfully added student: %s %s"%(first_name, last_name)

def get_project(title):
    query= """SELECT * FROM Projects WHERE title=?"""
    DB.execute(query, (title, ))
    row1 = DB.fetchone()
    return row1

def make_new_project(title, description, max_grade):
    query = """INSERT INTO Projects(title, description, max_grade) values(?,?,?)"""
    DB.execute(query, (title, description, max_grade))
    CONN.commit()
    return "Successfully added project %s %s %s" %(title, description, max_grade)

def get_grade_by_project(first_name, last_name, project_title):
    query = """SELECT first_name, last_name, project_title, grade FROM Students JOIN Grades ON(github=student_github) 
    WHERE first_name=? AND last_name=? AND project_title=?"""
    DB.execute(query, (first_name, last_name, project_title)) 
    row1= DB.fetchone()
    return "Here is the %s %s %s %s"%(row1[0], row1[1], row1[2], row1[3])

def add_grade_to_project(github, project_title, grade):
    query = """INSERT INTO Grades(student_github,project_title,grade) VALUES (?,?,?)"""
    DB.execute(query, (github, project_title, grade))
    CONN.commit()
    return "Successfully added grade %s %s %s" %(github, project_title, grade)

def show_all_grades(github):
    query= """SELECT * FROM Grades WHERE student_github=?"""
    DB.execute(query, (github,))
    row= DB.fetchall()
    return row
    # return "Here are all the grades for this student %s %s %s" %(row[0], row[1], row[2])

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
        elif command == "get_project":
            get_project(*args)
        elif command == "new_project":
            make_new_project(*args)
        elif command == "grade":
            get_grade_by_project(*args)
        elif command == "add_grade":
            add_grade_to_project(*args)
        elif command == "show_grades":
            show_all_grades(*args)   

    CONN.close()        


if __name__ == "__main__":
    main()
