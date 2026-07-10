from tkinter import *

root = Tk()
root.title("Library Management System")
root.geometry("500x400")

Label(root, text="Library Management System",
      font=("Arial", 16, "bold")).pack(pady=10)

Label(root, text="Book Name").pack()

book_entry = Entry(root, width=30)
book_entry.pack(pady=5)

books = []

def add_book():
    book = book_entry.get()
    books.append(book)
    print("Book Added:", book)
    book_entry.delete(0, END)

Button(root, text="Add Book", command=add_book).pack(pady=10)

root.mainloop()