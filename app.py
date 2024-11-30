from utils import database

USER_CHOICE = """
Enter:
-'a' to add a new book
-'l' to list all books
-'r' to mark a book as read
-'d' to delete a book
-'q' to quit

your choice: """

def menu():
  user_input = input(USER_CHOICE)
  while user_input != 'q':
    if user_input == 'a':
      prompt_add_book()
    elif user_input == 'l':
      list_books()
    elif user_input == 'r':
      prompt_read_book()
    elif user_input == 'd':
      prompt_delete_book()
    user_input = input(USER_CHOICE)

def prompt_add_book():
  name = input('Enter the new book name: ')
  author = input('Enter the author: ')

  database.add_book(name, author)

def list_books():
  books = database.get_all_books()
  for book in books:
    title = book['name']
    author = book['author']
    read = 'yes'if book['read'] else 'no'
    print(f'{title} written by {author} has been read: {read}')

def prompt_read_book():
  name = input('What is the title of the book: ')
  database.mark_read(name)

def prompt_delete_book():
  name = input('Enter the name of the book to remove from the database: ')
  database.delete_book_better(name)

menu()