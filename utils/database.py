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