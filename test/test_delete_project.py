from model.project import Project
from random import randrange
from random import choice


def test_delete_project(app):
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    old_projects = app.soap.get_project_list(username, password)
    if len(old_projects) == 0:
        ind = str(randrange(0, 99))
        app.project.create(Project(name="Project " + ind), description="Project " + ind + " description")
        old_projects = app.soap.get_project_list(username, password)
    project = choice(old_projects)
    old_projects.remove(project)
    app.project.delete_project_by_id(project.id)
    new_projects = app.soap.get_project_list(username, password)
    assert old_projects == new_projects
