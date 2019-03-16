from crud_file_repository import CrudFileRepository

class Member(CrudFileRepository):
    def __init__(self, name, id = None):
        self.id = id
        self.name = name
        super(Member, self).__init__("../member.txt")