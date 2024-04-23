from selenium.webdriver.common.by import By
from model.project import Project


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_proj_create_page.php"):
            wd.get(self.app.base_url + "/manage_proj_create_page.php")

    def create(self, project):
        wd = self.app.wd
        self.open_project_page()
        self.fill_project_form(project)
        # submit project creation
        wd.find_element(By.CSS_SELECTOR, "input[value='Add Project']").click()
        self.app.project.open_project_management_page()
        self.project_cache = None

    def open_project_management_page(self):
        wd = self.app.wd
        wd.get(self.app.base_url + "/manage_proj_page.php")

    def fill_project_form(self, project):
        self.change_field_value("name", project.name)
        self.select_field_value("status", project.status)
        self.select_field_value("view_state", project.view_state)
        self.change_field_value("description", project.description)

    def select_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.XPATH, "//select[@name='" + field_name + "']/option[@value='" + text + "']").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.app.project.open_project_management_page()
            self.project_cache = []
            projects_list = wd.find_elements(By.CSS_SELECTOR, "tr[class='row-1'], tr[class='row-2']")
            projects_list.pop(len(projects_list) - 1)
            for element in projects_list:
                properties = element.find_elements(By.CSS_SELECTOR, "td")
                name = properties[0].find_element(By.CSS_SELECTOR, "a").text
                status = properties[1].text
                view_state = properties[3].text
                description = properties[4].text
                href = properties[0].find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                project_id = href[71:len(href)]
                self.project_cache.append(
                    Project(name=name, status=status, view_state=view_state, description=description,
                            project_id=project_id))
        return list(self.project_cache)

    def select_project_by_project_id(self, project_id):
        wd = self.app.wd
        wd.find_element(By.XPATH, '//a[@href="manage_proj_edit_page.php?project_id=%s"]' % project_id).click()

    def delete_project_by_id(self, project_id):
        wd = self.app.wd
        self.open_project_management_page()
        self.select_project_by_project_id(project_id)
        # submit project deletion
        wd.find_element(By.CSS_SELECTOR, "input[value='Delete Project']").click()
        # confirm project deletion
        wd.find_element(By.CSS_SELECTOR, "input[value='Delete Project']").click()
        self.app.project.open_project_management_page()
        self.project_cache = None
