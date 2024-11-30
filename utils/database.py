"""

Concerned with storing and retrieving books from a csv file

name,author,0\n
name,author,0\n
"""
books_file = 'books.csv'

def add_book(name, author):
  with open(books_file, 'a') as file:
    file.write(f'{name}, {author},0\n')

def get_all_books():
  with open(books_file, 'r') as file:
    lines = [line.strip().split(',') for line in file.readlines()] #[['name','author','0'],[name,author,0]]
  return [
    {
      'name': line[0], 'author': line[1], 'read': line[2]
    } for line in lines
  ]

def mark_read(title):
  books = get_all_books()
  for book in books:
    name = book['name']
    if name == title:
      book['read'] = '1'
      _save_all_books(books)
  
def _save_all_books(books):
  with open(books_file, 'w') as file:
    for book in books:
      file.write(f"{book['name']},{book['author']},{book['read']}\n")

#best practise to remove a book from a list is creating a new list with list comprehension
def delete_book_better(title):
  books = get_all_books() 
  books = [book for book in books if book['name'] != title]
  _save_all_books()


