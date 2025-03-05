def update_book(book):
    while True:    
        title = input("Enter Book title: ")
        if title == "":
            print("\nInvalid Title! Title can not be empty \n")
            continue
        elif type(title) != str:
            print("\nInvalid Title! Title must be a String.\n")
            continue
        else:
            break
    
    while True:    
        author = input("Enter Book author: ")
        if author == "":
            print("\nInvalid Author! can not be empty.\n")
            continue
        elif type(author) != str:
            print("\nInvalid Author! must be a String.\n")
            continue
        else:
            break
        
    while True:    
        genre = input("Enter Book genre: ")
        if genre == "":
            print("\nInvalid Genre! can not be empty.\n")
            continue
        elif type(genre) != str:
            print("\nInvalid Genre! must be a String.\n")
            continue
        else:
            break
        
    while True:    
        publisher = input("Enter Book publisher: ")
        if publisher == "":
            print("\nInvalid Publisher! can not be Empty.\n")
            continue
        elif type(publisher) != str:
            print("\nInvalid Publisher! must be a String.\n")
            continue
        else:
            break
        
    while True:    
        year_of_publication = input("Enter Year of Publication: ")
        if year_of_publication == None:
            print("\nInvalid Year_of_publication! can not be empty.\n")
            continue
        elif year_of_publication.isnumeric() == False:
            print("\nInvalid Year_of_publication! must be an Integer.\n")
            continue
        else:
            year_of_publication = int(year_of_publication)
            break
        
    while True:
        price = input("Enter Book price: ")
        if type(price) == 'str' or float(price) < 0:
            print("\nInvalid Price! must be a positive number.\n")
            continue
        else:
            price = float(price)
            break
        
    while True:
        quantity = input("Enter Book quantity: ")
        if quantity.isnumeric() == False or int(quantity) < 0:
            print("\nInvalid Quantity! must be a non-negative integer.\n")
            continue
        else:
            quantity = int(quantity)
            break
    
    book.title = title
    book.author = author
    book.genre = genre
    book.publisher = publisher
    book.year_of_publication = year_of_publication
    book.set_price(price)
    book.set_quantity(quantity)
    print("\nBook updated successfully!\n")