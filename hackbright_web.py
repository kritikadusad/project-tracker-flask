"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    grades_and_projects = hackbright.get_grades_by_github(github)

    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github, grades_and_projects = grades_and_projects)

    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student-add")
def student_add():
	""" Show form for adding a student."""

	return render_template("add_student.html")


@app.route("/student-added", methods = ["POST"])
def student_added():
	""" Show information about added student."""

	first_name = request.form.get('firstname')
	last_name = request.form.get('lastname')
	github = request.form.get('github')

	hackbright.make_new_student(first_name, last_name, github)

	return render_template("added.html",
							github=github)


@app.route("/project")
def get_project():
	""" Show project information """

	title = request.args.get('title')

	project_title, description, max_grade = hackbright.get_project_by_title(title)
	
	return render_template("project_info.html", 
							project_title=project_title,
							description=description,
							max_grade=max_grade)



if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
