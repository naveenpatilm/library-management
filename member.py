from crud_file_repository import CrudFileRepository

class Member(CrudFileRepository):

    def __init__(self, name = None, id = None):
        self.id = id
        self.name = name
    
    def filepath(self):
        return "members.txt"