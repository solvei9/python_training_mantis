from model.project import Project
from random import randrange


def test_add_project(app):
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    ind = str(randrange(0, 99))
    project = Project(name="Project " + ind, description="Project " + ind + " description")
    old_projects = app.soap.get_project_list(username, password)
    app.project.create(project)
    new_projects = app.soap.get_project_list(username, password)
    old_projects.append(project)
    old_projects == new_projects
