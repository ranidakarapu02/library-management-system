books = []
issued_books = []


def add_book():
    book = input("Enter book name: ")
    books.append(book)
    print("Book Added Successfully")


def view_books():
    print("\nBooks List:")
    
    if len(books) == 0:
        print("No Books Available")
    else:
        for b in books:
            print(b)


def search_book():
    search = input("Enter book name to search: ")

    if search in books:
        print("Book Found")
    else:
        print("Book Not Found")


def delete_book():
    delete_book_name = input("Enter book name to delete: ")

    if delete_book_name in books:
        books.remove(delete_book_name)
        print("Book Deleted Successfully")
    else:
        print("Book Not Found")


def issue_book():
    issue_book_name = input("Enter book name to issue: ")

    if issue_book_name in books:
        books.remove(issue_book_name)
        issued_books.append(issue_book_name)
        print("Book Issued Successfully")
    else:
        print("Book Not Available")


def return_book():
    return_book_name = input("Enter book name to return: ")

    if return_book_name in issued_books:
        issued_books.remove(return_book_name)
        books.append(return_book_name)
        print("Book Returned Successfully")
    else:
        print("Book Was Not Issued")


while True:

    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        delete_book()

    elif choice == "5":
        issue_book()

    elif choice == "6":
        return_book()

    elif choice == "7":
        print("Thank You")
        break

    else:
        print("Invalid Choice")