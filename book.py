from crud_file_repository import CrudFileRepository

class Book(CrudFileRepository):
    def __init__(self, name, author, id = None):
        self.id = id
        self.name = name
        self.author = author
        super(Book, self).__init__("books.txt")
