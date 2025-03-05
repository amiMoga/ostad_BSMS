from BSMS import Book

#Book.load_book_data()

while True:
    print("BOOK STORE MANAGEMENT SYSTEM")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Remove Book")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        Book.add_book()
    elif choice == 2:
        Book.view_books()
    elif choice == 3:
        Book.search_book()
    elif choice == 4:
        Book.update_book()
    elif choice == 5:
        Book.remove_book()
    elif choice == 6:
        Book.save_book_data()
        break
    else:
        print("Invalid choice! Please enter a valid choice:")
        continue
    
