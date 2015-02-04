from flask import Flask, render_template, request
import hackbright

app = Flask(__name__)

@app.route("/project")
def get_project1():
    hackbright.connect_to_db()
    title = request.args.get("get_project")
    row = hackbright.get_project(title)
    html = render_template("student_info.html", id=row[0],title=row[1], description=row[2], maxgrade=row[3] )
    return html

@app.route("/")
def get_title():
    return render_template("get_project.html")

if __name__ == "__main__":
    app.run(debug=True)