books=[]
issued_books=[]
issued_books=[]
while True:
    print("\n--library management system--")
    print("1.add book")
    print("2.view book")
    print("3.search book")
    print("4.delete book")
    print("5.issued book")
    print("6.return book")
    print("7.exit")
    choice=input("enter choice:")
    if choice=="1":
        book=input("enter book name:")
        books.append(book)
        print("book added succesfully")
    elif choice=="2":
        print("\n books list:")
        for b in books:
            print(b)
    elif choice=="3":
        search=input("enter book name to search:")
        if search in books:
            print("book found")
        else:
            print("book not found")
    elif choice=="4":
        delete_book=input("enter book name to delete:")
        if delete_book in books:
            books.remove(delete_book)
            print("book deleted succesfully")
        else:
           print("book not found")
    elif choice=="5":
        issue_book=input("enter book name to issue:")
        if issue_book in books:
            books.remove(issue_book)
            issued_books.append(issue_book)
            print("book issued successfully")
        else:
           print("book not availsble")
    elif choice=="6":
        return_book=input("enter book name to return:")
        if return_book in issued_books:
            issued_books.remove(return_book)
            books.append(return_book)
            print("book returned successfully")
        else:
            print("book was not issued")
    elif choice=="7":
        print("thank you")
        break
    else:
        print("invalid choice")
