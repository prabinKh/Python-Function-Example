"""
1. add the book to the librart
2. remove the book from the library
3. search book by title , auther, genre
4. borrow the book
5. return the book
6. view all book in library
7. view borrowed book
8. fine for over due books
"""
from datetime import datetime,timedelta
library = []
borrowed_books = []
def add_book(title, auther,genre):
    books = {
        'title' : title,
        'auther' : auther,
        'genre' : genre,
        "available": True

    }
    library.append(books)
    print (f"the book {title} is adde sucessfully to {auther} about {genre}")



def remove_book(title):
    for book in library:
        if book['title'] == title:
            library.remove(book)
            print(f"the book {title} is removed from the library")
        else:
            print(f"the book {title} is not found in the library")



def search(title,auther,genre):
    found_book = []
    for book in library:
        if book['title'] == title or book['auther'] == auther or book['genre'] == genre:
            found_book.append(book)
            print(f" book found : {book['title']} by {book['auther']} in {book['genre']}")
            return
    if not found_book:
        print("book not found")

def borrow_book(title, borrow):
    for book in library:
        if book['title'] == title:
            if book['available']:
                book['available'] = False
                borrowed_books.append({
                    'title': title,
                    'borrower': borrow,
                    'borrow_date' : datetime.now(),
                    'due_date': datetime.now() + timedelta(days=14) 

                })
                print(f'the book {title} is borrowed by {borrow}  Due date : {borrowed_books[-1]['due_date'].strftime('%Y-%m-%d')}')
                return
            else:
                    print(f"the book {title} is not available")
                    return
        print(f"the book {title} is not found in the library")
                    


def return_book(title):
    global borrowed_books, library
    for book in borrowed_books:
        if book['title'] == title:
            book['available'] = True
            borrowed_books.remove(book)
            print(f"the book {title} is returned")
            return
        print(f"the book {title} is not found in the borrowed books")
    print(f"Book '{title}' not found in the library.")


def view_all_book():
    if not library:
        print("the library is empty")

    else:
        for book in library:
            print(f"Title: {book['title']}, Auther: {book['auther']}, Genre: {book['genre']}, Available: {book['available']}")

def view_borrowed_book():
    if not borrowed_books:
        print("No books are currently borrowed.")
    else: 
        for book in borrowed_books:
            print(f"title : {book['title']},Borrower: {book['borrower']}, Borrow Date: {book['borrow_date'].strftime('%Y-%m-%d')}, Due Date: {book['due_date'].strftime('%Y-%m-%d')}")

def fine_for_over_duedate():
    current_data =datetime.now()
    for book in borrowed_books:
        if book['due_date'] < current_data:
            fine = (current_data - book['due_date']).days *10
            print(f'the fine for the book {book['title']} is ${fine}')
        else:
            print(f"the book {book['title']} is not over due")


def __main__():
    while True:
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Borrow Book") 
        print("5. Return Book")
        print("6. View All Book")
        print("7. View Borrowed Book")
        print("8. Fine for Over Due Date")
        print("9. Exit")

        choice = input("Enter you choice  1 to 9 : ")

        if choice == '1':
            title = input("Enter the title of the book: ")
            auther = input("Enter the auther of the book: ")
            genre = input("Enter the genre of the book: ")
            add_book(title,auther,genre)
        
        elif choice == '2':
            title = input("Enter the title of the book to remove: ")
            remove_book(title)

        elif choice == '3':
            t = input("Enter the title of the book to search: ")
            a = input("Enter the auther of the book to search: ")
            g = input("Enter the genre of the book to search: ")
            search(t,a,g)
        
        elif choice =='4':
            title = input(" Enter the title of the book to borrow: ")
            borrow = input("Enter your name: ")
            borrow_book(title,borrow)
        
        elif choice == '5':
            title = input('Enter the title of the book to return: ')
            return_book(title)

        elif choice == '6':
            view_all_book()
        

        elif choice == '7':
            view_borrowed_book()

        elif choice == '8':
            fine_for_over_duedate()
        

        elif choice == '9':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

            

if __name__ == "__main__":
    __main__()