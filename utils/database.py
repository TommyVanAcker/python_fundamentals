"""

Concerned with storing and retrieving books from a list

"""
books = []

def add_book(name, author):
  books.append({
    'name': name,
    'author': author,
    'read': False
  })

def get_all_books():
  return books

def mark_read(title):
  for book in books:
    name = book['name']
    if name == title:
      book['read'] = True

#best practise to remove a book from a list is creating a new list with list comprehension
def delete_book_better(title):
  global books #tell python that books is not local otherwise python will create a local variabel that only exist here.
  books = [book for book in books if book['name'] != title]

#not a good practise to do the following (removing from a list while iterating over it)
def delete_book(title):
  for book in books:
    name = book['name']
    if name == title:
      books.remove(book)