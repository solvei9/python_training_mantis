from model.project import Project
from random import randrange


def test_add_project(app):
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    ind = str(randrange(0, 99))
    project = Project(name="Project " + ind, description="Project " + ind + " description")
    old_projects = Project.convert_project_list_from_mantis_to_model(app.soap.get_project_list(username, password))
    app.project.create(project)
    old_projects.append(project)
    new_projects = Project.convert_project_list_from_mantis_to_model(app.soap.get_project_list(username, password))
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
