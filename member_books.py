from crud_file_repository import CrudFileRepository
from exception import ValueNotFound

class MemberBooks(CrudFileRepository):
    def __init__(self, member_id = None, book_id = None, id = None):
        self.id = id
        self.member_id = member_id
        self.book_id = book_id

    def filepath(self):
        return "member_books.txt"

    def delete(self):
        with open(self.filepath(), "r+") as file:
            lines = file.readlines()
            file.truncate(0)
            file.seek(0)
            for line in lines:
                if (',%s,%s\n' % (str(self.member_id), str(self.book_id))) not in line:
                    file.write(line)
