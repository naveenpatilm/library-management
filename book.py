from crud_file_repository import CrudFileRepository

class Book(CrudFileRepository):

    def __init__(self, name = None, author = None, id = None):
        self.id = id
        self.name = name
        self.author = author

    def filepath(self):
        return "books.txt"