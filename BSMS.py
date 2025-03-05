import json

from add_book import add_book
from view_book import view_books
from update_book import update_book
#from remove_book import remove_book

class Book:
    book_objects = []
    
    def __init__(self, book_id, title, author, genre, publisher, year_of_publication, price, quantity):
        self.__isbn = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.publisher = publisher
        self.year_of_publication = year_of_publication
        self.__price = price
        self.__quantity = quantity
        
    def __str__(self):
        return f"ISBN: {self.__isbn}\nTitle: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}\nPublisher: {self.publisher}\nYear of Publication: {self.year_of_publication}\nPrice: {self.__price}\nQuantity in Stock: {self.__quantity}\n"

    def get_isbn(self):
        return self.__isbn
    
    def set_price(self, price):
        self.__price = price
        
    def set_quantity(self, quantity):
        self.__quantity = quantity
    
    @staticmethod
    def load_book_data():
        try:
            with open("books.json", "r") as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print("\nNo File available!\n")
        except json.decoder.JSONDecodeError:
            print("\nNo data available!\n")
        except Exception as e:
            print(e)
      
    @staticmethod
    def add_book():
        while True:
            isbn = input("Enter Book ISBN:")
            if isbn.isnumeric() == False:
                print("\nInvalid ISBN! must be an Integer.\n")
                continue
            else:
                isbn = int(isbn)
                break
        
        for book in Book.book_objects:
            if book.get_isbn() == isbn:
                print("\nBook already exists!\n")
                return
            else:
                add_book(isbn, Book)
                return
            
    @staticmethod 
    def view_books():
        view_books(Book)
    
    @staticmethod
    def search_book():
        while True:
            get_value =  input("1. Search by Title, Author, Genre, Publication or Year of publication(back to menue > B): ")
            print()
            if get_value == 'B' or get_value == 'b':
                return
            else:
                for book in Book.book_objects:
                    if get_value in book.title or get_value in book.author or get_value in book.genre or get_value in book.publisher or get_value in str(book.year_of_publication):
                        print(book)
                        return
                    else:
                        print("\nBook not found\n")
                        return
    @staticmethod
    def update_book():
        isbn = int(input("Enter Book ISBN:"))
        for book in Book.book_objects:
            if book.get_isbn() == isbn:
                update_book(book)
                return
        print("\nBook not found!\n")
        
    @staticmethod
    def remove_book():
        isbn = int(input("Enter Book ISBN:"))
        for book in Book.book_objects:
            if book.get_isbn() == isbn:
                Book.book_objects.remove(book)
                print("\nBook removed!\n")
                return
        print("\nBook not found!\n")
        
    @staticmethod
    def save_book_data():
        data = {"books": []}
        for book in Book.book_objects:
            data["books"].append({"ISBN": book.get_isbn(), "title": book.title, "author": book.author, "genre": book.genre, "publisher": book.publisher, "year_of_publication": book.year_of_publication, "price": book.__price, "quantity_in_stock": book.__quantity})
        try:
            with open("books.json", "w") as file:
                json.dump(data, file, indent=4)
                print("\nData saved successfully!\n")
        except FileNotFoundError:
            print("\nNo File available!\n")
        except json.decoder.JSONDecodeError:
            print("\nNo data available!\n")
        except Exception as e:
            print(e)
            
data = Book.load_book_data()

if data is not None:
    for book in data['books']:
        temp = Book(book["ISBN"], book["title"], book["author"], book["genre"], book["publisher"], book["year_of_publication"], book["price"], book["quantity_in_stock"])
        Book.book_objects.append(temp)   
    print("Data loaded successfully!")  
                                   





