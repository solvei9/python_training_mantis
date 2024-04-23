from model.project import Project
from random import randrange


def test_add_project(app):
    ind = str(randrange(0, 99))
    project = Project(name="Project " + ind, description="Project " + ind + " description")
    old_projects = app.project.get_project_list()
    app.project.create(project)
    new_projects = app.project.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
