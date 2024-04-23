from model.project import Project
from random import randrange
from random import choice


def test_delete_project(app):
    old_projects = app.project.get_project_list()
    if len(old_projects) == 0:
        ind = str(randrange(0, 99))
        app.project.create(Project(name="Project " + ind), description="Project " + ind + " description")
        old_projects = app.project.get_project_list()
    project = choice(old_projects)
    old_projects.remove(project)
    app.project.delete_project_by_id(project.project_id)
    new_projects = app.project.get_project_list()
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
