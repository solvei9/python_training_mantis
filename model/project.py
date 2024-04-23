from sys import maxsize


class Project:
    def __init__(self, name=None, status=None, category=None, view_state=None, description=None, project_id=None):
        self.name = name
        self.status = status
        self.category = category
        self.view_state = view_state
        self.description = description
        self.project_id = project_id

    def __repr__(self):
        return "%s:%s:%s;%s;%s;%s" % (self.name, self.status, self.description, self.category, self.view_state,
                                      self.project_id)

    def __eq__(self, other):
        return ((self.project_id is None or other.project_id is None or self.project_id == other.project_id)
                and self.name == other.name)

    def id_or_max(self):
        if self.project_id:
            return int(self.project_id)
        else:
            return maxsize
