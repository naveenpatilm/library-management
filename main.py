from book import Book

book = Book("GOT", "naveen")
book.save()
print(book.findAll())
print(book.findById(22))