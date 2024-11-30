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
    read = book['read']
    print(f'{title} written by {author} has been read: {read}')

def prompt_read_book():
  pass

def prompt_delete_book():
  pass

menu()