from book import Book
from member import Member
from exception import ValueNotFound
from member_books import MemberBooks

def save_book():
    name = input('Enter book name>>>')
    author = input('Enter author name>>>')
    book = Book(name, author)
    book.save()

def view_book():
    id = input('Enter book id>>>')
    return Book().find_by_id(id)

def delete_book():
    id = input('Enter book id to be deleted>>>')
    Book().delete_by_id(id)

def update_book():
    id = input('Enter book id to be updated>>>')
    name = input('Enter updated book name>>>')
    author = input('Enter update author name>>>')
    book = Book(name, author, id)
    book.save()

def save_Member():
    name = input('Enter member name>>>')
    member = Member(name)
    member.save()

def view_member():
    id = input('Enter member id>>>')
    return Member().find_by_id(id)

def delete_member():
    id = input('Enter member id to be deleted>>>')
    Member().delete_by_id(id)

def update_member():
    id = input('Enter member id to be updated>>>')
    name = input('Enter updated member name>>>')
    member = Member(name, id)
    member.save()

def issue_book():
    book_id = input('Enter book id to be issued>>>')
    member_id = input('Enter your member id>>>')
    member_book = MemberBooks(member_id, book_id)
    member_book.save()

def return_book():
    book_id = input('Enter book id to be returned>>>')
    member_id = input('Enter your member id>>>')
    member_book = MemberBooks(member_id, book_id)
    member_book.delete()

lib_ops = {
        '1': save_book, 
        '2': view_book, 
        '3': delete_book,
        '4': update_book, 
        '5': save_Member, 
        '6': view_member,
        '7': delete_member, 
        '8': update_member, 
        '9': issue_book, 
        '10': return_book,
        'exit': exit
    }

def main():
    while True:
        print_menu()
        option = input("Please choose your option >>>")
        manage_library(option)

def manage_library(ops):
    try:
        print(lib_ops[ops]())
    except ValueNotFound as v:
        print(str(v))
    except Exception as e:
        print("Something went wrong. Please try again!\n" + str(e))

def print_menu():
    print("""
    Library Management System

        1. Add book
        2. View Book
        3. Delete Book
        4. Update Book

        5. Add Member
        6. View Member
        7. Delete Member
        8. Update Member


        9. Issue Book
        10. Return Book
        
        Type 'exit' to end.""")

main()